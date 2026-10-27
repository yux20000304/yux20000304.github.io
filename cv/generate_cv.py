"""Build the homepage CV from resume.json using ReportLab (Python 3.10+)."""

import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)


ROOT = Path(__file__).resolve().parent
ACCENT = colors.HexColor("#386887")
TEXT = colors.HexColor("#18222B")
MUTED = colors.HexColor("#52616B")
PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN = 48
# Platypus frames reserve 6 points of padding on each side.
WIDTH = PAGE_WIDTH - 2 * MARGIN - 12


def register_fonts():
    """Embed a complete serif family; support standard macOS and Linux fonts."""
    candidates = [
        (Path("/System/Library/Fonts/Supplemental"),
         ["Times New Roman.ttf", "Times New Roman Bold.ttf",
          "Times New Roman Italic.ttf", "Times New Roman Bold Italic.ttf"]),
        (Path("/usr/share/fonts/truetype/dejavu"),
         ["DejaVuSerif.ttf", "DejaVuSerif-Bold.ttf",
          "DejaVuSerif-Italic.ttf", "DejaVuSerif-BoldItalic.ttf"]),
    ]
    for directory, filenames in candidates:
        if all((directory / name).is_file() for name in filenames):
            for face, filename in zip(
                ["CV", "CV-Bold", "CV-Italic", "CV-BoldItalic"], filenames
            ):
                pdfmetrics.registerFont(TTFont(face, str(directory / filename)))
            pdfmetrics.registerFontFamily(
                "CV", normal="CV", bold="CV-Bold", italic="CV-Italic",
                boldItalic="CV-BoldItalic",
            )
            return
    raise RuntimeError("Install Times New Roman or DejaVu Serif to build the CV.")


def build(output):
    data = json.loads((ROOT / "resume.json").read_text())
    register_fonts()
    styles = {
        "body": ParagraphStyle("body", fontName="CV", fontSize=11, leading=13.6,
                               textColor=TEXT, spaceAfter=3),
        "small": ParagraphStyle("small", fontName="CV", fontSize=10, leading=12.3,
                                textColor=MUTED, spaceAfter=2),
        "heading": ParagraphStyle("heading", fontName="CV-Bold", fontSize=12,
                                  leading=14, textColor=ACCENT, spaceBefore=12,
                                  spaceAfter=4, keepWithNext=True),
        "name": ParagraphStyle("name", fontName="CV-Bold", fontSize=28,
                               leading=32, alignment=TA_CENTER, textColor=TEXT),
        "contact": ParagraphStyle("contact", fontName="CV", fontSize=10.3,
                                  leading=14, alignment=TA_CENTER, textColor=MUTED),
        "right": ParagraphStyle("right", fontName="CV", fontSize=10,
                                leading=13.6, alignment=TA_RIGHT, textColor=MUTED),
        "bullet": ParagraphStyle("bullet", fontName="CV", fontSize=10.5,
                                 leading=12.8, leftIndent=10, firstLineIndent=-8,
                                 textColor=TEXT, spaceAfter=2),
    }

    def p(text, style="body"):
        return Paragraph(text, styles[style])

    def section(title):
        rule = HRFlowable(width="100%", thickness=0.5, color=ACCENT, spaceAfter=6)
        rule.keepWithNext = True
        return [p(escape(title.upper()), "heading"), rule]

    def row(left, right, style="body", right_width=132):
        table = Table([[p(left, style), p(escape(right), "right")]],
                      colWidths=[WIDTH - right_width, right_width])
        table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ]))
        return table

    story = [p(escape(data["name"]), "name"), Spacer(1, 4)]
    email = escape(data["email"])
    story.append(p(
        f'<a href="mailto:{email}">{email}</a> &nbsp; | &nbsp; '
        f'{escape(data["phone"])} &nbsp; | &nbsp; '
        f'<a href="{escape(data["website"])}">Personal website</a> &nbsp; | &nbsp; '
        f'<a href="{escape(data["scholar"])}">Google Scholar</a>', "contact"))
    story += section("Research Profile")
    story.append(p(escape(data["summary"])))
    story += section("Education")
    for item in data["education"]:
        story.append(KeepTogether([
            p(f'<b>{escape(item["institution"])}</b>'),
            row(f'<i>{escape(item["degree"])}</i>', item["dates"]),
            p(escape(item["detail"]), "small"), Spacer(1, 5),
        ]))
    story += section("Publications")
    for index, item in enumerate(data["publications"], 1):
        authors = ", ".join(
            f"<b>{escape(name)}</b>" if name == data["name"] else escape(name)
            for name in item["authors"]
        )
        note = f' <b>{escape(item["note"])}</b>' if item.get("note") else ""
        story.append(KeepTogether([
            p(f'<b>[{index}] {escape(item["title"])}</b>'),
            p(authors + ".", "small"),
            p(f'<i>{escape(item["venue"])}</i>, {escape(item["year"])}.{note}'),
            Spacer(1, 7),
        ]))

    story.append(PageBreak())
    story += section("Research Experience")
    for item in data["research"]:
        group = [p(f'<b>{escape(item["title"])}</b>'),
                 row(f'<i>{escape(item["institution"])}</i>', item["dates"], "small")]
        group += [p("&#8226; " + escape(bullet), "bullet") for bullet in item["bullets"]]
        group.append(Spacer(1, 4))
        story.append(KeepTogether(group))
    story += section("Teaching Experience")
    item = data["teaching"]
    story += [p(f'<b>{escape(item["title"])}</b>'),
              row(escape(item["institution"]), item["dates"], "small")]
    story += section("Academic Service")
    for item in data["service"]:
        story.append(p(f'<b>{escape(item["role"])}</b>, {escape(item["venue"])}'))
    story += section("Selected Talks")
    for item in data["talks"]:
        story.append(KeepTogether([
            p(escape(item["title"])),
            row(f'<b>{escape(item["venue"])}</b>', item["date"], "small"),
            Spacer(1, 3),
        ]))
    story += section("Honors & Awards")
    for item in data["awards"]:
        story.append(row(escape(item["title"]), item["year"]))
    story += section("Technical Skills")
    story.append(p("<b>Programming:</b> " + escape(data["skills"])))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("CV", 9)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN, 28, f'{data["name"]} | Curriculum Vitae')
        canvas.drawRightString(PAGE_WIDTH - MARGIN, 28,
                               f'Updated {data["updated"]} | {doc.page}')
        canvas.restoreState()

    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output), pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=35, bottomMargin=43, title=f'{data["name"]} - Curriculum Vitae',
        author=data["name"], subject="Academic curriculum vitae",
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT.parent / "static/uploads/resume.pdf")
    build(parser.parse_args().output)

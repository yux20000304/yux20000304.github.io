# Homepage CV

Edit `resume.json`, then regenerate the PDF linked by the homepage:

```sh
python3 -m pip install reportlab
python3 cv/generate_cv.py
```

The renderer embeds Times New Roman on macOS or DejaVu Serif on Linux.
Use `--output /tmp/resume.pdf` to preview before replacing `static/uploads/resume.pdf`.
Render and inspect both pages after editing; check page count, text, links, and spacing.

Keep publication titles, author order, and status consistent with
`content/authors/admin/_index.md`. An acceptance year is not a formal publication date.
The source deliberately contains no unpublished manuscript links.

Content baseline: the previous homepage CV and confirmed homepage information.
The IEEE Transactions on Computers reviewer role was confirmed on October 27, 2026;
no service start date is asserted. The footer date is explicit in `resume.json`.

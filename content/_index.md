---
title: 'Home'
date: 2023-10-24
type: landing

design:
  layout: sidebar
  spacing: "clamp(1.5rem, 3vw, 2rem)"

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  - block: compact-biography
    id: section-resume-biography
    content:
      title: About
      username: admin
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      banner:
        filename: kalen-emsley-Bkci_8qcdvQ-unsplash.jpg
  - block: news
    content:
      title: News
      username: admin
    design:
      date_format: 'Jan 2, 2006'
  - block: compact-experience
    id: section-resume-experience
    content:
      title: Background
      username: admin
    design:
      # Hugo date format
      date_format: 'Jan 2006'
      # Education or Experience section first?
      is_education_first: false
  - block: publication
    content:
      title: Publications
      username: admin
  - block: talks
    content:
      title: Talks
      username: admin
    design:
      date_format: 'Jan 2, 2006'
  - block: compact-text
    id: academic-service
    content:
      title: Academic Service
      text: |-
        **Reviewer**, IEEE Transactions on Computers
  - block: compact-skills
    id: section-resume-skills
    content:
      title: Skills & Hobbies
      username: admin
---

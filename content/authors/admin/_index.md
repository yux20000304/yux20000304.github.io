---
# Display name
title: Yuxin Yang

# Name pronunciation (optional)
# name_pronunciation: Chien Shiung Wu

# Full name (for SEO)
first_name: Yuxin
last_name: Yang

# Status emoji
status:
  icon: ☕️

# Is this the primary user of the site?
superuser: true

# Role/position/tagline
role: PhD student at UCSC

# Organizations/Affiliations to display in Biography blox
# organizations:
#   - name: GenCoin
#     url: https://www.example.com/

# Social network links
# Need to use another icon? Simply download the SVG icon to your `assets/media/icons/` folder.
profiles:
  - icon: at-symbol
    url: mailto:yyang460@ucsc.edu
    label: E-mail Me
  - icon: brands/github
    url: https://github.com/yux20000304 
  - icon: brands/linkedin
    url: https://www.linkedin.com/in/yuxin-yang-6371a5345
  - icon: brands/google-scholar
    url: https://scholar.google.com/citations?user=-fEn4QcAAAAJ&hl=zh-CN

education:
  - area: PhD in Computer Architecture
    institution: University of California, Santa Cruz
    date_start: 2025-08-01
    date_end: 2030-06-30
    summary: |
      Research Topic: Security for CXL memory systems
    # button:
    #   text: 'Read Thesis'
    #   url: 'https://example.com'
  - area: Master in Computer Architecture
    institution: Huazhong University of Science and Techonology
    date_start: 2022-09-01
    date_end: 2025-06-30
    summary: |
      GPA: 87.3/100
      
      Research Topic: Learned Index in database systems, Distributed file systems, Flash-Friendly File System(F2FS)
  - area: B.E in Computer Science
    institution: Huazhong University of Science and Techonology
    date_start: 2018-09-01
    date_end: 2022-06-30
    summary: |
      GPA: 88.9/100

work:
  - position: Teaching Assistant
    company_name: University of California, Santa Cruz
    company_url: ''
    company_logo: ''
    date_start: 2026-03-01
    date_end: 2026-06-30
    summary: |
      Teaching Assistant for CSE 121 (Embedded System Design).

news:
  - title: 'Received a MICRO 2026 Student Travel Grant'
    date: '2026-10-13' # Homepage announcement date.
    category: 'Award'
    summary: |
      The grant supports my attendance at MICRO 2026.
  - title: 'ALT-index+ accepted to ACM TOS'
    date: '2026-10-13' # Homepage announcement date.
    category: 'Publication'
    summary: |
      Our extended ALT-index work adds non-blocking retraining and parallel bulkloading for concurrent memory systems.
  - title: 'Decoupled-DSM accepted to MICRO 2026'
    date: '2026-07-08'
    category: 'Publication'
    summary: |
      Our work introduces a scalable trusted execution environment for multi-host CXL disaggregated shared memory.
  - title: 'AIORE presented at NVMW 2026'
    date: '2026-03-09'
    category: 'Talk'
    summary: |
      I presented our work on adaptive incremental offloaded (re-)encryption for secure CXL memory.
  - title: 'ALT-index accepted to ICDE 2025'
    date: '2024-11-27'
    category: 'Publication'
    summary: |
      Our hybrid learned index for concurrent in-memory database systems will appear at ICDE 2025. [[Paper]](/uploads/ALT-Index_A_Hybrid_Learned_Index_for_Concurrent_Memory_Database_Systems.pdf) [[Slides]](/uploads/icde25_slides.pdf)
  - title: 'Best Paper nomination at ICCD 2023'
    date: '2023-11-08'
    category: 'Award'
    summary: |
      Our work on low-latency, scalable metadata management for distributed file systems was nominated for Best Paper. [[Paper]](/uploads/Low-Latency_and_Scalable_Full-path_Indexing_Metadata_Service_for_Distributed_File_Systems.pdf)

# work:
#   - position: Director of Cloud Infrastructure
#     company_name: GenCoin
#     company_url: ''
#     company_logo: ''
#     date_start: 2021-01-01
#     date_end: ''
#     summary: |2-
#       Responsibilities include:
#       - lorem ipsum dolor sit amet, consectetur adipiscing elit
#       - lorem ipsum dolor sit amet, consectetur adipiscing elit
#       - lorem ipsum dolor sit amet, consectetur adipiscing elit
#   - position: Backend Software Engineer
#     company_name: X
#     company_url: ''
#     company_logo: ''
#     date_start: 2016-01-01
#     date_end: 2020-12-31
#     summary: |
#       Responsibilities include:
#       - Migrated infrastructure to a new data center
#       - lorem ipsum dolor sit amet, consectetur adipiscing elit
#       - lorem ipsum dolor sit amet, consectetur adipiscing elit

# Skills
# Add your own SVG icons to `assets/media/icons/`
skills:
  - name: Technical Skills
    items:
      - name: C/C++
        description: ''
        percent: 80
        # icon: devicon/python
      - name: Python
        description: ''
        percent: 15
        icon: devicon/python
      - name: JAVA
        description: ''
        percent: 5
        # icon: devicon/pytorch
  - name: Hobbies
    color: '#eeac02'
    color_border: '#f0bf23'
    items:
      - name: Badminton
        description: ''
        percent: 60
        icon: custom/shuttlecock
      - name: Sleeping
        description: ''
        percent: 20
        icon: moon
      - name: Clash Royale
        description: ''
        percent: 20
        icon: custom/crown

        
# languages:
#   - name: English
#     percent: 100
#   - name: Chinese
#     percent: 75
#   - name: Portuguese
#     percent: 25

# Publications.
#   Add/remove as many publications below as you like.
#   Only `title`, `venue`, and `date` are required.
#   Optional: `venue_short`, `authors` (Markdown), `award`, `status`, and `links` (name/url).
#   Begin multi-line `summary` with YAML's `|` or `|2-` multi-line prefix and indent 2 spaces below.
publications:
  - title: 'ALT-index+: An Efficient Hybrid Learned Index for Concurrent Memory Systems'
    date: '2026-10-13' # Homepage update date; formal publication date pending.
    venue_short: 'TOS'
    venue: 'ACM Transactions on Storage (TOS)'
    status: 'Accepted'
    authors: 'Mengya Lei, **Yuxin Yang**, Fang Wang\*, Zhiwei Ye, Dan Feng.'
    summary: |
      Extends ALT-index with non-blocking retraining and parallel bulkloading for concurrent memory systems.

  - title: 'Decoupled-DSM: A Scalable Secure Trusted Execution Environment for Multi-Host CXL Disaggregated Shared Memory'
    date: '2026-01-01'
    venue_short: 'MICRO'
    venue: 'The 59th IEEE/ACM International Symposium on Microarchitecture (MICRO), 2026'
    status: 'Accepted'
    authors: '**Yuxin Yang**, Yuanchao Xu.'
    summary: |
      Keeps memory allocation on CXL devices and offloads permission checks to host-side trusted execution environments for secure multi-host shared memory.

  - title: 'ALT-index: A Hybrid Learned Index for Concurrent Memory Database Systems'
    date: '2025-05-21'
    venue_short: 'ICDE'
    venue: 'The 41st IEEE International Conference on Data Engineering (ICDE), 2025'
    authors: '**Yuxin Yang**, Fang Wang\*, Mengya Lei, Peng Zhang, Dan Feng;'
    summary: |
      We introduce a solution which combines the learned index and adaptive radix tree with a hybrid design.
    links:
      - name: Paper
        url: /uploads/ALT-Index_A_Hybrid_Learned_Index_for_Concurrent_Memory_Database_Systems.pdf
      - name: Slides
        url: /uploads/icde25_slides.pdf

  - title: 'Low-Latency and Scalable Full-path Indexing Metadata Service for Distributed File Systems'
    date: '2023-11-08'
    venue_short: 'ICCD'
    venue: 'The 41st IEEE International Conference on Computer Design (ICCD), 2023'
    award: 'Best Paper Nominee'
    authors: 'Chao Dong, Fang Wang\*, **Yuxin Yang**, Mengya Lei, Jianshun Zhang, Dan Feng;'
    summary: |
      We introduce a metadata management for distributed file systems.
    links:
      - name: Paper
        url: /uploads/Low-Latency_and_Scalable_Full-path_Indexing_Metadata_Service_for_Distributed_File_Systems.pdf

talks:
  - title: 'AIORE: Efficient Security Support for CXL Memory through Adaptive Incremental Offloaded (Re-)Encryption'
    date: '2026-03-09'
    awarder: 'NVMW 2026'
    summary: |
      **Yuxin Yang** presented this work at NVMW 2026.
  - title: 'ALT-index: A Hybrid Learned Index for Concurrent Memory Database Systems'
    url: /uploads/icde25_slides.pdf
    date: '2025-05-21'
    awarder: 'ICDE 2025'
    summary: |
      **Yuxin Yang** presented this talk at ICDE 2025. [[slides]](/uploads/icde25_slides.pdf)
#   - title: Blockchain Fundamentals
#     url: https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals
#     date: '2023-07-01'
#     awarder: edX
#     icon: edx
#     summary: |
#       Learned:
#       - Synthesize your own blockchain solutions
#       - Gain an in-depth understanding of the specific mechanics of Bitcoin
#       - Understand Bitcoin’s real-life applications and learn how to attack and destroy Bitcoin, Ethereum, smart contracts and Dapps, and alternatives to Bitcoin’s Proof-of-Work consensus algorithm
#   - title: 'Object-Oriented Programming in R'
#     url: https://www.datacamp.com/courses/object-oriented-programming-with-s3-and-r6-in-r
#     certificate_url: https://www.datacamp.com
#     date: '2023-01-21'
#     awarder: datacamp
#     icon: datacamp
#     summary: |
#       Object-oriented programming (OOP) lets you specify relationships between functions and the objects that they can act on, helping you manage complexity in your code. This is an intermediate level course, providing an introduction to OOP, using the S3 and R6 systems. S3 is a great day-to-day R programming tool that simplifies some of the functions that you write. R6 is especially useful for industry-specific analyses, working with web APIs, and building GUIs.
---

I am a second-year Ph.D. student in the Department of Computer Science and Engineering at the University of California, Santa Cruz, advised by [Prof. Yuanchao Xu](https://yuanchaoxu6.github.io/).
My research focuses on computer architecture and systems, with particular interests in secure memory systems, CXL-based memory disaggregation, trusted execution environments, and distributed file systems.

Before joining UCSC, I received my master's degree from the Wuhan National Laboratory for Optoelectronics at Huazhong University of Science and Technology (HUST), where I was advised by [Prof. Fang Wang](http://faculty.hust.edu.cn/wangfang16/en/index.htm) and [Prof. Dan Feng](http://faculty.hust.edu.cn/dfeng/en/index.htm). I also received my bachelor's degree in Computer Science from HUST.

Please feel free to contact me by email.

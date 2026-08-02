# Internship Application Kit (Japan + FAANG + Goldman Sachs)

Everything you need to apply for paid software engineering internships — researched from
official career pages, Reddit, LinkedIn, levels.fyi, and ATS studies (2026).

## What's inside

```
internship-kit/
├── README.md                     ← this file, your roadmap
├── resumes/
│   ├── resume-en-ats.tex           ← ⭐ STANDARD English resume template (LaTeX/Overleaf)
│   ├── resume-en-ats.md            ← same content as .tex, in plain Markdown (reference)
│   ├── resume-japan-english.tex    ← English resume template tuned for Japanese companies (LaTeX)
│   ├── resume-japan-english.md     ← same, plain Markdown (reference)
│   ├── rirekisho.tex               ← Japanese 履歴書 template (LaTeX/XeLaTeX)
│   ├── rirekisho-guide.md          ← Japanese 履歴書 format + translation (how to fill the .tex)
│   ├── shokumu-keirekisho.md       ← Japanese engineering work-history (職務経歴書)
│   ├── ── FINAL RESUMES (filled with your real info) ──
│   ├── resume-aditya-swe-faang.tex ← SWE generalist → Microsoft/Amazon/Google SWE interns
│   ├── resume-aditya-ml-engineer.tex← ML/AI Engineer → Google ML, ML/data-science roles
│   ├── resume-aditya-data-analyst.tex← Data Analyst → analyst/BI/data roles
│   ├── resume-aditya-web-dev.tex   ← Web/Frontend/Fullstack developer roles
│   ├── resume-aditya-goldman.tex   ← Goldman Sachs SWE Summer Intern (distributed systems focus)
│   ├── resume-aditya-japan.tex     ← Japan English resume (Mercari/Rakuten/Sony/LY/Google JP/HENNGE)
│   └── rirekisho-aditya.tex        ← Japan 履歴書 filled in (XeLaTeX — verify katakana/志望動機)
├── cover-letters/
│   ├── cover-letter-japan.tex    ← for Mercari / Rakuten / Sony / LY Corp (LaTeX)
│   ├── cover-letter-faang.tex    ← for Google / Meta / Amazon / Microsoft (LaTeX)
│   ├── cover-letter-goldman.tex  ← for Goldman Sachs / JPMorgan (LaTeX)
│   └── [same three .md versions] ← plain-text references
├── visa-documents/
│   └── visa-checklist.md        ← Designated Activities (Internship) visa docs
├── github-projects/
│   ├── projects-to-build.md     ← 6 hireable projects with tech stack + metrics
│   └── github-polish.md         ← how to make GitHub pass the 60-second recruiter test
└── checklists/
    ├── application-checklist.md ← master checklist for every application
    └── company-by-company.md    ← what each company specifically requires
```

## The 3 golden rules (from all the research)

1. **Format wins before content.** ATS studies (2,417 scans, 2026) found 62% of resumes
   have formatting errors. Single-column, plain text, no tables/icons. This alone is worth
   ~14 points.
2. **Tailor for every job.** Tailoring to a specific job description raises ATS match score
   by an average of 22 points — the single biggest lever.
3. **Japan: match the resume type to the company.**
   - English-first companies (Mercari, Rakuten, Google Japan, Sony, LY Corp): **English resume**
   - Traditional Japanese companies: **履歴書 (Rirekisho)**
   - When in doubt, submit both.

## How to use the LaTeX files (Overleaf)

All resumes and cover letters exist as `.tex` files ready to compile on **Overleaf**:

1. Go to **overleaf.com** → New Project → Blank Project (name it, e.g. `Resume`).
2. Delete the default `main.tex`, then **upload** the `.tex` file you want (or copy-paste its content into `main.tex`).
3. **Compiler setting (critical):**
   - English resumes (`resume-en-ats.tex`, `resume-japan-english.tex`, all `resume-aditya-*.tex`) and cover letters → **pdfLaTeX** (Overleaf default — just click Compile).
   - `rirekisho.tex` and `rirekisho-aditya.tex` (Japanese) → **XeLaTeX** (Menu → Compiler → XeLaTeX). Overleaf has the needed Japanese fonts built in.
4. Replace every `[bracketed]` placeholder with your info (the `resume-aditya-*` files are already filled in — just compile and download).
5. Click Compile → download the PDF. Check it visually: must be **exactly 1 page** for the English resume, no text overflowing margins.

## Resume to role mapping

| Target | Use this file |
|---|---|
| Microsoft / Amazon / Google SWE intern, generic SWE | `resume-aditya-swe-faang.tex` |
| Google ML, ML/AI or data-science roles | `resume-aditya-ml-engineer.tex` |
| Data Analyst / BI / analytics roles | `resume-aditya-data-analyst.tex` |
| Web / Frontend / Fullstack roles | `resume-aditya-web-dev.tex` |
| Goldman Sachs (and JPMorgan) SWE Summer | `resume-aditya-goldman.tex` |
| Mercari / Rakuten / Sony / LY / Google JP / HENNGE / Woven | `resume-aditya-japan.tex` |
| Traditional Japanese companies (HR asks for 履歴書) | `rirekisho-aditya.tex` (XeLaTeX) |

**Layout guarantees built in:** `geometry` margins (0.6in), `titlesec` section spacing, `enumitem` compact bullets, `parskip` for clean spacing, `hidelinks` so URLs are invisible but clickable — all standard packages that never misalign or spill off the page.

## Quick timeline

| Month | What to do |
|---|---|
| Now | Learn Python + DSA, build projects, polish GitHub (see github-projects/) |
| Aug–Dec | Apply to underclassman programs: Microsoft Explore, Amazon Future Engineer, Meta University, Google STEP |
| Sep–Dec | Apply to Japan internships: Mercari, Sony, HENNGE, Woven by Toyota, METI JIP |
| Dec–Mar | Interviews, offers |
| Apr+ | Internship begins / MEXT scholarship cycle next year |

## Start here

1. Read `resumes/resume-en-ats.md` and fill in your details.
2. Read `checklists/company-by-company.md` for the target company's exact requirements.
3. Read `github-projects/projects-to-build.md` and pick ONE project to start today.

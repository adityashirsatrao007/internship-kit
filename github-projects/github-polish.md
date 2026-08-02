# GitHub Polish — pass the 60-second recruiter test

**Researched from:** placement guides, hiring-manager write-ups, and what company career pages say (Mercari explicitly: "provide links to your GitHub, blog, or past work").

Recruiters and interviewers click your GitHub link from the resume and spend ~60 seconds deciding if you're real. Here's how to win that 60 seconds.

## The 60-second test (what reviewers check)
1. Is there a profile README with a clear bio? (yes = pass)
2. Are exactly 2–4 projects pinned? (pinned = these matter)
3. Do the pinned repos have live demo links? (deployed = pass)
4. Are the READMEs complete (screenshots, setup, limitations)? (documented = pass)
5. Is there regular commit activity? (alive = pass)
6. Any obvious red flags? (leaked API keys, empty repos, copied tutorials)

## Step-by-step polish plan

### 1. Profile README (github.com/YOURNAME/YOURNAME)
Create a repo named exactly `YOURNAME` and add a README.md:
- One-liner: who you are, what you build
- Current focus: e.g., "Building full-stack apps with Python + React; preparing for SWE internships"
- Links: portfolio, LinkedIn, LeetCode, email
- Keep it clean — no wall of emojis or ASCII art

### 2. Pin your BEST 3 projects
- Only 3 (any more and none stand out)
- These must match the projects on your resume — same names, same links (the "single story" rule)

### 3. Fix the READMEs (this is the highest-ROI work)
Each pinned repo README needs:
- **Badge-free, plain header** (name + 1-line description)
- **Live demo link** at the very top
- **Screenshots** (1–2)
- **Tech stack** list
- **Setup:** `git clone`, install, run — tested from a fresh clone
- **What was hard:** one honest sentence about a technical challenge (this is what interviewers probe)
- **One known limitation + next improvement** (shows self-awareness)

### 4. Clean the profile
- Remove old/dead repos from pinned (move to "repositories" tab is fine, just unpin)
- Delete junk repos or archive them
- Set a real avatar and a real name
- Add topics/descriptions to pinned repos (e.g., `fastapi`, `postgresql`, `react`)

### 5. Activity
- Commit at least 3–4 times a week while building (consistency signal)
- Use meaningful commit messages ("add JWT auth", not "update")
- A 2-month-old project with no recent commits is fine IF you're actively building new ones

## Red flags that get you filtered
- ❌ `.env` files or API keys committed (auto-disqualify — security)
- ❌ Repo named "project" or "test" or "new folder"
- ❌ README with only "this is my project"
- ❌ 100% fork of a tutorial with zero changes
- ❌ No live links anywhere

## The one-week turnaround (do this now)
- [ ] Create profile README
- [ ] Pin 3 best repos
- [ ] Rewrite the 3 READMEs (demo link + screenshot + limitation)
- [ ] Remove any committed keys/secrets (rewrite git history if needed)
- [ ] Set avatar + name + topics
- [ ] Commit the README fixes today

## Match the story across platforms
Your resume, GitHub, and LinkedIn must tell the SAME story:
- Same project names (resume says "Marketplace API" → GitHub repo is "marketplace-api")
- Same links
- LinkedIn Featured section → same 3 projects
- This consistency is what recruiters check — inconsistent stories = rejected

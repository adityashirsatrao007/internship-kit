# 6 Hireable Projects to Build (that get internship offers)

**Researched from:** dev.to portfolio guides, hiring-manager interviews, GreatFrontend, and what Mercari/Rakuten recruiters explicitly say they look for ("provide links to GitHub, blog, or past work").

## The rules that make a project hireable
1. Solves a real problem (even a small one you actually have)
2. Is deployed and usable (live URL, not just a repo)
3. Uses a tech relevant to the target company's stack
4. Has a story: why you built it, what was hard, what you learned
5. Has a README with: what it does, setup steps, screenshots, one limitation, architecture

**Build 3 of these — 1 backend, 1 full-stack, 1 DSA/AI — and pin them on your GitHub profile.**

---

## Project 1: Marketplace / E-commerce Backend (Mercari-style) — BACKEND
**Why it lands interviews:** Mercari, PayPay, Rakuten are all marketplace/payment companies. Building a listing+search backend directly mirrors their product.
- **Stack:** Python + FastAPI (or Java + Spring Boot), PostgreSQL, Docker
- **Features to include:**
  - REST API: items CRUD, search with filters, pagination
  - JWT authentication (users, roles)
  - Redis cache (adds a "wow" factor: cutting latency)
- **Metrics to claim:** handles X concurrent requests (load-test with a simple script), response time X ms, X unit tests at X% coverage
- **Deploy:** Docker + Render/Railway (free tiers)

## Project 2: Full-Stack Dashboard App (Expense Tracker / Job Tracker) — FULL-STACK
**Why it lands interviews:** Shows frontend + backend + state management + real product thinking. A job/internship tracker is meta (recruiters relate instantly).
- **Stack:** React + TypeScript, Node.js or FastAPI, PostgreSQL/SQLite, Tailwind
- **Features:** CRUD, filters, charts (data viz), empty/loading/error states, local persistence, mobile-responsive
- **Metrics:** N users, page load X s, handles N records, forms validated
- **Deploy:** Vercel (frontend) + Railway/Render (backend)

## Project 3: DSA Visualizer / Algorithm Practice Platform — DSA (shows CS rigor)
**Why it lands interviews:** Japanese recruiters specifically value documented complexity analysis. Visualizers prove you understand algorithms deeply, not just use them.
- **Stack:** React + TypeScript (no backend needed, or minimal)
- **Visualize:** sorting algorithms (bubble → quick → merge), pathfinding (BFS/DFS/A*), or linked-list/tree operations
- **Include:** step-by-step animation, time/space complexity notes per algorithm, tests
- **Metrics:** N algorithms, used by N fellow students, live demo link

## Project 4: AI Study Buddy / AI Chatbot with RAG — AI (hot in 2026)
**Why it lands interviews:** AI integration is an instant interviewer interest trigger in 2026. RAG (Retrieval-Augmented Generation) shows modern ML-adjacent skills.
- **Stack:** Python + LangChain (or LlamaIndex), ChromaDB vector store, OpenAI/Gemini API, Streamlit or Next.js UI
- **Features:** upload documents → ask questions → grounded answers with citations; chunking + embeddings + retrieval pipeline
- **Metric:** answers X% of test questions correctly (a number recruiters love)

## Project 5: Open Source Contribution Finder — API integration
**Why it lands interviews:** Uses the GitHub API, solves a real developer pain point, signals open-source literacy.
- **Stack:** React + GitHub API
- **Features:** find "good first issue" issues matching your languages, difficulty predictor (comment count + labels)
- **Metric:** X repos fetched, Y issues surfaced in <1s

## Project 6: Interview Prep Platform — complex, meta
**Why it lands interviews:** You built an interview-prep tool while prepping for interviews. Complex state management, very relatable.
- **Stack:** React + Node.js, or FastAPI + React
- **Features:** question bank (Blind 75/NeetCode), timer, progress tracking, note-taking, maybe AI feedback (Gemini API)
- **Metric:** N questions, M study sessions logged

---

## My recommendation for a beginner (in this order)
1. **Project 2** (full-stack — teaches the most fundamentals) — 2–3 weeks
2. **Project 3** (DSA visualizer — proves CS rigor for Japan) — 2 weeks
3. **Project 4** (AI chatbot/RAG — 2026 attention grabber) — 2 weeks

## What NOT to build
- Todo apps / calculators / "clone this tutorial" projects (no differentiation)
- Anything with no README, no demo, no tests
- A repo with 1 commit and a week of silence (looks abandoned)

## Every project must have
- [ ] README: problem → solution → setup → screenshots → one limitation → next steps
- [ ] Live demo link near the top
- [ ] .gitignore (no exposed API keys — this is checked!)
- [ ] Tests (at least some — signals engineering discipline)
- [ ] Consistent commits over the build period (shows process)
- [ ] Pinned on your GitHub profile with a clear name

# Deployment Guide (2026)

How to take the live-deployable repos from "repo" to "working URL" in a few clicks.
Everything below is **one-click ready** — no code changes needed.

---

## Which repos can go live (web apps with a UI/API)

| Repo | Type | Platform | Status |
|---|---|---|---|
| `production-cicd-template` | FastAPI web app + `/health` | Render | ✅ render.yaml committed |
| `rag-knowledge-assistant` | FastAPI RAG API + `/health` | Render | ✅ render.yaml committed |
| `error-tracking-observability-sdk` | FastAPI backend (docker) | Render | ✅ render.yaml committed (repo ref fixed) |
| `fir-digitization-legal-ai` | FastAPI backend (docker) | Render | ✅ render.yaml committed (repo ref fixed) |
| `ai-threat-detection` | FastAPI backend (docker) + React frontend | Render + Vercel | ✅ render.yaml fixed; vercel.json present |

The two data-pipeline repos (`nyc-taxi-data-pipeline`, `real-time-clickstream`) are **batch/streaming
pipelines** (Airflow/dbt and Kafka/Spark) — they run on docker-compose locally, not as public web
apps. They stay as CI-green repos + README architecture, which is what data-analyst recruiters
look at. Optional: deploy nyc-taxi's dbt to a free DuckDB/Duckpipes hosted run later.

---

## Option A — Render (fastest, free tier, handles both Python & Docker)

1. Go to https://render.com → Sign up with GitHub → **Authorize** the repos below.
2. **New → Blueprint** (recommended, reads `render.yaml`) → pick the repo.
   Render reads the committed `render.yaml` and provisions everything.
3. For `ai-threat-detection`: also deploy the frontend on **Vercel**:
   - vercel.com → Import repo → framework **Vite** → build `cd frontend && npm install && npm run build`,
     output `frontend/dist`, set `VITE_API_URL` to your Render backend URL.
4. After deploy, copy the `https://xxxx.onrender.com` URL into:
   - The repo README (replace any placeholder).
   - Your resume project lines (nice-to-have).

### Per-repo notes
- **rag-knowledge-assistant**: set `STORE_PATH=/app/chroma_db` (already in render.yaml). The app
  has a `/health` endpoint for Render's health check.
- **production-cicd-template**: python runtime, `uvicorn app.main:app --port $PORT` (already set).
- **error-tracking-observability-sdk / fir-digitization-legal-ai / ai-threat-detection**:
  `runtime: docker`, uses `./backend/Dockerfile` (already set). Requires filling env vars
  (DATABASE_URL, REDIS, SECRET_KEY) in the Render dashboard — `sync: false` values are
  intentionally blank and must be set once.

---

## Option B — Railway / Fly.io (alternatives)

- **Railway** (railway.app): click **New Project → Deploy from GitHub repo**. Railway auto-detects
  the Dockerfile/requirements. Free trial credit; keep service running with `railway up` or
  continuous deploy.
- **Fly.io** (fly.io): `fly launch` in a clone of the repo; generates `fly.toml`. Needs a card on
  file but has a free allowance. More manual than Render.

**Recommendation: use Render for all 5.** It reads the committed `render.yaml`, so it's literally
"Import → Deploy".

---

## After deploying — quick QA checklist

- [ ] URL loads (200) and `/health` returns `{"status":"ok"}` (or 200).
- [ ] One real request works (ask the API one question for RAG; open the dashboard for cicd-template).
- [ ] README badge/section updated with the live URL.
- [ ] Add the URL to the resume project line as "Live: <url>" (only for the repos listed above).
- [ ] Update `github-projects/master-hub.md` with the live URL next to each repo.

---

## What still needs YOUR account (I can't do these)

1. Render/Vercel accounts + authorizing the repos.
2. Pinning the 6 strongest repos on your profile (manual drag-and-drop, no API).

Everything code-side is done and verified.

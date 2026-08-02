# Interview Prep Pack — DSA Schedule + Behavioral + Question Bank

Goal: from "resume gets shortlisted" to "offer." Most rejections at interview stage come from
(1) weak DSA speed, (2) no STAR stories, (3) can't explain own projects under pressure.

Use alongside: `application-checklist.md` (what to do per stage) and your projects.

---

## Part 1 — DSA 6-week sprint (re-usable before every interview loop)

Based on the top-20 patterns interviewers actually use. ~2 problems/day, 45 min max each.

### Week 1 — Arrays & Strings (foundation)
- Two pointers (two-sum II, container with most water)
- Sliding window (max sum subarray, longest substring no repeat)
- Prefix sums (subarray sum = k)
- String manipulation (valid palindrome, reverse words)

### Week 2 — Hashmaps, Sorting, Intervals
- HashMap (group anagrams, top-k frequent)
- Intervals (merge, insert, non-overlapping)
- Sorting-based (k closest points, meeting rooms)
- Dutch flag / partition

### Week 3 — Linked Lists & Stacks/Queues
- Linked list (reverse, merge two, detect cycle, reorder)
- Monotonic stack (next greater element, daily temperatures)
- Queue/Deque (sliding window max)

### Week 4 — Trees & Graphs
- DFS/BFS (tree traversals, level order, max depth)
- Binary search tree (validate, kth smallest, LCA)
- Graph (number of islands, course schedule / topological sort, word ladder)
- Dijkstra (network delay time, cheapest flights)

### Week 5 — Recursion, Backtracking, DP
- Backtracking (permutations, subsets, combinations, N-queens)
- DP 1D (climbing stairs, house robber, coin change, word break)
- DP 2D (unique paths, longest common subsequence, edit distance, knapsack)

### Week 6 — Heaps, Binary Search, Harder + Mock
- Heap (top-k, kth largest, merge k sorted lists)
- Binary search on answer (split array largest sum, koko bananas)
- 2 mock interviews/day (see below), review mistakes, redo failed problems

### Mock-interview protocol (do at least 5 mocks before any real loop)
1. 45-min timed, 1 problem Medium/Hard, talk out loud.
2. State the brute force → optimize → correctness → test cases (this is what they grade).
3. After: write down what you missed. Redo the same problem 24h later from scratch.
4. Use peer mocks or free platforms (Pramp, LeetCode interview, friend).

---

## Part 2 — STAR behavioral stories (prepare 6, reuse everywhere)

Formula: **S**ituation (1-2 lines) → **T**ask (what you owned) → **A**ction (2-4 lines, "I" + verbs + specifics) → **R**esult (number/metric).

### Story 1 — Teamwork / collaboration (use hackathon-project-1)
- **S:** 24–48h hackathon, team of 3–4, building a multi-language error-tracking SDK.
- **T:** Owned the Python/Kotlin agents + the shared schema the other teammates' languages used.
- **A:** Defined the message contract first, wrote a stub, then each language agent implemented against it; I reviewed and merged, ran the integration tests.
- **R:** 3 languages integrated without rework; shipped a working demo; project placed/featured.

### Story 2 — Technical challenge / hard problem (use order-matching-engine)
- **S:** Wanted a low-latency matching engine; naive order book was O(n) for matching.
- **T:** Design a price-time priority engine that handles millions of orders/sec.
- **A:** Chose price-time priority FIFO, hash-map by price level + sorted containers, measured with a benchmark harness, iterated on hot-path.
- **R:** 10.9M orders/sec benchmark; the project became my fintech resume centerpiece.

### Story 3 — Leadership / initiative (use rag-knowledge-assistant or a college role)
- **S:** No one on the team had built RAG before.
- **T:** Get a citations-backed Q&A system over documents working end-to-end.
- **A:** Picked the stack (Chroma + FastAPI), built ingest→retrieve→answer pipeline, added an eval set so quality is measurable, documented for the team.
- **R:** 92% retrieval hit-rate on eval set; reusable pattern the team can copy.

### Story 4 — Failure / lesson learned (hackathon-project-2 or a project that broke)
- **S:** A feature/API shipped but crashed at startup in a deployed-like environment (e.g., Redis unreachable).
- **T:** Fix without blocking the whole app.
- **A:** Added graceful degradation — app starts, features that need the dependency no-op with a clear log; added a test to prevent regression.
- **R:** Startup crash fixed, resilience pattern reused in other services; I now design for failure by default.

### Story 5 — Conflict / disagreement (college team or hackathon)
- **S:** Two teammates disagreed on tech stack mid-project.
- **T:** Reach a decision without stalling.
- **A:** Listed criteria (time-to-demo, team skill, long-term value), asked each person to defend, made a call, got buy-in by showing the demo path.
- **R:** Picked the pragmatic stack, shipped on time; decision framework reused.

### Story 6 — Ambition / why this company (tailor per company)
- **S:** Why I'm applying (company's product/division), why I can contribute, what I want to learn.
- **T:** Connect my projects to their problem space (e.g., matching engine → Goldman/JPM trading infra; RAG → Google AI/ML; observability SDK → Microsoft/Mercari scale).
- **A/R:** 1 specific example of their engineering I admire + how my work maps to it.

> Practice each story as a 60-90 second spoken answer. Recruiters at FAANG/GS/Japan all ask the
> "tell me about a time" format — reuse these 6 everywhere, tailoring the ending to the company.

---

## Part 3 — Question bank by interview type

### DSA warm-ups (must be instant, <5 min)
Two-sum · valid palindrome · reverse linked list · merge two sorted lists · balanced parentheses ·
max subarray (Kadane) · binary search · BFS/DFS template · LRU cache · top-k frequent

### System-design-lite (intern level)
- Design a URL shortener / rate limiter / chat app / news feed
- Approach: scale numbers → API → storage → caching → where bottlenecks are → trade-offs

### ML-specific (for ML/AI resumes)
- Overfitting: causes + fixes (regularization, data aug, early stopping, dropout)
- Precision vs recall vs F1 — when each matters (tie to bert/sentiment repo)
- Train/val/test split + leakage (tie to ai-nids: why time-based split)
- Bias/variance; confusion matrix interpretation
- Why BERT/mBERT? (tie to Scopus paper — multilingual transfer)
- RAG: chunking, embedding, retrieval, evaluation (tie to rag repo)
- Imbalanced classes: the bank-marketing dataset → class weights, SMOTE, thresholds

### Data-specific (for Data Analyst resume)
- SQL: JOIN types, window functions (ROW_NUMBER, LAG), GROUP BY + HAVING
- Know your pipelines end-to-end (Airflow DAG → dbt → dashboard) — you built them
- Explain a metric: define daily active users, retention, funnel

### Behavioral (always asked)
- Tell me about yourself (60s: education → projects → why them)
- Why this company / why this role / why Japan (if applicable)
- Biggest project / hardest bug / failure / conflict (use Part 2 stories)

---

## What to bring to the interview
1. Your 2-3 core projects memorized: stack, your exact role, the hard part, one limitation, the metric.
2. 6 STAR stories rehearsed out loud.
3. 2 questions to ask them (engineering blog topic, team's biggest challenge).
4. Fresh water, clean video setup, links to repos ready in chat.

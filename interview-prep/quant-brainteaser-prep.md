# Quant + Brainteaser Prep (Goldman / JPM / Citadel / Jane Street / Two Sigma)

For finance-adjacent interviews (Goldman Sachs Summer Analyst, JPMorgan, and any trading firm
that screens numeracy). Separate from DSA — these test speed math, probability, and market logic.

---

## Part 1 — Mental-math speed (train daily, 5 min)
- Multiplication of two-digit numbers, percentages, fractions ↔ decimals
- Divisibility rules (2,3,5,9,11) — instant rejection if you're slow here
- Compound growth: rule of 72, doubling time
- Do 10 random mental-math drills every day until fluent

## Part 2 — Must-know probability facts
- P(A or B) = P(A)+P(B)−P(A∩B); P(A and B) = P(A)·P(B|A)
- Expected value = Σ value·probability (be able to set up instantly)
- Birthday problem (~23 people → 50% collision)
- Monty Hall; coin-flip streak expectations
- Bayes' rule — Goldman loves it (e.g., disease-testing, spam-filter examples)

## Part 3 — Brainteasers (Goldman/JPM classic)

### Easy (answer in ~1 min)
1. **Coin flips:** Expected number of flips to get first heads? → **2**
2. **Cards:** Probability a single card is a face card (J/Q/K)? → **12/52 = 3/13**
3. **Die:** Expected value of one fair 6-sided die? → **3.5**
4. **Socks:** Drawer with 10 black, 10 white socks. Min draws to guarantee a matching pair? → **3**
5. **Clock:** How many times do clock hands overlap in 12 hours? → **11**

### Medium (2-3 min)
6. **Coin streak:** Expected flips to get 2 heads in a row? → **6** (2^1 + 2^2 = 6)
7. **Rope burn:** Two ropes, each burns in 60 min but unevenly. Time exactly 45 min? → burn one at both ends (30) and start it when lighting second at one end, then light second's other end at the 30-min mark → 15 more.
8. **10 jars, one fake:** 10 jars of pills, one jar's pills are 1g lighter. Weigh once to find it? → take 1 pill from jar1, 2 from jar2... weigh; the shortfall tells the jar.
9. **Ants on a plank:** 100 ants, random directions, collide and turn around. Time until all fall off? → **same as if they pass through each other**: max distance / speed.
10. **Two trains:** 100 km apart, 100 km/h, fly at 200 km/h shuttling between them. Distance flown before collision? → 100 km (fly flies for the 0.5h until collision, at 200 km/h = 100 km).

### Hard (show structured thinking — they want the method, not just the number)
11. **N dice:** Expected sum of N fair dice = 3.5N. Prove in one line.
12. **Random chord length** (a circle, random chord vs side length) → say "this is Bertrand's paradox, answer depends on how you define random" — showing you know it's ill-posed is the correct answer.
13. **50 prisoners, 2 doors** (one escape, one death, half the group must be told the truth, half lies) → the classic guard question: "Which door would the other guard say is safe?" → take the opposite.
14. **Selling at a loss but net profit:** bought for $5 sold for $6, bought again for $7 sold for $8 → **+$2 total** (track cash flow, don't overthink).

## Part 4 — Finance/CS logic questions (GS/JPM-specific)
- **HackerRank:** Goldman uses HackerRank coding (DSA), then a **video interview** (HireVue-style: answer a prompt on camera). JPMorgan: HackerRank + HireVue too.
- Know **what the division does**: GS Engineering / Global Markets / Quant Strats; JPM Global Markets / Corporate & Investment Bank (CIB). Tailor "why us" to the division.
- Market logic: what moves a stock price? (supply/demand, earnings, rates, sentiment) — they like simple, correct answers over jargon.

## Part 5 — Where this matters vs your resume
- Your **order-matching-engine** (10.9M orders/sec, price-time priority FIFO) is the perfect anchor for market-infra questions.
- **nyc-taxi-data-pipeline** shows you understand real financial-scale data pipelines.
- Practice telling both in 60 seconds BEFORE the HackerRank/video stage.

---

## 1-week quant cram (if interview is soon)
- Day 1: mental math + divisibility drills
- Day 2: probability rules + expected value + Bayes
- Day 3: brainteasers easy+medium (1-10 above)
- Day 4: hard brainteasers + structured-thinking method
- Day 5: finance/CS logic + Goldman/JPM division research
- Day 6-7: 2 timed mock HackerRanks + 2 timed HireVue-style video answers (record yourself)

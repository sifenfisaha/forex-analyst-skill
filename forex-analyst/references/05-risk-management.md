# 05 — Risk Management (the part that actually makes you profitable)

**This is the most important file in the skill.** Edge is meaningless without risk control. A 70%-win strategy still blows an account if size is reckless. Protect capital first; profit is what's left after you've survived.

## The user's hard rules

| Rule | Value |
|---|---|
| **Risk per trade** | **0.5%–1%** of account equity. Default **1%**; drop to **0.5%** for B-grade or pre-news. |
| **Minimum reward-to-risk** | **1:3** (3R). No exceptions. |
| **Max concurrent risk** | ≤ **2%** total open across all positions (correlated pairs count as one risk). |
| **Daily loss limit** | **−3%** (or **2 losing trades**), whichever first → **stop for the day.** |
| **Weekly loss limit** | **−6%** → stop for the week, review the journal. |

If a setup can't satisfy **≥1:3 with a logical stop and a real liquidity target**, it is a **NO-TRADE**. Never widen the stop or shrink the target to fake the ratio.

---

## Position sizing — the formula

```
Risk amount ($)      = Account equity × Risk %
Stop distance (pips) = |Entry − Stop|  (in pips)
Position size (lots) = Risk amount ($) / (Stop distance in pips × Pip value per lot)
```

**Pip values per 1.00 standard lot** (quick reference, USD account):
- Pairs with **USD as quote** (EURUSD, GBPUSD, AUDUSD…): **$10 / pip** per standard lot.
- **XAUUSD (gold):** ≈ **$10 per $1.00 move** per 100-oz lot (1 pip = $0.10 move → $1/pip per lot on many brokers — **always confirm the broker's contract spec**).
- **JPY quote** (USDJPY, GBPJPY…): pip = 0.01; pip value ≈ **$1000 / USDJPY price** per lot (~$6.7/pip at 150). 
- Lot tiers: standard = 1.0 ($10/pip), mini = 0.1 ($1/pip), micro = 0.01 ($0.10/pip) for USD-quote majors.

**Always use `scripts/position_size.py` for the actual number** — it handles the arithmetic and prints the RR. Don't eyeball lot size.

### Worked example
- Account: $10,000. Risk: 1% = **$100**.
- EURUSD long, entry 1.0850, stop 1.0830 → **20 pips** risk.
- Size = $100 / (20 × $10) = **0.5 lots**.
- Target 1.0910 (60 pips) = **3R = $300**. ✅ meets 1:3.

---

## Stop placement (where, and why)

- Place the stop **beyond the invalidation**, not at a round guess. For CRT: just past the **swept wick / OB origin** + a **spread buffer**.
- The stop answers: *"At what price is my idea simply wrong?"* If price trades there, the sweep wasn't a sweep — get out.
- **Never** place the stop where it's *convenient* for sizing. Size adjusts to the stop, not the other way around.
- Account for **spread & slippage**, especially around news and on JPY/gold. Add a few pips buffer beyond the technical level.

## Target placement
- **TP1:** opposite side of the CRT range / nearest opposing liquidity → bank partials, move to break-even.
- **TP2:** next external liquidity pool (PDH/PDL, equal highs/lows, session extreme).
- Targets must be **real liquidity**, not arbitrary R multiples. The 3R *minimum* must coincide with an actual draw on liquidity, otherwise the target is fantasy.

---

## Trade management (after entry)

1. **Partial at TP1** (e.g., close 50%), move stop to **break-even**. Now it's a risk-free runner.
2. **Trail** the remainder behind LTF structure (each new HL in a long / LH in a short) toward TP2.
3. **Don't micromanage** out of fear — if the thesis (sweep + MSS holding) is intact, let it work to target.
4. **Cut early only** if structure invalidates *before* the stop (e.g., opposite MSS against you). A broken thesis ≠ wait for the stop.
5. **No averaging down.** Adding to a loser violates the fixed-risk model. One idea, one risk.

---

## Daily-loss guardrail (enforce this in the verdict)

Track the day's outcomes in conversation. After the user reports:
- **2 losses** in the session, **or** cumulative **−3%** → respond: **"Daily stop hit. Done trading today. Journal the trades and walk away."** Do not provide new setups that day even if asked — protecting the user from tilt is part of the job.
- A **revenge-trade pattern** (sizing up after a loss, chasing) → call it out directly and recommend stepping away.

## Prop-firm note (if relevant)
If the user trades a funded/prop account (FTMO-style), the binding constraints are usually:
- **Daily drawdown** (e.g., −5% from day-start balance) → our −3% rule keeps a safe buffer.
- **Max overall drawdown** (e.g., −10%) → never let cumulative risk approach it; halve size after a −6% week.
- Favor **0.5% risk** on prop to stretch the drawdown buffer across more trades.

---

## The expectancy reality check

Profitability = **Win% and Avg-RR together**, not win rate alone.

```
Expectancy (R) = (Win% × Avg win in R) − (Loss% × 1R)
```

At **1:3 RR**, you only need to win **~26%** of trades to break even; **35–40%** is solidly profitable. This is *why* the 1:3 minimum exists — it lets you be wrong more than half the time and still grow. **Stop chasing win rate; protect the RR.**

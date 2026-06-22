# 08 — Trade Plan Output Template

Every analysis ends with **one** of the two formats below. Be concise, specific, and numeric. No vague hedging.

---

## FORMAT A — Trade Plan (setup passed the scorecard)

```
📋 TRADE PLAN — <PAIR> <DIRECTION ▲LONG / ▼SHORT>   [Grade: A+ / B]

THESIS (1–2 lines):
<e.g., "D1 bullish, price swept Asian low + PDL in the London KZ and shifted bullish on M5 with displacement. Targeting buy-side at PDH.">

BIAS & STRUCTURE:
• HTF bias:        <D1 bullish / H4 bearish / etc.>
• Premium/Discount: <price in discount, OTE 70%>
• Sweep:           <which liquidity was taken>
• Confirmation:    <MSS on M5 + FVG at xxxx>

THE LEVELS:
• Entry:    <price>   (<FVG / OB zone>)
• Stop:     <price>   (<beyond swept wick + buffer>)   = <NN> pips
• TP1:      <price>   (<opposite range edge / liquidity>)  = <R>  → take 50%, BE
• TP2:      <price>   (<external liquidity pool>)           = <R>
• RR:       1 : <X.X>   ✅ (meets 1:3 minimum)

RISK & SIZE:
• Risk:     <0.5–1%> of account = $<amount>
• Size:     <lots> (from position_size.py)
• Max risk respected: ✅

TIMING & NEWS:
• Session:  <London KZ / NY AM KZ>  — valid window: <times ET>
• News:     <clear / "CPI at 8:30 ET — wait until 9:00">

MANAGEMENT:
• At TP1: close 50%, stop → break-even.
• Trail remainder behind M5 structure to TP2.
• Invalidation: <the price/condition that kills the idea — exit if hit before stop>.

SCORECARD: <7/10 — A+>
```

Keep it tight. The user should be able to act on it in 20 seconds.

---

## FORMAT B — No-Trade Verdict (setup failed)

```
🚫 NO-TRADE — <PAIR>

WHY: <the single most important reason — pick the first that applies>
   • No clear HTF bias (price mid-range / chop), OR
   • No liquidity sweep yet, OR
   • Sweep present but NO structure shift (unconfirmed), OR
   • RR < 1:3 (target too close / stop too wide), OR
   • High-impact news in the window, OR
   • Wrong session (Asian / NY lunch / late Friday), OR
   • Counter-trend into strong HTF momentum.

WHAT WOULD MAKE IT TRADEABLE:
   <the specific missing ingredient — e.g., "wait for M5 to shift bullish after this low sweep">

SET AN ALERT ON:
   <price level / time window to watch — e.g., "alert at 1.0820 (PDL) during London KZ">

GRADE: <C — marginal / D — skip>
```

---

## Tone & delivery rules

- **Numbers, not adjectives.** "Stop at 1.0830 (18 pips)" beats "a tight stop."
- **Name the liquidity.** Always say *which* pool was swept and *which* is the target.
- **State invalidation explicitly.** The user must know what proves the idea wrong.
- **Own the verdict.** Trade plan or no-trade — never "could go either way."
- **One screen.** If the plan runs longer than a screen, it's over-explained — trim it.
- **End with the grade** so the user instantly knows the conviction level.

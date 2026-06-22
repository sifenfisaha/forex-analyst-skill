# 01 — Candle Range Theory (CRT) Playbook

CRT is the user's primary engine. Master it. Everything else (structure, liquidity, sessions) feeds the CRT execution.

## The one-sentence definition

**Map a higher-timeframe candle as a price *range*, then trade the moment price sweeps one edge of that range (manipulation) and reverses back inside, heading for the opposite edge.**

The high and low of the chosen HTF candle are **liquidity pools**. Price reaches above/below them to grab orders, then expands the other way.

---

## AMD — the engine underneath CRT

Every CRT range is one cycle of **Accumulation → Manipulation → Distribution** (a.k.a. the **Power of Three / PO3**). Institutions don't fill large positions at one price; they build inside a range, push price the *wrong* way to trap retail and harvest liquidity, then drive the real move.

| Phase | What it looks like | What it means | What you do |
|---|---|---|---|
| **Accumulation** | Tight range / consolidation. The "body" of the CRT candle. | Smart money building positions; orders resting above & below. | Mark the range high & low. Wait. |
| **Manipulation** | A sharp wick/spike that sweeps the range high OR low (a "purge" / Judas swing / turtle soup). | Stops hunted, liquidity grabbed, weak hands trapped. | **This is your trigger.** Watch for rejection back inside. |
| **Distribution** | Strong displacement toward the *opposite* side of the range. | The real, intended move. | Enter on the retrace; target the opposite liquidity. |

**Core insight:** the manipulation leg is a *fake-out against the eventual direction*. Sweep of the **high** → bias **short**. Sweep of the **low** → bias **long**. Trade *with* the distribution, *against* the manipulation.

---

## The 3-candle CRT model (the classic pattern)

On the HTF, CRT often reads as three candles:

1. **Candle 1 — the Range.** Defines the high and low. This is your dealing range / accumulation.
2. **Candle 2 — the Manipulation.** Its wick **sweeps beyond Candle 1's high or low**, then **closes back inside Candle 1's range**. The close-back-inside is the key tell — the sweep failed.
3. **Candle 3 — the Distribution.** Expands toward the opposite extreme of Candle 1's range (and often beyond, to external liquidity).

> If Candle 2 sweeps the low and closes back inside → expect Candle 3 to expand UP. You are looking for **longs**.
> If Candle 2 sweeps the high and closes back inside → expect Candle 3 to expand DOWN. You are looking for **shorts**.

A **valid CRT** needs the sweep to *close back inside the range*. A candle that sweeps and **closes outside** is a breakout/continuation, NOT a CRT reversal — do not fade it.

---

## Timeframe pairings (HTF range → LTF execution)

CRT is fractal; pick a clean pairing and stay consistent. For this user's **intraday** style, the primary pairings are:

| CRT range (HTF) | Execution / entry (LTF) | Best for |
|---|---|---|
| **Daily candle** | M15 → M5 | Primary intraday bias; sweep of PDH/PDL |
| **H4 candle** | M5 → M1 | Session-based intraday trades (London/NY) |
| **H1 candle** | M1 | Scalp-style refinement inside a killzone |

**Default recommendation:** use the **Daily or H4 candle** as the CRT range and execute on **M15/M5** inside the London or NY AM killzone.

The cleanest CRT ranges form on **Daily, H4, and H1**. Asian-range highs/lows are premium liquidity that London frequently sweeps (classic CRT).

---

## The full CRT entry sequence (intraday)

1. **Frame the range.** Mark the high & low of the chosen HTF candle (e.g., today's daily open range, or the Asian session range, or the prior H4).
2. **Wait for the killzone.** Most clean manipulations happen in the London KZ or NY AM KZ (see `04-sessions-killzones.md`). Outside those windows, lower your expectations.
3. **Wait for the sweep.** Price must trade *beyond* the range high or low and take the resting liquidity. No sweep = no trade.
4. **Drop to the LTF and demand a shift.** After the sweep, require a **Market Structure Shift (MSS / CHoCH)** on M5/M1 — price breaks the most recent LTF swing in the new direction, ideally with **displacement** (a strong candle that leaves an **FVG**). This is your confirmation the sweep is real.
5. **Enter on the retrace into a PD array.** Place the entry in the **FVG** or **Order Block** left by the displacement leg. Don't chase — let price come to you.
6. **Stop** goes just beyond the swept extreme (the wick of the manipulation) + spread buffer. That's the invalidation: if price runs the sweep further, the CRT failed.
7. **Targets:** the **opposite side of the CRT range** (internal liquidity) as TP1, then the next **external liquidity** pool (PDH/PDL, prior session H/L, equal highs/lows) as TP2.
8. **Confirm RR ≥ 1:3** before committing. If the opposite range edge isn't ≥ 3R away, either the stop is too wide or the trade is too late — stand aside.

---

## Quarterly Theory (advanced timing overlay — optional)

CRT pairs powerfully with **Quarterly Theory**: time is divided into recurring AMD quarters. Each cycle of 4 splits into Accumulation → Manipulation → Distribution → Continuation/Reversal.

- **Yearly →** 4 quarters of 3 months.
- **Monthly →** 4 weeks.
- **Weekly →** the trading days (Mon = accumulation, Tue/Wed = manipulation+expansion often the weekly high/low forms Tue/Wed).
- **Daily →** four 6-hour quarters (00:00, 06:00, 12:00, 18:00 NY time).
- **90-minute cycles →** each 6h quarter splits into four 90-min "micro" sessions, each its own AMD.

Use it to **anticipate WHEN** the manipulation→distribution flip is likely (e.g., London open manipulating the Asian range, NY open manipulating the London range). Don't overfit; use it as a timing confluence, not a standalone signal.

---

## CRT failure modes (when NOT to take it)

- **Sweep closes *outside* the range** → that's continuation/breakout, not CRT. Don't fade.
- **No MSS after the sweep** → the reversal isn't confirmed. Wait or skip.
- **Range is too small / price is mid-range** → no clean liquidity to target; poor RR.
- **Sweep happens dead in the Asian session or NY lunch** → low-probability timing; demand more confluence or skip.
- **High-impact news inside the window** → the "manipulation" may just be a news spike with no follow-through structure. Stand aside (conservative profile).
- **Counter-trend into strong HTF momentum** → CRT works best when the distribution aligns with HTF bias *or* at a clear HTF extreme. Fading a freight-train trend mid-move is low probability.

---

## Quick CRT checklist (use in the scorecard)

- [ ] HTF CRT range clearly marked (high & low = liquidity)
- [ ] Price swept one edge of the range
- [ ] Sweep closed back inside (failed breakout)
- [ ] Sweep happened in/near a killzone
- [ ] MSS/CHoCH confirmed on execution TF, ideally with displacement + FVG
- [ ] Entry sits in an FVG or OB from the displacement leg
- [ ] Opposite range edge / next liquidity is ≥ 3R away
- [ ] No high-impact news in the entry window
- [ ] Direction aligns with HTF bias OR price is at a clean HTF extreme

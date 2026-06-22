# 03 — Liquidity & PD Arrays

Price moves **from liquidity to liquidity**. Smart money needs resting orders to fill large positions, so price is engineered toward pools of stops. If you know where liquidity rests, you know the *draw* — the magnet price wants to reach.

## Liquidity = resting orders (where stops sit)

- **Buy-side liquidity (BSL):** rests **above** highs (old highs, equal highs, PDH, session highs). Made of buy-stops from shorts' stop-losses + breakout buyers. Price runs **up** into it to harvest, then often reverses.
- **Sell-side liquidity (SSL):** rests **below** lows (old lows, equal lows, PDL, session lows). Made of sell-stops. Price runs **down** into it, then often reverses.

### Key liquidity reference points (mark these every session)
- **PDH / PDL** — previous day high / low.
- **PWH / PWL** — previous week high / low (for context).
- **Asian session range** high & low — classic liquidity London sweeps.
- **Prior session high/low** (London high/low going into NY).
- **Equal highs / equal lows** — two+ touches at the same level = an obvious, juicy stop pool ("liquidity magnet"). Often gets swept.
- **Obvious trendline touches** — retail trendline stops cluster here.
- **Round numbers** (00 / 50 levels) — psychological stop clusters.

---

## Liquidity sweep / raid / purge (the trigger)

A **sweep** = price spikes *beyond* a liquidity level, grabs the stops, then **rejects back**. This is the manipulation phase of AMD and the heart of a CRT entry.

- **Confirmed sweep:** wick beyond the level + close back on the origin side (failed breakout). Best when it leaves a clear rejection and is followed by an MSS.
- **Not a sweep (continuation):** price closes *and holds* beyond the level with displacement → that's a genuine break / expansion. Don't fade it.

> **The single most important entry filter in CRT:** a real sweep is followed by a *structure shift back the other way*. Sweep **without** a shift = price may keep going. Wait for the shift.

### Inducement (the trap before the trap)
**Inducement** is a *minor* liquidity pool (a small obvious high/low) placed *before* the real point of interest. Smart money runs inducement to fuel the move into the real OB/FVG. Practically: a small swing that looks like a great entry is often bait — the real fill is slightly deeper. Don't grab the first obvious level; let inducement get taken, then enter at the deeper array.

---

## PD Arrays — your entry zones (Premium/Discount Arrays)

After a sweep + MSS, you enter on the **retrace into a PD array** left by the displacement leg.

### Fair Value Gap (FVG) — imbalance
A **3-candle** pattern where the middle candle is so strong that **candle-1's high and candle-3's low don't overlap** (bullish FVG; inverted for bearish). The gap = inefficient, one-sided delivery. Price tends to **return to fill** part of it before continuing.
- **Entry:** place limit/zone at the FVG edge or 50% of the gap (the **Consequent Encroachment**).
- A **stacked** set of FVGs in the trend direction = strong displacement = quality.

### Order Block (OB)
The **last opposite-color candle before a strong displacement move**.
- **Bullish OB** = last *down* candle before a strong up-move → demand zone, look to buy its return.
- **Bearish OB** = last *up* candle before a strong down-move → supply zone, look to sell its return.
- Highest quality when the OB **created the sweep + MSS** and is paired with an FVG ("OB + FVG confluence").

### Breaker Block
A **failed OB that price broke through, then returns to use as the opposite role.** A bullish OB that gets violated and flips into resistance becomes a bearish breaker. Strong continuation entries after a structure shift.

### Mitigation Block
An OB that price returns to in order to "mitigate" (offload/refill) prior positions. Similar use to OBs; think of it as smart money getting to break-even on trapped orders.

### Rejection / Wick
A long wick into a level shows aggressive rejection — useful confirmation, and the wick origin can act as a mini-array.

---

## How to combine them (the entry stack)

The A+ entry is a **confluence stack**, not a single line:

```
Liquidity sweep (BSL/SSL taken)
        ↓
MSS / CHoCH with displacement (leaves an FVG)
        ↓
Retrace into OB + FVG confluence, in discount/premium, inside OTE (62–79%)
        ↓
Entry — stop beyond the swept wick, target the opposite liquidity (≥3R)
```

When 3–4 of these line up at one price, that's your A+ zone. One alone is a coin flip.

---

## Draw on liquidity — naming the target

Before entering, answer out loud: **"What liquidity is price drawing toward?"**
- If longs: which BSL above (equal highs / PDH / session high) is the target? Is it ≥3R away?
- If shorts: which SSL below (equal lows / PDL / session low)?

If you can't name a clean liquidity target that's ≥3R away, the trade has no logical destination → **NO-TRADE**. Liquidity gives both the *reason* and the *target*.

---

## Visual checklist (off a screenshot)

- [ ] Marked PDH/PDL and Asian range high/low
- [ ] Marked equal highs/lows and obvious swing liquidity
- [ ] Identified which side just got **swept** (and did it close back inside?)
- [ ] Found the displacement leg and its **FVG**
- [ ] Found the **OB** at the origin of the move
- [ ] Named the **draw on liquidity** (the target pool) and checked it's ≥3R away

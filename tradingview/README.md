# TradingView Indicator — Forex Analyst (CRT + Price Action)

A Pine Script™ v5 indicator that puts the `forex-analyst` skill's framework **live on your TradingView chart**. It's the *eyes*; the Claude skill stays the *analyst*.

**Open source (MIT). No password gate. No expiry. No Telegram upsell.**

## What it shows live

| On the chart | What it is |
|---|---|
| **BOS / CHoCH labels** | Market-structure breaks (continuation vs change of character) |
| **CRT range** (2 bold lines + midline) | The previous higher-timeframe candle mapped as a range — high/low = liquidity |
| **Premium / Discount shading** | Upper half = sell zone, lower half = buy zone, split at equilibrium |
| **PDH / PDL** (orange) | Previous day high/low liquidity |
| **Asian range** (purple) | Asian-session high/low — the liquidity London sweeps |
| **▲ / ▼ sweep markers** | Price raided the CRT range and closed back inside (manipulation) |
| **FVG boxes** | Fair value gaps (imbalance) |
| **Killzone shading** | London KZ (blue) + NY AM KZ (orange), in NY time |
| **BUY / SELL labels** | A sweep + structure shift aligned (optionally inside a killzone) |
| **Trade levels** | Auto entry / stop / TP1–3, RR-to-target, position size, with a **1:3 gate** |
| **Dashboard** | Bias, session, range zone, sweep status, last RR, lot size, confluence grade /5 |
| **Alerts** | Buy, Sell, CRT sweep (high/low), bullish/bearish structure break |

## How to install on TradingView

1. Open **TradingView → any chart → Pine Editor** (bottom panel).
2. Open `forex-analyst.pine` from this folder, **copy the whole file**, paste it into the Pine Editor (replace the default template).
3. Click **Save** (name it anything), then **Add to chart**.
4. Open the indicator's **⚙ Settings** to tune it (see below).
5. *(Optional)* Make it permanent: Pine Editor → **⋯ → Add to favorite indicators**, or pin it via the chart's indicator list.

> You do **not** need a paid TradingView plan for this. No login to any external service, no key to enter.

## Recommended settings (matches the skill)

- **Chart timeframe:** M15 or M5 (intraday execution).
- **CRT higher timeframe:** `D` (Daily) or `240` (H4) — must be *higher* than your chart TF.
- **Timezone:** `America/New_York` (institutional standard; killzone times assume it).
- **Risk:** Account size + `Risk %` (0.5–1) + `Minimum reward-to-risk` (3).
- **Pip size / pip value:** `0.0001` & `~10` for USD-quote majors; `0.01` for JPY pairs and Gold (confirm with your broker).
- **Only signal inside a killzone:** ON (higher-probability windows only).

## How to read it (the workflow, on-chart)

1. **Bias** from the dashboard + BOS/CHoCH labels → which way are we leaning?
2. Price reaches the **CRT high/low** or **PDH/PDL / Asian** liquidity and you see a **sweep marker** (▲/▼).
3. A **BUY/SELL** label prints when structure shifts back after the sweep, inside a killzone.
4. The **trade levels** draw automatically — check the dashboard says **RR ✅ (≥3)** and the **confluence grade** is A/B.
5. If it says **🚫 RR < 3** or grade **C/D** → it's a no-trade. Wait.

## Honest limitations (read this)

- **No news/fundamentals.** Pine cannot fetch an economic calendar. Check high-impact news yourself (and the skill flags it). Don't take signals into red-folder events.
- **Pivots confirm with a lag.** Market-structure swings confirm `pivotLen` bars after they form — that's standard, not a live promise. Signals fire on the confirming bar close.
- **It does not read intent.** The indicator flags *mechanical* confluence; the Claude skill adds the judgment (is this a clean HTF extreme? is the draw on liquidity real?). Use both together.
- **Sweep + shift ≠ guaranteed.** This raises probability; it does not predict. Risk management (the 0.5–1% / 1:3 rules baked in) is what keeps you in the game.
- **Position size is an estimate.** Pip value for JPY/metals/exotics is broker-dependent — verify before trading live.

*This indicator is analysis and education, not financial advice. Trading carries substantial risk of loss.*

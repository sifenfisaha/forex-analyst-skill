# Forex Analyst Skill — Intraday CRT + Price Action

A professional, institutional-style forex analysis skill for Claude. You paste a chart screenshot (and the pair/timeframe/time); it runs a disciplined top-down workflow and returns a **graded, risk-defined trade plan** — or an honest **NO-TRADE** verdict.

Built for **intraday day-trading**, backbone is **Candle Range Theory (CRT / AMD) + price action**, with **conservative risk (0.5–1% per trade, minimum 1:3 RR)**.

## What it evaluates (every analysis)

1. **Market structure** & HTF bias (BOS / CHoCH / MSS, premium/discount)
2. **Liquidity** & PD arrays (sweeps, inducement, FVG, order blocks)
3. **CRT / AMD** framing (HTF candle as a range, manipulation → distribution)
4. **Trend strength** (displacement vs weakness, structure-shift confirmation)
5. **Session timing** (London KZ, NY AM KZ, Judas swing, day-of-week)
6. **News impact** (red-folder events, DXY/correlations, news guardrail)
7. **Confluence scorecard** (a hard gate — no grade ≥ B = no trade)
8. **Risk & the plan** (position sizing, RR, invalidation, management)

## Install

### From the GitHub repo (recommended)

```bash
npx skills add sifenfisaha/forex-analyst-skill --skill forex-analyst
```

Claude Code-targeted install:

```bash
npx skills add sifenfisaha/forex-analyst-skill --skill forex-analyst --agent claude --yes
```

Full GitHub URL form:

```bash
npx skills add https://github.com/sifenfisaha/forex-analyst-skill --skill forex-analyst
```

Or install directly from the skill path:

```bash
npx skills add https://github.com/sifenfisaha/forex-analyst-skill/tree/main/forex-analyst
```

For local testing:

```bash
mkdir -p ~/.claude/skills
cp -R forex-analyst ~/.claude/skills/forex-analyst
```

> The [`skills` CLI](https://skills.sh) installs into the agent's skills folder — `~/.claude/skills/` for Claude (`--agent claude`), `~/.codex/skills/` for Codex (`--agent codex`). Use `--global`/user-level (default) or run inside a project for a project-level `.claude/skills/` install.

### Manual install (no npx)

```bash
# user-level (every project) — clone then copy the skill folder up
git clone https://github.com/sifenfisaha/forex-analyst-skill.git
mkdir -p ~/.claude/skills
cp -R forex-analyst-skill/forex-analyst ~/.claude/skills/forex-analyst
```

Or grab the ZIP from the green **Code** button on GitHub, unzip, and copy the inner `forex-analyst/` folder into `~/.claude/skills/`.

### Prerequisites
- **Claude Code** (CLI, desktop, or IDE extension) — or any agent that reads `SKILL.md` skills.
- **Python 3** — only for the `position_size.py` calculator (`python3 --version` to check).
- **Node.js / npx** — for the `npx skills add` method (optional; manual install needs only git).

### Verify the install

The folder must contain `SKILL.md` directly inside it:

```bash
ls ~/.claude/skills/forex-analyst/SKILL.md   # should print the path, not "No such file"
```

Then in Claude, run `/skills` (or just paste a chart and ask for a trade plan). Claude reads the `name`/`description` frontmatter in `SKILL.md` and auto-triggers the skill when you paste a chart or ask for a setup, bias, grade, or sizing.

## TradingView indicator (live on your chart)

A companion **Pine Script v5 indicator** lives in [`tradingview/`](tradingview/) — it draws the skill's framework directly on a TradingView chart: BOS/CHoCH, the CRT range, sweeps, liquidity (PDH/PDL + Asian range), FVGs, premium/discount, killzone shading, auto trade levels with RR + position size, a confluence dashboard, and alerts.

**Install:** open TradingView → Pine Editor → paste [`tradingview/forex-analyst.pine`](tradingview/forex-analyst.pine) → Add to chart. Full guide in [`tradingview/README.md`](tradingview/README.md).

It's the *eyes*; the Claude skill is the *analyst* — use them together. Open source, no password gate, no expiry.

## Usage Guide

Once installed, just talk to Claude naturally — the skill auto-triggers when you paste a chart or ask for a trade plan, setup grade, bias, or sizing.

### 1. What to give the skill (every time)

For a proper read, include the three essentials. The skill will ask if any are missing rather than guess:

| Give it | Example |
|---|---|
| **Pair / instrument** | EURUSD, GBPJPY, XAUUSD (gold) |
| **Timeframe(s)** shown | "D1 for bias + M15 for entry" |
| **Current time / session** | "London KZ now", "8:40 AM ET", or just "live now" |

**Best results:** paste **two screenshots** — a higher timeframe (D1/H4) for bias and a lower one (M15/M5) for the entry trigger. The skill does top-down analysis, so it wants both the map and the street view.

### 2. The kinds of things you can ask

| You want… | Say something like |
|---|---|
| **Full trade plan** | *"EURUSD, D1 + M15, London KZ now — trade plan?"* (attach charts) |
| **Just a bias** | *"What's the H4 bias on gold here?"* (attach) |
| **Grade a setup** | *"Grade this setup."* (attach) → returns A+/B/C/D + scorecard |
| **A directional idea** | *"GBPUSD swept the Asian high — is there a short?"* |
| **Size a position** | *"USDJPY long, entry 150.20, stop 150.00, TP 150.80 — size it on a $10k account."* |
| **Check timing** | *"Is now a good session to trade GBPUSD?"* |
| **News check** | *"Anything on the calendar before I take EURUSD long?"* |
| **Sanity check yourself** | *"I want to revenge-trade after 2 losses — talk me out of it."* |

### 3. What you get back

The skill always ends with **one** of two verdicts (never a vague "could go either way"):

- ✅ **A trade plan** — direction, grade, entry, stop, TP1/TP2, RR, position size, session window, news flag, invalidation, and a management plan. Actionable in ~20 seconds.
- 🚫 **A NO-TRADE verdict** — the single most important reason it fails, exactly what would make it tradeable, and what level/time to set an alert on.

Expect "No trade" **often** — that's the skill working, not failing. It only greenlights setups that clear all four non-negotiable gates *and* score ≥ B.

### 4. A typical session flow

1. **Pre-market:** *"Mark the key levels on EURUSD for today."* → PDH/PDL, Asian range, bias.
2. **Killzone opens:** paste the M15, *"London KZ now — anything forming?"*
3. **Setup appears:** *"Grade this."* → if A+/B, you get the full plan.
4. **Before entry:** run `position_size.py` (the skill does the math, or you run it) to get exact lots.
5. **After the trade:** log it in `assets/trade-journal-template.csv` (win *or* loss).
6. **Weekend:** *"Review my journal"* → expectancy, follow-the-plan %, what's working.

### 5. Position-size calculator (standalone)

You can run it directly without the chat:

```bash
python3 scripts/position_size.py -a 10000 -r 1 -p EURUSD -e 1.0850 -s 1.0830 -t 1.0910
# or run with no flags for interactive prompts
```

It prints lot size + RR and **rejects** anything over 1% risk or under 1:3 RR.

### 6. Tips for getting the most out of it

- **Be honest about the session/time** — timing is half the edge; the skill weighs killzones heavily.
- **Don't argue it into a trade.** If it says C-grade, the disciplined move is to wait. Ask *"what would make this an A+?"* instead.
- **Log every trade.** The journal is where your real edge shows up after 30–50 trades — the skill can only analyze what you feed it back.
- **Trust the daily stop.** After 2 losses / −3%, it will tell you to stop. That rule protects more accounts than any entry signal.

## Structure

```
forex-analyst-skill/               # the repo
├── README.md                          # this file
├── LICENSE
├── .gitignore
├── tradingview/                       # live TradingView indicator (Pine v5)
│   ├── forex-analyst.pine             # paste into TradingView Pine Editor
│   └── README.md                      # install + how to read it
└── forex-analyst/                     # the skill (installs to ~/.claude/skills/forex-analyst)
    ├── SKILL.md                       # master workflow + hard rules (the orchestrator)
    ├── references/
    │   ├── 01-crt-playbook.md         # Candle Range Theory: AMD, 3-candle model, entries, Quarterly Theory
    │   ├── 02-market-structure.md     # BOS/CHoCH/MSS, swings, premium-discount, trend strength
    │   ├── 03-liquidity-pd-arrays.md  # liquidity, sweeps, inducement, FVG, order blocks, breakers
    │   ├── 04-sessions-killzones.md   # session/killzone times (ET), Judas swing, day-of-week
    │   ├── 05-risk-management.md      # sizing, 1:3 RR, daily-loss guardrails, prop rules, expectancy
    │   ├── 06-news-fundamentals.md    # red-folder events, news guardrail, DXY & correlations
    │   ├── 07-confluence-scorecard.md # the grading rubric that gates every trade
    │   ├── 08-trade-plan-template.md  # the exact output format
    │   └── 09-psychology-journaling.md# discipline, tilt control, journaling routine
    ├── scripts/
    │   └── position_size.py           # lot-size + RR calculator with rule enforcement
    └── assets/
        └── trade-journal-template.csv # log every trade — the only way to find your edge
```

## Position-size calculator

```bash
python3 forex-analyst/scripts/position_size.py -a 10000 -r 1 -p EURUSD -e 1.0850 -s 1.0830 -t 1.0910
# or run with no flags for interactive prompts
# (once installed, the path is ~/.claude/skills/forex-analyst/scripts/position_size.py)
```
It prints lot size + RR and **flags any violation** of the 1% max risk / 1:3 RR rules.

## The philosophy

> **Be a risk manager who happens to use CRT — not a CRT trader who hopes risk works out.**

The skill is deliberately strict. It will tell you "No trade" often, refuse setups under 1:3, and enforce a daily stop after 2 losses. That discipline — plus journaling every trade — is what actually compounds an account. Quality over quantity.

## License

[MIT](LICENSE) © 2026 Sifen Fisaha. Free to use, modify, and share — just keep the copyright notice. No warranty.

## Important disclaimer

This skill provides **trading analysis and education, not financial advice**. Forex/CFD trading carries substantial risk of loss. No method guarantees profit; the skill manages probability and risk, it does not predict the future. You are solely responsible for your trading decisions. Pip values for metals/JPY/exotic pairs are broker-dependent — confirm against your broker's contract specs before trading live.

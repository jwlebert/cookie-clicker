# Cookie Clicker Scripts

A collection of automation tools and utility scripts for [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) (macOS / Steam).

# Available Scripts

## Endless Cycle Bot (`scripts/endless-cycle.py`)

Automates the 1,000 ascensions required for the **Endless Cycle** shadow achievement in Cookie Clicker.

The script runs a continuous ~29-second loop that buys starter upgrades and Cursors, scrolls to purchase high-tier producers (*Fractal Engine*, *You*), buys all upgrades to reach the +1 Prestige threshold, triggers **Legacy**, and clicks **Reincarnate** to repeat.

### Estimated Completion Time

| Milestone / Achievement | Ascensions | Estimated Time |
|---|---|---|
| **Average Cycle** | 1 | ~28.9s |
| **Reincarnation** | 100 | ~48m 11s |
| **Endless Cycle** | 1,000 | ~8h 01m 54s |

### Key Features

- **8-Step Automated Pipeline**: Handles building purchases, scrolling, upgrades, legacy ascension, and reincarnation in one continuous loop.
- **Coordinate-Based Targeting**: Uses direct pixel coordinates for fast and reliable navigation without template matching latency.
- **Performance & Timing Tracker**: Automatically tracks cycle duration and prints performance summaries on demand.
- **Process Guardrails**: Executes clicks only when Cookie Clicker is active and focused (via macOS `osascript`).
- **Hotkey & Failsafe Controls**:
  - <kbd>q</kbd> — Pause / resume.
  - <kbd>t</kbd> — Print cycle timings & performance summary.
  - <kbd>l</kbd> — Print current mouse position (for coordinate recalibration).
  - <kbd>Esc</kbd> — Exit immediately.
  - Moving the mouse to any corner triggers the PyAutoGUI failsafe stop.

### Demo & Setup

https://github.com/user-attachments/assets/d236d932-b7ab-41ad-b4ab-9d59960a2b3d

> [!NOTE]
> Coordinates are calibrated for fullscreen macOS. Press <kbd>l</kbd> while running to log cursor coordinates if recalibration is needed.
> 
> Ascension speed and purchase timing depend on your Prestige level and chosen permanent upgrades.
> - **Tested Prestige**: ~52 trillion
> - **Permanent Upgrades**: Kitten strategists, Fortune #103, Kitten Admins, United Workforce, Omelette
> - **macOS Permissions**: Ensure your terminal has **Accessibility** permissions enabled in *System Settings > Privacy & Security*.

### How to Run

Run directly with [`uv`](https://github.com/astral-sh/uv) (dependencies are declared via PEP 723 inline script metadata):

```bash
uv run scripts/endless-cycle.py
```

1. Focus the Cookie Clicker window.
2. Press <kbd>q</kbd> to start or pause the loop (<kbd>t</kbd> for timing stats, <kbd>Esc</kbd> to quit).

# Repository Structure

```text
cookie-clicker/
├── scripts/             # Automation scripts
│   └── endless-cycle.py # Endless Cycle shadow achievement bot
├── pyproject.toml
└── README.md
```

# Future Additions

More helper scripts and automation tools for other achievements, minigames (Stock Market, Garden), or combo setups may be added here over time.

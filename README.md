# Cookie Clicker Scripts

A collection of automation tools and utility scripts for [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) (macOS / Steam).

# Available Scripts

## Endless Cycle Bot (`scripts/endless-cycle.py`)

Automates the 1,000 ascensions required for the **Endless Cycle** shadow achievement in Cookie Clicker.

The script runs a continuous ~1-minute loop that buys starter upgrades and Cursors, scrolls to purchase high-tier producers (*Prism*, *Fractal Engine*, *You*), buys all upgrades to reach the +1 Prestige threshold, triggers **Legacy**, and clicks **Reincarnate** to repeat.

### Key Features

- **10-Step Automated Pipeline**: Handles building purchases, scrolling, upgrades, legacy ascension, and reincarnation in one continuous loop.
- **Vision-Based Matching**: Uses OpenCV and PyAutoGUI to locate buttons reliably across Retina and standard displays.
- **Process Guardrails**: Executes clicks only when Cookie Clicker is active and focused (via macOS `osascript`).
- **Hotkey & Failsafe Controls**:
  - <kbd>q</kbd> — Pause / resume.
  - <kbd>Esc</kbd> — Exit immediately.
  - Moving the mouse to any corner triggers the PyAutoGUI failsafe stop.

### Demo & Setup

https://github.com/user-attachments/assets/d236d932-b7ab-41ad-b4ab-9d59960a2b3d

> [!NOTE]
> Ascension speed and purchase timing depend on your Prestige level and chosen permanent upgrades.
> - **Tested Prestige**: ~52 trillion
> - **Permanent Upgrades**: Kitten strategists, Fortune #103, Kitten Admins, United Workforce, Omelette
> - **macOS Permissions**: Ensure your terminal has **Accessibility** and **Screen Recording** permissions enabled in *System Settings > Privacy & Security*.

### How to Run

Run directly with [`uv`](https://github.com/astral-sh/uv) (dependencies are declared via PEP 723 inline script metadata):

```bash
uv run scripts/endless-cycle.py
```

1. Focus the Cookie Clicker window.
2. Press <kbd>q</kbd> to start or pause the loop (<kbd>Esc</kbd> to quit).

# Repository Structure

```text
cookie-clicker/
├── assets/              # UI image templates for OpenCV/PyAutoGUI matching
├── scripts/             # Automation scripts
│   └── endless-cycle.py # Endless Cycle shadow achievement bot
├── pyproject.toml
└── README.md
```

# Future Additions

More helper scripts and automation tools for other achievements, minigames (Stock Market, Garden), or combo setups may be added here over time.

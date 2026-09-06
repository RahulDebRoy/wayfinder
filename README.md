# Wayfinder

A tiered goal and habit tracker with an energy-aware daily planner, built as a
single-file web app.

## What's in this repo

| File | Purpose |
|---|---|
| `wayfinder.html` | The app itself — open it in a browser to run it. |
| `wayfinder_bridge.py` | Optional local bridge server that lets the app sync its data to a JSON file on your disk. |
| `start_wayfinder_bridge.bat` | Double-click to manually start the bridge (Windows). |
| `start_wayfinder_bridge_silent.vbs` | Silent launcher for auto-starting the bridge at login. |

## Features

- Goals grouped into Primary / Secondary / Tertiary priority tiers
- Framework-based progress tracking (steps, milestones, completion)
- A day-timeline view of wake/sleep, meals, fixed commitments, and energy windows
- Automatic conflict detection (overlaps, meal buffers, sleep buffer, working hours)
- Fatigue-aware time-slot suggestions for new tasks
- Add / edit / delete goals
- Optional local sync bridge to back up data to a file on disk

## Running it

Open `wayfinder.html` directly in any modern browser. No build step, no
dependencies.

> **Note on data persistence:** the built-in auto-save uses a storage API
> that's only available when this file is run inside a Claude.ai artifact.
> If you're running it as a plain HTML file (e.g. from this repo or GitHub
> Pages), data won't persist between visits unless the storage layer is
> swapped for `localStorage` or connected to the bridge script below.

## Optional: local sync bridge

`wayfinder_bridge.py` is a small local server that lets the app save/load a
JSON file on your own machine, so your data survives independent of the
browser. See the in-app "Sync" button and the comments at the top of
`wayfinder_bridge.py` for setup details.

## License

Personal project — add a license here if you plan to share or open this up
for others to use or modify.

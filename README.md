# ISM2411 — Python for Business

**Name:** Leonardo Leon

**Semester:** Fall 2026

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week05/` — Conditionals: tiered discount calculator
- `week06/` — Loops: sales report with sum, average, max
- `week07/` — Functions: calculate_tax, apply_discount, final_price
- `week08/` — Git: first GitHub submission (this repo, its `.gitignore`, and README)

## How to Run

Each script is standalone. Open a terminal and run:
```
python week07/functions.py
```

## Reflection

**1. Commit history**

```
d88dac4 list week05 and week06 in README
dcd05e4 add module 5 discount calculator and module 6 sales loop
4693d43 add README with module listing and run instructions
ce0f367 add module 7 functions: calculate_tax, apply_discount, final_price
db00d2f add .gitignore for Python and OS files
9bad9ff Initial commit
```

If I were hiring someone and saw this history, it would tell me they work in small steps and finish one thing before starting the next. Each message says what changed, so you can understand the project without opening the files. The .gitignore comes first, which shows they set the project up before adding code instead of cleaning up later.

**2. How Git changes the way I edit a working script**

Before this module, if I wanted to change a script that already worked, I would edit it directly or make a copy like `module01_lab copy.txt` just in case. Now I would commit the working version first, so if my edit breaks something I can see exactly what changed and go back. I would also try to keep each commit to one change, so it is easy to find where a bug came in.

**3. Something I would add to my .gitignore**

I would add `* copy.*`, because on my Mac, Finder names duplicated files things like `module01_lab copy.txt`, and I had one of those sitting in my old folder. Those are just backups I made by hand, and they shouldn't be tracked because Git already keeps every version for me. Tracking them would only add clutter and make it unclear which file is the real one.

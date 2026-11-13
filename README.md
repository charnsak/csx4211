# CSX4211 Data Engineering — Labs

Assumption University · Vincent Mary School of Engineering, Science and Technology · Semester 2/2026

This repository holds the weekly labs. Everything runs in **GitHub Codespaces**: a cloud computer with Python, Git, Docker and Java already installed. Your laptop only needs a modern web browser.

## Start here (Week 1)

1. Sign in to GitHub (a free personal account is fine).
2. On this repository page, click **Code → Codespaces → Create codespace on main**.
3. The first start takes a few minutes. When the editor opens, follow `labs/week01/README.md`.

## Every Saturday

Reopen your codespace from https://github.com/codespaces (do not create a new one each week), then run this in the terminal:

```bash
git pull
```

This downloads the lab folder for the new week. Open `labs/weekNN/README.md` and start.

## What lives where

| Path | What is inside |
|---|---|
| `labs/week01/`, `labs/week02/`, … | One folder per week. A new folder appears each Saturday. |
| `.devcontainer/` | The recipe that builds your codespace. Please do not edit it. |
| `requirements.txt` | Python packages installed when the codespace is created. |

## Rules of thumb

- **Your codespace is your lab notebook.** Lab answers go into the weekly Google Form, so you never have to push lab code. (If you do commit, GitHub offers to create a fork of this repository for you.)
- **Stop your codespace when you finish** (https://github.com/codespaces → **…** → **Stop codespace**). Free personal accounts include 120 core-hours (about 60 hours on the default 2-core machine) and 15 GB-month of storage each month. A codespace stops by itself after 30 minutes without activity and is deleted after 30 days without use.
- **Never commit secrets**: passwords, API keys, or Google Cloud key files.


# Lab 0 (Week 1): Your data engineering workbench

**Saturday 14 November 2026  every student sets up their own codespace.**

By the end of this lab you will have:

1. a cloud development environment that you will use all semester (GitHub Codespaces),
2. run your first end-to-end data pipeline and traced it through the data engineering lifecycle, and

Answer the **Week 1 lab check** in MS Teams. It closes on **Monday 16 November at 23:59**. Several answers come from running the code, so do the steps instead of guessing.

---

## Part A: Your lab computer in the cloud (about 25 minutes)

### A1. GitHub account

Sign in at https://github.com, or create a free personal account. Choose a username you would be happy to show an employer.

> **Recommended:** apply for the free **GitHub Student Developer Pack** at https://education.github.com/pack using your `@au.edu` email. It upgrades you to GitHub Pro, which raises your monthly Codespaces allowance from 120 to 180 core-hours and from 15 to 20 GB-month of storage. Approval can take a few days, so apply today.

### A2. Create your codespace

1. Open the course repository .
2. Click **Code → Codespaces → Create codespace on main**. If you are asked for a machine type, choose **2-core**.
3. The first start takes a few minutes because it installs Python, Docker and Java. When it finishes you see VS Code in your browser with this file open.

### A3. Terminal warm-up

Open a terminal (**Ctrl+`**, or menu **☰ → Terminal → New Terminal**) and try:

```bash
pwd                     # where am I?
ls labs/week01          # what is in this folder?
git log --oneline -3    # the last three changes to the course repository
```

### A4. Check your tools

```bash
python labs/week01/check_env.py
```

Every line should say `PASS`. If only `docker` fails, wait one minute and run the script again, because Docker starts in the background. If anything else fails, ask a lab captain.

### A5. Look after your free quota

- Check how much of your free quota is left at https://github.com/settings/billing.
- When you finish today, stop the codespace: https://github.com/codespaces → **…** next to your codespace → **Stop codespace**.
- Next Saturday, reopen **the same codespace** from https://github.com/codespaces and run `git pull`. Do not create a new codespace each week.

---

## Part B: Hello, pipeline (about 40 minutes)

### B1. Run the pipeline

```bash
python labs/week01/hello_pipeline.py
```

You should see four steps, `[extract]`, `[load]`, `[transform]` and `[serve]`, and a table of New York City boroughs. The data is the official taxi zone lookup table published by the NYC Taxi & Limousine Commission (TLC).

### B2. Read the code and map it to the lifecycle

Open `labs/week01/hello_pipeline.py`. With your partner, copy this table into your notes and fill it in:

| Lifecycle stage | Where does it happen? (function or line) | What could go wrong here in a real company? |
|---|---|---|
| Generation | | |
| Ingestion | | |
| Storage | | |
| Transformation | | |
| Serving | | |

Example for the last column: *"Ingestion: the source URL changes, and the 3 a.m. download fails."*

### B3. Ask your own questions with SQL

`query.py` runs SQL against the database that the pipeline just built:

```bash
python labs/week01/query.py "SELECT * FROM taxi_zones LIMIT 5"
python labs/week01/query.py "DESCRIBE taxi_zones"
```

Run `python labs/week01/query.py` with no query to get an interactive `sql>` prompt.

Write one query for each question. You need the answers for the lab check.

1. How many rows are in `taxi_zones`? Now run `wc -l labs/week01/data/raw/taxi_zone_lookup.csv`. Why do the two numbers differ by one?
2. Look at the transform output again. Which borough has the most zones? Is there only one correct answer?
3. How many zones have `service_zone = 'Yellow Zone'`?
4. Is `Zone` a unique key? Find the zone names that appear more than once. *(Hint: `GROUP BY Zone HAVING count(*) > 1`)*
5. What is in the last two rows (`LocationID` 264 and 265)? Should they appear in a report about boroughs?
---
## Before you leave

- [ ] Answer the Week 1 lab check (MS Teams Assignment). It closes Monday 16 November, 23:59.
- [ ] Stop your codespace.
- [ ] Read for Week 2: *Fundamentals of Data Engineering* (Reis & Housley), chapters 1 and 2.

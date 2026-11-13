# Lab 0 (Week 1): Your data engineering workbench

**Saturday 7 November 2026 · 10:05–11:35 · Sit in pairs and help each other, but every student sets up their own codespace.**

By the end of this lab you will have:

1. a cloud development environment that you will use all semester (GitHub Codespaces),
2. run your first end-to-end data pipeline and traced it through the data engineering lifecycle, and
3. redeemed your Google Cloud credits and protected them with a budget alert.

At 11:35 you answer the **Week 1 lab check** (Google Form, linked on Google Classroom). It closes on **Monday 9 November at 23:59**. Several answers come from running the code, so do the steps instead of guessing.

---

## Part A: Your lab computer in the cloud (about 25 minutes)

### A1. GitHub account

Sign in at https://github.com, or create a free personal account. Choose a username you would be happy to show an employer.

> **Recommended:** apply for the free **GitHub Student Developer Pack** at https://education.github.com/pack using your `@au.edu` email. It upgrades you to GitHub Pro, which raises your monthly Codespaces allowance from 120 to 180 core-hours and from 15 to 20 GB-month of storage. Approval can take a few days, so apply today.

### A2. Create your codespace

1. Open the course repository (link on Google Classroom).
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

### B4. Challenge (optional)

Add a second report to the pipeline, `data/output/zones_per_service_zone.csv`, that counts zones per `service_zone`. Change only `transform()` and `serve()`, then run the pipeline again.

---

## Part C: Google Cloud credits and a budget alert (about 25 minutes)

We use Google Cloud from Week 10. We set it up today so that problems show up early, and so that cost control is a habit from day one.

> **Coupon link not posted yet?** If the instructor has not posted the student coupon link on Google Classroom, skip Part C today and do it as soon as the link appears, at the latest before the Week 3 class.

### C1. Request your coupon

1. Open the **student coupon link** on Google Classroom.
2. Enter your name and your `@au.edu` email address, then confirm the verification email.
3. A second email arrives with your **coupon code**, worth up to US$50. Each student can request one coupon.

### C2. Redeem the coupon

1. In the coupon email, click **Redeem now** and sign in with the Google Account you will use for this course. If your `@au.edu` account cannot open https://console.cloud.google.com, use a personal Gmail account instead.
2. Check the coupon code, read the terms, and click **Accept and continue**. The credit appears in a new Cloud Billing account named after the course.

> **Never enter a credit card.** Education credits do not need one. If a page asks for card details, you are in the Free Trial sign-up, not on the credits page. Stop and ask for help.

### C3. Create your course project

1. In the console, open the project picker in the top bar and click **New project**.
2. Project name: `csx4211-<your student ID>`.
3. Billing account: choose the education billing account from C2, then click **Create**.

### C4. Create a budget alert

Open **Billing → Budgets & alerts → Create budget** and use these settings:

| Setting | Value |
|---|---|
| Name | `csx4211-budget` |
| Time range | **Custom range**, from 7 Nov 2026 to 31 Mar 2027 |
| Projects | All projects |
| Savings | **Untick all savings** (credits and discounts), so the budget tracks your usage *before* the education credits are applied |
| Budget type and amount | Specified amount, **50** (USD) |
| Threshold rules | 50%, 90% and 100% of *Actual* spend (the defaults) |
| Notifications | Keep **Email alerts to billing admins and users** ticked |

Click **Finish**. Remember two things:

- A budget **only sends emails. It does not stop anything.** A cluster you forget to delete keeps costing money after the 100% email.
- If you leave the savings ticked, the credits cancel out your costs, the budget sees almost $0, and you get **no warning** until the credits are gone.

Coupons can be redeemed until **27 February 2027** (16 weeks after the course starts), and the credits last about a year, which is more than enough for this course.

---

## Before you leave

- [ ] Answer the Week 1 lab check (Google Classroom). It closes Monday 9 November, 23:59.
- [ ] Stop your codespace.
- [ ] Read for Week 2: *Fundamentals of Data Engineering* (Reis & Housley), chapters 1 and 2.

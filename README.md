# VEXORA website

A responsive one-page agency website built with Python Flask, HTML, CSS, and JavaScript.

## Run it on your computer

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (optional but recommended):
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the site: `python app.py`
6. Open `http://127.0.0.1:5000`

## Before publishing

Replace the sample brand text or service descriptions if needed. Add your real business email, social links, portfolio examples, and pricing only when you have confirmed details. Do not claim client work or testimonials that you do not have.

### Connect the contact form

The form sends email only after SMTP environment variables are configured on your host:

- `SECRET_KEY`: a long random secret
- `SMTP_HOST`: your email provider's SMTP host
- `SMTP_PORT`: usually `587`
- `SMTP_USER`: SMTP login / sender email
- `SMTP_PASSWORD`: SMTP app password (never put it in the source code)
- `CONTACT_INBOX`: email address where enquiries should arrive

If these are not configured, the form displays a message that it is not connected yet.

## Put it online with Render

1. Create a GitHub account and a Render account.
2. Create a new GitHub repository and upload the contents of this folder.
3. In Render, choose **New > Web Service**, connect the repository, and select Python.
4. Set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Add the environment variables listed above in Render's Environment settings.
6. Deploy. Render will give you a public `onrender.com` address.

The exact dashboard labels may change. Check Render's current Flask deployment guide if the interface differs.

## Get it on Google

A website being online does not automatically mean it appears in Google Search.

1. Make sure the deployed website is public and works on its own URL.
2. For a professional address, buy a domain (for example, `vexora.com` if available) from a domain registrar and connect it to Render using Render's domain instructions.
3. Add the domain in Google Search Console and verify ownership. A DNS TXT record is a common verification method.
4. Create a sitemap at `https://YOUR-DOMAIN/sitemap.xml` and submit it in Search Console. For this starter site, you can initially use the homepage URL inspection tool to request indexing; add a proper sitemap before expanding the site.
5. Make sure the page title and description are specific to your actual services and location. Add real project examples, useful service pages, and accurate contact details.
6. Keep the site fast, mobile-friendly, secure with HTTPS, and free of broken links.
7. Wait. Google decides when and whether to index pages; requesting indexing is not an instant guarantee or a paid placement.

Useful official resources:
- Google Search Console: https://search.google.com/search-console
- Google Search Central: https://developers.google.com/search/docs
- Render Flask deployment: https://render.com/docs/deploy-flask

## Important business note

This is a starter website template, not a registered business or a guarantee of customers. Before taking paid client projects, agree on scope, price, revisions, ownership, hosting, maintenance, and delivery dates in writing. If you are under 18, involve a parent or trusted adult for contracts, payments, and account setup.

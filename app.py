import os
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-before-deploying")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    service = request.form.get("service", "").strip()
    message = request.form.get("message", "").strip()

    if not all([name, email, message]):
        flash("Please fill in your name, email, and project details.", "error")
        return redirect(url_for("home") + "#contact")

    # Email delivery is enabled when SMTP settings are added to your hosting environment.
    smtp_host = os.environ.get("SMTP_HOST")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ.get("SMTP_USER")
    smtp_password = os.environ.get("SMTP_PASSWORD")
    inbox = os.environ.get("CONTACT_INBOX")

    if all([smtp_host, smtp_user, smtp_password, inbox]):
        msg = EmailMessage()
        msg["Subject"] = f"New VEXORA enquiry: {service or 'Website project'}"
        msg["From"] = smtp_user
        msg["To"] = inbox
        msg["Reply-To"] = email
        msg.set_content(
            f"Name: {name}\nEmail: {email}\nService: {service}\n\nProject details:\n{message}"
        )
        try:
            with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.send_message(msg)
            flash("Thanks! Your enquiry has been sent. We'll be in touch.", "success")
        except Exception:
            app.logger.exception("Unable to send contact enquiry")
            flash("Your message could not be sent right now. Please email us directly.", "error")
    else:
        flash("The contact form is not connected yet. Add your email settings before launch.", "error")

    return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)

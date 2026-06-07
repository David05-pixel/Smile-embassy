```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# ABOUT PAGE
# ==========================================

@app.route("/about")
def about():
    return render_template("about.html")


# ==========================================
# SERVICES PAGE
# ==========================================

@app.route("/services")
def services():
    return render_template("services.html")


# ==========================================
# SERVICE PAGES
# ==========================================

@app.route("/whitening")
def whitening():
    return render_template("whitening.html")


@app.route("/braces")
def braces():
    return render_template("braces.html")


@app.route("/implants")
def implants():
    return render_template("implants.html")


@app.route("/extraction")
def extraction():
    return render_template("extraction.html")


@app.route("/family-dentistry")
def family_dentistry():
    return render_template("family-dentistry.html")


# ==========================================
# BLOG
# ==========================================

@app.route("/blog")
def blog():
    return render_template("blog.html")


# ==========================================
# CONTACT PAGE
# ==========================================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==========================================
# APPOINTMENT PAGE
# ==========================================

@app.route("/appointment")
def appointment():
    return render_template("appointment.html")


# ==========================================
# BOOKING FORM
# ==========================================

@app.route("/book", methods=["POST"])
def book():

    fullname = request.form.get("fullname")
    phone = request.form.get("phone")
    email = request.form.get("email")
    service = request.form.get("service")
    appointment_date = request.form.get("appointment_date")
    appointment_time = request.form.get("appointment_time")
    first_visit = request.form.get("first_visit")
    notes = request.form.get("notes")

    print("===================================")
    print("NEW APPOINTMENT REQUEST")
    print("===================================")
    print("Name:", fullname)
    print("Phone:", phone)
    print("Email:", email)
    print("Service:", service)
    print("Date:", appointment_date)
    print("Time:", appointment_time)
    print("First Visit:", first_visit)
    print("Notes:", notes)
    print("===================================")

    return redirect(url_for("thank_you"))


# ==========================================
# THANK YOU PAGE
# ==========================================

@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")


# ==========================================
# TESTIMONIALS PAGE
# ==========================================

@app.route("/testimonials")
def testimonials():
    return render_template("testimonials.html")


# ==========================================
# PRIVACY POLICY
# ==========================================

@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy-policy.html")


# ==========================================
# TERMS OF SERVICE
# ==========================================

@app.route("/terms")
def terms():
    return render_template("terms.html")


# ==========================================
# CUSTOM ERROR PAGE
# ==========================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
```

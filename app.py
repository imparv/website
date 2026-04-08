from flask import Flask, render_template,url_for,request,redirect, flash
import json


from flask_mail import Mail

app = Flask(__name__)


app.secret_key='its-secret-key'
with open('userdata.json',"r",encoding='utf-8') as u:
    params = json.load(u)["params"]

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['mail-user'],
    MAIL_PASSWORD=params['mail-pass']
)
mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html",params=params)

@app.route("/post")
def post():
    return render_template("single-standard.html",params=params)

@app.route("/blog")
def blog():
    return render_template("blog.html",params=params)

@app.route("/about")
def about():
    return render_template("about.html",params=params)



@app.route("/contact", methods=['GET', 'POST'])
def contact():
    try:
        if request.method == 'POST':
            name = request.form.get('name')
            subject = request.form.get('subject')
            email = request.form.get('email')
            message = request.form.get('message')

            # Basic validation
            if not name or not email or not message:
                flash("Please fill all required fields")
                return redirect("/contact")

            mail.send_message(
                subject='Query from ' + name,
                sender=email,
                recipients=["iamparv.r@gmail.com"],
                body=f"{subject}\n\n{message}\n\nFrom: {email}"
            )

            flash("Message sent successfully!")
            return redirect("/contact")

        # GET request
        return render_template("contact.html",params=params)

    except Exception as e:
        print(e)
        return "Something went wrong", 500
@app.route("/journey")
def journey():
    return render_template("journey.html",params=params)

@app.route("/projects")
def project():
    return render_template("projects.html",params=params)

@app.route("/services")
def services():
    return render_template("services.html",params=params)

@app.route("/testimonials")
def testimonials():
    return render_template("testimonials.html",params=params)



if __name__ == "__main__":
    app.run(debug=True)

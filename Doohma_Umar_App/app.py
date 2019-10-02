from email.mime.image import MIMEImage

from flask import Flask, render_template, request
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
app.config['SECRET_KEY'] = '<---YOUR_SECRET_FORM_KEY--->'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ad = request.form['ad']
        adspend = request.form['adspend']
        noad = request.form['noad']
        visualad = request.form['visualad']
        comment = request.form['comment']
        pay = request.form['pay']
        duration = request.form['duration']
        name = request.form['name']
        email = request.form['email']
        businessstype = request.form['businesstype']
        telephone = request.form['telephone']
        website = request.form['website']
        files = request.files.getlist("image")

        # Set up users for email
        gmail_user = "pigeonera@gmail.com"
        gmail_pwd = "Doohma@61064"
        recipients = ["ugukmail@gmail.com"]

        # send it
        mail(gmail_user, gmail_pwd, recipients, "Subject Here", ad+" "+adspend+" "+noad+" "+visualad+" "+comment+" "+pay+" "+duration+" "+name+" "+email+" "+businessstype+" "+telephone+" "+website, files)

    return render_template('sendEmail.html')


# Create Module
def mail(gmail_user, gmail_pwd, to, subject, text, files):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = ", ".join(to)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    # get all the attachments
    for file in files:
        img_data = file.read()
        image = MIMEImage(img_data, name=os.path.basename(file.filename))
        msg.attach(image)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()


if __name__ == '__main__':
    app.run()

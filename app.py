import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, FileField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename


def send_email(subject, body, to_email, from_email, from_email_password, cc, files=None):
    # Create the root message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg['Cc'] = cc

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach files
    if files:
        for file in files:
            attachment = MIMEBase('application', 'octet-stream')
            try:
                with open(file, 'rb') as f:
                    attachment.set_payload(f.read())
                encoders.encode_base64(attachment)
                attachment.add_header(
                    'Content-Disposition', f'attachment; filename={os.path.basename(file)}')
                msg.attach(attachment)
            except Exception as e:
                print(f"Could not attach file {file}: {e}")
                flash_msg = e

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_email_password)

    # Send the email
    try:
        server.sendmail(from_email, to_email, msg.as_string())
        print('Email sent successfully!')
        flash_msg = "Email sent successfully"
    except Exception as e:
        print(f"Failed to send email: {e}")
        flash_msg = "Failed to send mail."
    finally:
        server.quit()
        return flash_msg


subject = 'Python (Selenium) Assignment - Susmit Kumar Pandey'
to_email = 'tech@themedius.ai'
from_email = 'susmitpandey22@gmail.com'
from_email_password = os.getenv("password")
cc = 'hr@themedius.ai'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ufhskjf83ry98ifsdkjfkj4'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024
bootstrap = Bootstrap5(app)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


class MailForm(FlaskForm):
    source_code = URLField("URL for the source code",
                           validators=[DataRequired()])
    git_link = URLField("URL for the github", validators=[DataRequired()])
    availability = StringField("Confirm your availability")
    ss = FileField("Upload the screenshot")
    resume = FileField("Upload your Resume")
    submit = SubmitField("Send Mail")


@app.route("/", methods=["GET", "POST"])
def home():
    form = MailForm()
    if form.validate_on_submit():
        source_code = form.source_code.data
        git_link = form.git_link.data
        availability = form.availability.data

        # Handle file uploads
        files = []
        ss_file = form.ss.data
        resume_file = form.resume.data

        if ss_file:
            ss_filename = secure_filename(ss_file.filename)
            ss_path = os.path.join(
                app.config['UPLOAD_FOLDER'], ss_filename)
            ss_file.save(ss_path)
            files.append(ss_path)

        if resume_file:
            resume_filename = secure_filename(resume_file.filename)
            res_path = os.path.join(
                app.config['UPLOAD_FOLDER'], resume_filename)
            resume_file.save(res_path)
            files.append(res_path)

        body = f'Approach : Initialise the selenium driver and get the web page of the google form. Get the input boxes using the driver and send the data through send_keys() function. Submit the form and take the screenshot of the page using get_screenshot() method.\n\n Source code:{source_code}\nGithub:{git_link}\n\n{availability}.'
        flash_msg = send_email(subject, body, to_email, from_email,
                               from_email_password, cc, files)
        flash(flash_msg)

        return redirect(url_for('home', flash=flash_msg))
    return render_template('mail.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

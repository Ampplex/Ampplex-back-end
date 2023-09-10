import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail():
    # Email configuration
    sender_email = 'team.amplex@gmail.com'
    receiver_email = 'ankesh3905222@gmail.com'
    subject = 'Test Email'
    message = 'This is a test email sent from Python.'

    # SMTP server settings (for Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # 587 is the default TLS port, use 465 for SSL

    # Your email account credentials (make sure to use an "App Password" or enable less secure apps)
    username = 'team.amplex@gmail.com'
    password = 'iyfmqibihwffqvjnp354'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    # Establish a secure SMTP connection
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        server.login(username, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the SMTP server
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    sendEmail()

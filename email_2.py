import smtplib
from email.message import EmailMessage

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create the email message
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.set_content(body)
        
        # Connect to SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
send_email(
    sender_email="your_email@gmail.com",
    sender_password="your_password",
    recipient_email="recipient@example.com",
    subject="Test Email",
    body="Hello, this is a test email sent from Python using EmailMessage!"
)

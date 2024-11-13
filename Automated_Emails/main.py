import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import schedule

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender = "mercedesmotivational9@gmail.com"
pw = "ylkc xrlz xcwx efwf"
recipient = "youngdirk2005@gmail.com"
subject_base = "Love Letter #"
email_count = 1

nouns = [
    "heart", "smile", "life", "world", "dream", "brain", "mind", "soul", "spirit", "presence"
]

environment_nouns = [
    "world", "earth", "universe", "galaxy", "planet", "atmosphere", "surroundings", "life"
]

verbs = [
    "love", "adore", "cherish", "worship", "treasure", "prize", "esteem", "value", "honor", "respect"
]

adjectives = [
    "lover", "mrs.", "woman", "everything", "queen", "princess", "goddess", "angel", "star", "sunshine"
]

good_adjectives = [
    "fulfilled", "amazing", "wonderful", "fantastic", "incredible", "ever lasting", "fabulous", "symbolic", "perfect", "excellent"
]

phrases = [
    "forever", "in every life", "always", "in every moment", "in every heartbeat", "in every breath", "in every thought", "in every dream", "in every wish", "in every desire"
]

templates = [
    "My {noun} belongs to you, {phrase}.",
    "You are my {adjective}, I {verb} you endlessly.",
    "Every time I think of you, my {noun} fills with {verb}.",
    "With you, life feels {good_adjectives}.",
    "My {noun} belongs to you, {phrase}.",
    "Forever my {adjective} in this {environment_nouns}."
]

gif_urls = [
    "http://localhost:8000/icegif-979.gif",
    "http://localhost:8000/sleep-icegif-12.gif",
    "http://localhost:8000/giphy.gif",
    "http://localhost:8000/hugs-icegif-3.gif",
    "http://localhost:8000/hug-love.gif"
]

def generate_message():
    template = random.choice(templates)
    message = template.format(
        noun=random.choice(nouns),
        environment_nouns=random.choice(environment_nouns),
        verb=random.choice(verbs),
        adjective=random.choice(adjectives),
        good_adjectives=random.choice(good_adjectives),
        phrase=random.choice(phrases)
    )
    return message.capitalize()

def send_email(email_count):
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = f"{subject_base}{email_count}"
    body = generate_message()
    signature = """
    \n\n
    𝓁 𝑜 𝓋 𝑒,
    𝓡 𝓲 𝓴 𝓴 𝓸
    """
    text = body + signature
    gif_url = random.choice(gif_urls)
    html = f"""
    <html>
    <body>
        <p>{body}</p>
        <p style="font-family: cursive;">𝓁 𝑜 𝓋 𝑒,<br>𝓡 𝓲 𝓴 𝓴 𝓸</p>
        <p>Check out my -> <a href="https://github.com/Rvkko">GitHub</a></p>
        <p>Check out my -> <a href="https://www.linkedin.com/in/derriko-herron-jr-bs/">LinkedIn</a></p>
        <p><a href="http://example.com/unsubscribe">Unsubscribe :(</a></p>
        <p><img src="{gif_url}" alt="Love GIF"></p>
    </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, pw)
            server.sendmail(sender, recipient, message.as_string())
            print(f"Email {email_count} sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent at 11:10 PM
# job = schedule.every().day.at("23:10").do(send_email, email_count)

def cancel_scheduled_email():
    # schedule.cancel_job(job)
    print("Scheduled email has been canceled.")

# Keep the script running
# try:
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
# except KeyboardInterrupt:
#     cancel_scheduled_email()

send_email(email_count)
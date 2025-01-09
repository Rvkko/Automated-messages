import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from datetime import datetime, timedelta

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender = "mercedesmotivational9@gmail.com"
pw = "ylkc xrlz xcwx efwf"
recipient = "youngdirk2005@gmail.com"
subject_base = "Motivational Quote # "
email_count = 1

nouns = [
    "courage", "hope", "passion", "dream", "vision", "strength", "determination", "perseverance", "journey", "success"
]

environment_nouns = [
    "adventure", "progress", "world", "realm", "universe", "path", "landscape", "possibility"
]

verbs = [
    "inspire", "empower", "uplift", "motivate", "encourage", "drive", "ignite", "spark", "support", "elevate"
]

adjectives = [
    "hero", "champion", "warrior", "leader", "innovator", "visionary", "trailblazer", "pioneer", "icon", "legend"
]

good_adjectives = [
    "unstoppable", "unbreakable", "remarkable", "extraordinary", "outstanding", "phenomenal", "brilliant", "admirable",
    "magnificent", "exceptional"
]

phrases = [
    "without limits", "to the stars", "with every step", "in every heartbeat", "with every breath", "in every moment",
    "on every journey", "with unyielding spirit", "with every challenge", "with relentless pursuit"
]

templates = [
    "Your {noun} is your strength, {phrase}.",
    "Keep going, {adjective}, you {verb} the world.",
    "Every challenge you face builds your {noun}.",
    "With a mindset like yours, life is {good_adjective}.",
    "Your {noun} is the key to your success, {phrase}.",
    "You are a {adjective} in this {environment_noun}, never forget your potential."
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
    𝓇 𝑒 𝑔 𝒶 𝓇 𝒹 𝓈,
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
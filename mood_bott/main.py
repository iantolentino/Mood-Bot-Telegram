import requests

BOT_TOKEN = "8197270240:AAF1ZW5COJZ3RqyJYfNNA3n6cxG98t-tBZY"
CHAT_ID = "-1003626550856"


def send_message(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()


def collect_moods():
    moods = []
    print("Enter 5 moods:")

    for i in range(5):
        mood = input(f"Mood {i + 1}: ").strip()
        moods.append(mood)

    return moods


def format_message(moods):
    lines = ["🧠 Daily Mood Report", ""]
    for mood in moods:
        lines.append(f"- {mood}")

    return "\n".join(lines)


if __name__ == "__main__":
    moods = collect_moods()
    message = format_message(moods)
    send_message(message)
    print("Message sent successfully.")

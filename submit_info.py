import requests
import json

base_url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

def collect_input(prompt, required=True):
    """Helper to safely collect user input"""
    while True:
        value = input(prompt).strip()
        if required and not value:
            print("This field is required. Please try again.")
        else:
            return value

def submit_info():
    """Collects student info and submits it with POST"""
    UCID = collect_input("Enter your UCID: ")
    first_name = collect_input("Enter your first name: ")
    last_name = collect_input("Enter your last name: ")
    github_username = collect_input("Enter your GitHub username: ")
    discord_username = collect_input("Enter your Discord username (with #tag): ")
    favorite_cartoon = collect_input("Enter your favorite cartoon: ")
    favorite_language = collect_input("Enter your favorite programming language: ")
    movie_or_game_or_book = collect_input("Enter your favorite movie, game, or book: ")
    section = "103"

    data = {
        "UCID": UCID,
        "first_name": first_name,
        "last_name": last_name,
        "github_username": github_username,
        "discord_username": discord_username,
        "favorite_cartoon": favorite_cartoon,
        "favorite_language": favorite_language,
        "movie_or_game_or_book": movie_or_game_or_book,
        "section": section
    }

    try:
        response = requests.post(
            base_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data),
            timeout=10
        )
        if response.status_code == 200:
            print("✅ Submitted successfully!")
            print("Response:", response.json())
        else:
            print(f"❌ Server returned error {response.status_code}")
            print("Details:", response.text)
    except Exception as e:
        print("⚠️ Error submitting info:", e)


def get_info():
    """Retrieves student info with GET"""
    UCID = collect_input("Enter your UCID to look up: ")
    section = "101"  # must match your submission

    url = f"{base_url}?UCID={UCID}&section={section}"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✅ Record found!")
            print("Response:", response.json())
        elif response.status_code == 404:
            print("⚠️ Record not found. Did you submit first?")
        else:
            print(f"❌ Server returned error {response.status_code}")
            print("Details:", response.text)
    except Exception as e:
        print("⚠️ Error retrieving info:", e)

def delete_info():
    """Deletes a student record with DELETE"""
    UCID = collect_input("Enter your UCID to delete: ")
    section = collect_input("Enter the section where you submitted (e.g., 101 or 103): ")

    url = f"{base_url}?UCID={UCID}&section={section}"

    try:
        response = requests.delete(url, timeout=10)
        if response.status_code == 200:
            print("✅ Record deleted successfully!")
            print("Response:", response.json())
        elif response.status_code == 404:
            print("⚠️ Record not found. Double-check UCID and section.")
        else:
            print(f"❌ Server returned error {response.status_code}")
            print("Details:", response.text)
    except Exception as e:
        print("⚠️ Error deleting info:", e)

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Submit my info (POST)")
    print("2. Get my info (GET)")
    print("3. Delete my info (DELETE)")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        submit_info()
    elif choice == "2":
        get_info()
    elif choice == "3":
        delete_info()
    else:
        print("Invalid choice.")




def show_calendar():
    print("\n --- Calendar --- ")
    print("today: 2024-06-01")
    print("events: register the lab work")

if __name__ == "__main__":
    show_calendar()

def feature_author():
    print("\n --- Author --- ")
    print("Name: aziz")
    print("Email:")

from datetime import datetime

def show_time():
    now = datetime.now()
    print("\n --- Current Time --- ")
    print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))


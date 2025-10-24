import datetime


def print_current_datetime():
    date_input = input("Enter a date in YYYY-MM-DD format: ")
    year, month, day = map(int, date_input.split("-"))

    date = datetime.date(year, month, day)
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day_name = days[date.weekday()]
    print(f"The day on {date} is {day_name}.")


if __name__ == "__main__":
    print_current_datetime()

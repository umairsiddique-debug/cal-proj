
def is_leap_year(year):
    """Return True if year is a leap year (Gregorian rules)."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def print_current_datetime():
    date_input = input("Enter a date in YYYY-MM-DD format: ")
    year, month, day = map(int, date_input.split("-"))
    print(f"You entered the date: Year={year}, Month={month}, Day={day}")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_date = "1970-01-01"
    date_and_day_dict  = {start_date: days[3]}  # 1970-01-01 was a Thursday
    current_year = 1970
    current_month = 1
    current_day = 1
    day_index = 3  # Index for Thursday
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while (current_year < year) or (current_year == year and current_month < month) or (current_year == year and current_month == month and current_day < day):
        current_day += 1
        day_index = (day_index + 1) % 7
        if current_day > month_days[current_month - 1]:
            if current_month == 2 and is_leap_year(current_year) and current_day == 29:
                pass
            else:
                current_day = 1
                current_month += 1
                if current_month > 12:
                    current_month = 1
                    current_year += 1
        date_str = f"{current_year:04d}-{current_month:02d}-{current_day:02d}"
        date_and_day_dict[date_str] = days[day_index]
    print(f"The day of the week for {date_input} is {date_and_day_dict[date_input]}")



if __name__ == "__main__":
    print_current_datetime()

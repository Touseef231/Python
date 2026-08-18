import datetime
current_year = datetime.datetime.now().year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"You are {age} years old")
days_lived = age * 365
print(f"You have lived approximately {days_lived} days in this universe.")
hours_lived = days_lived * 24
print(f"You have lived approximately {hours_lived} hours in this universe.")
seconds_lived = hours_lived * 60 * 60
print(f"You have lived approximately {seconds_lived} seconds in this universe.")
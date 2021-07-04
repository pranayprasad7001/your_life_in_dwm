print("Your Life in Days, Weeks & Months:\n")
# Enter your age.
age = input("What is your current age? ")
# Taking 90 years of age as max lifespan.
# Calculating no. of days, weeks & months left.
age_left = 90 - int(age)
days = age_left * 365
weeks = age_left * 52
months = age_left * 12
# Printing the days, weeks & months left to the end of  your lifespan.
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Delos Santos, Venn P.  // BSCS 2-A
# Problem Set 1.1
# Program that checks a person's birthdate and their corresponding horoscope

# datetime module import 
import datetime

# function for validating date format
def validate(date_text):
	try:
		datetime.datetime.strptime(date_text, '%B %d')
		return True
	except ValueError:
		return False

# statement to get and validate user input
while True:
	birthdate=input("Enter your Birthdate: ")
	if validate(birthdate):
		break
	else:
		print('Invalid Input')

date=datetime.datetime.strptime(birthdate,"%B %d")

month=date.month
day=date.day

if month == 1:
	horoscope = 'Capricornus' if (day < 22) else 'Aquarius'
elif month == 2:
	horoscope = 'Aquarius' if (day < 20) else 'Pisces'
elif month == 3:
	horoscope = 'Pisces' if (day < 20) else 'Aries'
elif month == 4:
	horoscope = 'Aries' if (day < 21) else 'Taurus'
elif month == 5:
	horoscope = 'Taurus' if (day < 20) else 'Gemini'
elif month == 6:
	horoscope = 'Gemini' if (day < 21) else 'Cancer'
elif month == 7:
	horoscope= 'Cancer' if (day < 22) else 'Leo'
elif month == 8:
	horoscope = 'Leo' if (day < 23) else 'Virgo'
elif month == 9:
	horoscope = 'Virgo' if (day < 23) else 'Libra'
elif month == 10:
	horoscope = 'Libra' if (day < 23) else 'Scorpius'
elif month == 11:
	horoscope= 'Scorpius' if (day < 24) else 'Sagittarius'
elif month == 12:
	horoscope = 'Sagittarius' if (day < 22) else 'Capricornus'
print("Your Horoscope is :", horoscope)
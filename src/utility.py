"""Contains various utility functions"""

import argparse
from datetime import datetime
from os import get_terminal_size

from .settings import DAY_LIMIT

def print_line():
	for i in range(get_terminal_size().columns):
		print("\u001b[31m-",end="")

# Checks for validity of date
def valid_date(s):
	try:
		date = datetime.strptime(s, "%Y-%m-%d")
	except ValueError:
		msg = "Invalid date: {0}".format(s)
		raise argparse.ArgumentTypeError(msg)
	try:
		if((date-datetime.now()).days>DAY_LIMIT):
			raise ValueError
	except ValueError:
		msg = f"CLI supports only {DAY_LIMIT} days of forecast"
		raise argparse.ArgumentError(msg)
	return date

# prints the weather of the given date
def print_weather(weather, given_date):
	loc_dict = dict(Latitude=weather['lat'], Longitude=weather['lon'], TimeZone=weather['timezone'])
	for key in loc_dict.keys():
		print(f"\u001b[32m{key}: \u001b[0m{loc_dict[key]}")
	print_line()
	for day in weather['daily']:
		date = datetime.fromtimestamp(day['dt'])
		if abs((date-given_date).days) <= 2:
			print(f"\u001b[34m{date.strftime('%Y-%m-%d')}")
			weather_dict = {'Humidity':day['humidity'],
							'Pressure':day['pressure'],
							'Average Temperature':day['temp']['day'],
							'Wind Speed': day['wind_speed'],
							'Wind Degree': day['wind_deg'],
							'UV Index': day['uvi']}
			for key in weather_dict.keys():
				print(f"\u001b[32m{key}: \u001b[0m{weather_dict[key]}")
			print_line()
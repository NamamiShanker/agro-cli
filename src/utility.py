"""Contains various utility functions"""

import argparse
from datetime import datetime

# Checks for validity of date
def valid_date(s):
	try:
		return datetime.strptime(s, "%Y-%m-%d")
	except ValueError:
		msg = "Invalid date: {0}".format(s)
		raise argparse.ArgumentTypeError(msg)

def print_weather(weather, date):
	print("TODO: Implement date function")
	pass
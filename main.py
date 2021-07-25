import argparse
import sys

from src.utility import valid_date
from src.app import arg_handler

def info():
	print("Weather CLI app for Agro")

parser = argparse.ArgumentParser()

parser.add_argument("-c",
					"--city",
					help="Get weather with city name")

parser.add_argument("-lg",
					"--longitude",
					help="Get weather with longitude",
					type=float)

parser.add_argument("-lt",
					"--latitude",
					help="Get weather with latitude",
					type=float)

parser.add_argument("-d",
					"--date",
					help="Get forecast of a date - format YYYY-MM-DD",
					required=True,
					type=valid_date)

ARGS = parser.parse_args()

# Check if user has provided at least some info about location
if((ARGS.city==None and (ARGS.longitude == None or ARGS.latitude == None))
	or (ARGS.longitude == None and ARGS.latititude == None) and ARGS.city==None):
	print("You need to enter either City name of the coordinates of location")
	sys.exit(1)

arg_handler(ARGS)
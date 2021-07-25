import os
import requests

from .settings import CURRENT_WEATHER_DATA
from .settings import ONE_CALL_API

class Search:
	def __init__(self, args):
		self.current_weather_url=CURRENT_WEATHER_DATA+\
								f"appid={os.environ.get('WEATHER_API_KEY')}"+"&"
		self.one_call_api_url=ONE_CALL_API+\
								f"appid={os.environ.get('WEATHER_API_KEY')}"+"&"
		self.args = args

	def get_weather_from_coordinates(self):
		params = dict(lat=self.args.latitude, lon=self.args.longitude)
		url = self.one_call_api_url
		for key in params.keys():
			url += f"{key}={params[key]}"+"&"
		try:
			response = requests.get(url)
			response.raise_for_status()
		except requests.exceptions.ConnectionError as e:
			print("Encountered Connection Error, please check your internet connection")
			raise SystemExit(e)
		except requests.exceptions.HTTPError as e:
			raise SystemExit(e)
		return response.json()


	def get_weather_from_city(self):
		params = dict(q=self.args.city)
		url = self.current_weather_url
		for key in params.keys():
			url += f"{key}={params[key]}"+"&"
		try:
			response = requests.get(url)
			response.raise_for_status()
		except requests.exceptions.ConnectionError as e:
			print("Encountered Connection Error, please check your internet connection")
			raise SystemExit(e)
		except requests.exceptions.HTTPError as e:
			raise SystemExit(e)
		res = response.json()
		self.args.latitude = res['coord']['lat']
		self.args.longitude = res['coord']['lon']
		return self.get_weather_from_coordinates()

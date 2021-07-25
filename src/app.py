from dotenv import load_dotenv

from .search import Search
from .utility import print_weather

load_dotenv()

def arg_handler(args):
	search_client = Search(args)
	if(args.city == None):
		weather = search_client.get_weather_from_coordinates()
	else:
		weather = search_client.get_weather_from_city()
	print_weather(weather, 'date')

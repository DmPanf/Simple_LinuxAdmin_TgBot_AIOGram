from pprint import pprint
from pickle import dump, load

with open('area.pkl', mode='rb') as f:
    cities = load(f)
pprint(cities)
#!/p/nvm/env/commontools/bin/python3
# -*- coding: utf-8 -*-
import random as rand
import datetime
import sys

date = datetime.datetime.today()
day = date.strftime('%A')

places = ["Cafe", "Pho ABC", "BJs", "Johnny Rockets", "Fire Rock", "Buckhorn", "Thai Paradise", "Land Ocean", "River Thai", "Pho M", "Mongolian BBQ", "Pieology", "Islands"]

if(day == "Tuesday"):
	print("Taco Tuesday @ Salsa's!")
	sys.exit(0)

choice = places[rand.randint(0, len(places)-1)]
print(choice)




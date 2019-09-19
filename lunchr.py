#!/p/nvm/env/commontools/bin/python3
# -*- coding: utf-8 -*-
import random as rand

places = ["Cafe", "Pho ABC", "Salsas", "BJs", "Johnny Rockets", "Fire Rock", "Buckhorn", "Thai Paradise", "Land Ocean", "River Thai", "Pho M", "Mongolian BBQ", "Pieology", "Islands"]


choice = places[rand.randint(0, len(places)-1)]
print(choice)




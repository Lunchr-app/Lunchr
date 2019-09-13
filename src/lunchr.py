#!/p/nvm/env/commontools/bin/python3
# -*- coding: utf-8 -*-
import random as rand

places = ["Cafe", "ABC Pho", "Salsas", "BJs", "Johnny Rockets", "Fire Rock", "Buckhorn", "Thai Paradise"]


choice = places[rand.randint(0, len(places)-1)]
print(choice)




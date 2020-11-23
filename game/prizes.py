from os import listdir
categories = ["body", "carry", "head", "shoe"]
base = 'cyberpi_dress_up_game/media/'
prizes = []
for category in categories: 
    items = (listdir(base + category)) 
    [prizes.append({"url":"/static/" + category + '/' + item,"id":item.encode("utf-8").hex(),"type":category}) for item in items]

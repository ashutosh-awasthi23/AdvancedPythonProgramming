scores={"alice":85, 'Bob':92, "Charlie":78, "David":65}
dicto={key:value+5 for key,value in scores.items() if value>80 }
print(dicto)
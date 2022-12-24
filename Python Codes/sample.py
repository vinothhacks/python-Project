from time import time


dict=[
    {"contry":"tamilnadu",
    "cities_visited":["virudhunagar","chennai","madurai","coimbature","tuthukudi"],
    "times":10
    },
    {"contry":"kerala",
    "cities_visited":["ooty",'kochi','beach'],
    "times":12
    }
]
for i in dict:
    print(i)
def dic(country,cities_visited,times):
    dict1={}
    dict1["country"]=country
    dict1["cities_visited"]=cities_visited
    dict1["time"]=times
    dict.append(dict1)

dic("marvel",["wakanda","new york","qweens","las vegas"],9)
print(dict)
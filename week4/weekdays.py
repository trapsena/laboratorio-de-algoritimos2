
def classes(week):
    weekend={}
    for i in week:
        ass= input(f"What do you have in {i}: ")
        weekend[i] = ass
    u = 0 
    for i in week:
        print(f"Na {i} voçê tem: {list(weekend.values())[u]}")
        u += 1
def main():
    
    week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    week = classes(week)
main()
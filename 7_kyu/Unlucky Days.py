from datetime import date

def unlucky_days(year):
    counter=0
    for i in range(1,13):
        if date(year, i, 13).weekday()==4:
            counter+=1
    return counter 
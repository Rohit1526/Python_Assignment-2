def bonus(salary):
    hike = salary*0.05
    print('Bonus is', round(hike))


salary = int(input())
years = int(input())

if years>5:
    bonus(salary)
else:
    print('No Bonus')
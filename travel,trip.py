class Travel:
    def __init__(self,city,days):
        self.city = city
        self.days = days

class Sport:
    def __init__(self,name,location):
        self.name = name
        self.location = location

trip = Travel("대전", 1)
sport = Sport("축구", "대전")

print(trip.city)
print(trip.days)

print(sport.name)
print(sport.location)

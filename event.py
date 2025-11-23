class Event:
    def __init__(self, name, date, price, attendees):
        self.name = name
        self.date = date
        self.price = price
        self.attendees = attendees

    def __str__(self):
        return f"{self.name} on {self.date}"

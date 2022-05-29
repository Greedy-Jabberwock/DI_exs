from datetime import datetime


def check_instance(cls, other):
    """Checks instance of class with given class, if True returns instance, else raise TypeError."""
    if isinstance(cls, other):
        return cls
    else:
        raise TypeError(f'Value must be {other.__name__()} class.')


class Airline:
    """
    Airline just represent a flight company and store planes of this company
    """

    def __init__(self, id: int, name: str):
        self.id = check_instance(id, str)
        self.name = check_instance(name, str)
        self.planes = []

    def __str__(self):
        return f'Airline {self.name}'

    def __repr__(self):
        return f"<Airline {self.name}:\n" \
               f"ID: {self.id}, " \
               f"Planes: {[str(p) for p in self.planes]}>"


class Airport:
    """
    Class represents airport in some city. It stores planes, which now at
    the airport and lists of departures and arrivals.
    """

    def __init__(self, city: str):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def __str__(self):
        return f'Airport {self.city}'

    def __repr__(self):
        return f'\nAirport {self.city}\n' \
               f'Planes: {[str(plane) for plane in self.planes]}\n' \
               f'Arrivals: {[str(flight) for flight in self.scheduled_arrivals]}\n' \
               f'Departures: {[str(flight) for flight in self.scheduled_departures]}\n'

    def schedule_flight(self, destination, date):
        """Finds available airplane in this Airport, schedules Airplane for the flight"""
        if self.planes != 0:
            for plane in self.planes:
                if plane.available_on_date(date, self):
                    date = check_instance(date, datetime)
                    flight = Flight(date, destination, self, plane)
                    sort_func = lambda x: x.date
                    self.scheduled_departures.append(flight)
                    self.scheduled_departures.sort(key=sort_func)
                    plane.next_flights.append(flight)
                    plane.next_flights.sort(key=sort_func)
                    destination.scheduled_arrivals.append(flight)
                    destination.scheduled_arrivals.sort(key=sort_func)
                    break
            else:
                print('There are no available airplanes at this date.')
        else:
            print('There are no airplanes in this airport.')

    def info(self, start_date, end_date):
        """Displays every scheduled flight from start_date to end_date"""
        filter_flight = lambda x: start_date <= x.date <= end_date
        filtered_departures = list(filter(filter_flight, self.scheduled_departures))
        filtered_arrivals = list(filter(filter_flight, self.scheduled_arrivals))
        print('--------------------------------------------------------')
        print(self.city)
        print(f'Departures:\n{[x.id for x in filtered_departures]}')
        print(f'Arrivals:\n{[x.id for x in filtered_arrivals]}')
        print('--------------------------------------------------------')


class Airplane:
    """
    Airplane represent the airplane. It stores current location of airplane,
    company and list of the next flights
    """

    def __init__(self, id, current_location: Airport, company: Airline):
        self.id = id
        self.current_location = current_location
        self.current_location.planes.append(self)
        self.company = company
        self.company.planes.append(self)
        self.next_flights = []

    def __str__(self):
        return f'Airplane {self.id}'

    def __repr__(self):
        return f'Airplane {self.id}:\n' \
               f'Location: {self.current_location}, ' \
               f'Company: {self.company}, ' \
               f'Flights: {[str(f) for f in self.next_flights]}'

    def fly(self, destination):
        """
        Method changes the current location of airplane,
        calling methods take_off() and land() from Fight class
        """
        if len(self.next_flights) == 0:
            print('There are no scheduled flights of this airplane.')
            return None
        next_flight = self.next_flights[0]
        if next_flight.destination == destination:
            self.next_flights.pop(0)
            next_flight.take_off()
            next_flight.land()
        else:
            print("There is no such flight in the schedule.")

    def location_on_date(self, date):
        """
        Method returns where the airplane will be on given date.
        """
        if len(self.next_flights) == 0:
            return self.current_location
        for flight in self.next_flights:
            if flight.date == date:
                return flight.origin
        else:
            return None

    def available_on_date(self, date, location):
        """
        Returns True if the plane can fly from given location on this day
        (airplane is in this location and have no flights on this day)
        """
        for flight in self.next_flights:
            if flight.date == date:
                return False
        if self.location_on_date(date) == location:
            return True
        else:
            return False


class Flight:
    """
    This class represents information about flight. It's methods just change data in other classes.
    """

    def __init__(self, date, destination, origin, plane):
        self.date = check_instance(date, datetime)
        self.destination = check_instance(destination, Airport)
        self.origin = check_instance(origin, Airport)
        self.plane = check_instance(plane, Airplane)
        self.id = f"{destination.city}-{plane.company.id}-{date.strftime('%Y/%m/%d')}"

    def __str__(self):
        return f'{self.id}'

    def __repr__(self):
        return f'\nFlight {self.id}: ' \
               f'Plane: {self.plane},' \
               f'Date: {self.date},' \
               f'Origin: {self.origin},' \
               f'Destination: {self.destination}\n'

    def take_off(self):
        """Remove current plane from origin Airport"""
        plane_index = self.origin.planes.index(self.plane)
        self.origin.planes.pop(plane_index)
        flight_index = self.origin.scheduled_departures.index(self)
        self.origin.scheduled_departures.pop(flight_index)

    def land(self):
        """Append current plane to the Airport scheduled arrivals"""
        self.destination.planes.append(self.plane)
        flight_index = self.destination.scheduled_arrivals.index(self)
        self.destination.scheduled_arrivals.pop(flight_index)
        self.plane.current_location = self.destination


def main():
    el_al = Airline('EL', 'El-Al')
    ren_air = Airline('RA', 'RenAir')
    aeroflot = Airline('AF', 'Aeroflot')

    winna = Airport('Winna')
    vnukovo = Airport('Vnukovo')
    ben_gurion = Airport('Ben_Gurion')
    istanbul = Airport('Istanbul')

    el_1 = Airplane(5098, istanbul, el_al)
    el_2 = Airplane(8903, vnukovo, el_al)
    air_1 = Airplane(234, winna, ren_air)
    air_2 = Airplane(222, ben_gurion, ren_air)
    aero_1 = Airplane(12455, vnukovo, aeroflot)
    aero_2 = Airplane(12344, istanbul, aeroflot)

    _date = datetime(2022, 10, 12)

    vnukovo.schedule_flight(istanbul, _date)
    vnukovo.schedule_flight(winna, _date)

    istanbul.schedule_flight(ben_gurion, _date)
    istanbul.schedule_flight(ben_gurion, _date)
    istanbul.schedule_flight(ben_gurion, _date)

    el_2.fly(istanbul)
    air_1.fly(winna)

    istanbul.schedule_flight(ben_gurion, datetime(2022, 10, 11))
    istanbul.schedule_flight(vnukovo, datetime(2023, 12, 1))

    start_date = datetime(2021, 10, 12)
    end_date = datetime(2023, 10, 12)
    istanbul.info(start_date, end_date)
    ben_gurion.info(start_date, end_date)

    istanbul.schedule_flight(vnukovo, datetime(2022, 10, 11))

    print(istanbul.__repr__())
    print(el_1.__repr__())


main()

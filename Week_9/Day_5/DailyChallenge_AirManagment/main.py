from datetime import datetime

class Airline:
    """
    Airline just represent a flight company and store planes of this company
    """
    def __init__(self, name):
        print('\nAirline initialized.')
        self.name = name
        self.id = self.name[:2].upper()
        self.planes = []
        print(self)

    def __repr__(self):
        return f'|||Airline {self.name}, ' \
               f'ID: {self.id}, ' \
               f'Planes: {self.planes}|||'

    def __str__(self):
        return f'Airline {self.name}'


class Airplane:
    """
    Airplane represent the airplane. It stores current location of airplane,
    company and list of the next flights
    """
    def __init__(self, id, current_location, company):
        print('\nAirplane initialized.')
        self.id = id
        self.current_location = current_location
        self.company = company
        self.company.planes.append(self)
        self.current_location.planes.append(self)
        self.next_flights = []
        print(self)

    def __repr__(self):
        return f'\t|||Airplane {self.id}, ' \
               f'curr_loc: {self.current_location}, ' \
               f'company: {self.company}, ' \
               f'next_flights: {self.next_flights} |||\t'

    def __str__(self):
        return f'Airplane {self.id}'

    def fly(self, destination):
        """
        Method needs to change current location of airplane, using take_off
        and land methods of Flight class
        """
        print(f'Airplane {self.id} fly method.')
        if len(self.next_flights) > 0:
            flight = self.next_flights.pop(0)
            if flight.destination == destination:
                flight.take_off()
                flight.land()
                print(f'Airplane {self.id} fly method ends successfully.')
            else:
                print(f'Airplane {self.id} fly method ends.')
                print('There is no such destination in this flight.')
        else:
            print(f'Airplane {self.id} fly method ends.')
            print('There is no scheduled flights for this plane.')

    def location_on_date(self, date):
        """
        Method returns the location where the airplane will be on a given date
        """
        print(f'Airplane {self.id} location_on_day method starts.')
        filter_result = filter(lambda flight: flight.date == date, self.next_flights)
        result = []
        for _flight in filter_result:
            result.append(_flight.origin)
            print(f'Airplane {self.id} location_on_day method ends.\n'
                  f'Result: {result}')
        return result

    def available_on_date(self, date, location):
        """
        Method returns True, if Airplane has no flights on a given date, else False
        """
        print(f'Airplane {self.id} available_on_day method starts.')
        if len(self.next_flights) == 0 and self.current_location == location:
            print(f'Airplane {self.id} available_on_day method ends.'
                  f'Return True (list is empty and current.location == location)')
            return True
        for flight in self.next_flights:
            pass


class Flight:
    """
    This class represents information about flight. It's methods just change data in other classes.
    """
    def __init__(self, date, destination, origin, plane):
        print('\nFlight initialized.')
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f'{destination.city}-{self.plane.company.id}-{date.year[1:4]}' \
                  f'{date.month}{date.day}'
        print(self)

    def __repr__(self):
        return f'|||\tFlight: Date: {self.date}, Destination: {self.destination}, ' \
               f'Origin: {self.origin}, Plane: {self.plane}, ID: {self.id}|||\t'

    def __str__(self):
        return f'Flight {self.id}'

    def take_off(self):
        """
        Deletes plane from origin Airport list of planes
        """
        print(f'Flight {self.id} take_off method starts.')
        index_in_list = self.origin.planes.index(self.plane)
        self.origin.planes.pop(index_in_list)
        print(f'Flight {self.id} available_on_day method ends.')

    def land(self):
        """
        Add plane to list in destination Airport
        """
        print(f'Flight {self.id} land method starts.')
        self.destination.planes.append(self.plane)
        print(f'Flight {self.id} land method ends.')


class Airport:
    """
    Class represents airport in some city. It stores planes, which now at
    the airport and lists of departures and arrivals.
    """
    def __init__(self, city):
        print('\nAirport initialized')
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []
        print(self)

    def __repr__(self):
        return f'|||\tAirport in {self.city}, ' \
               f'Planes: {self.planes}, ' \
               f'Scheduled departures: {self.scheduled_departures}, ' \
               f'Scheduled arrivals: {self.scheduled_arrivals}|||\t'

    def __str__(self):
        return f'Airport in {self.city}'

    def schedule_flight(self, destination, datetime):
        """
        Finds an available airplane from an airline and schedules the airplane
        for the flight.
        """
        print(f'Airport {self.city} schedule_flight method starts.')
        for plane in self.planes:
            if plane.available_on_date(datetime, destination):
                flight = Flight(datetime, destination, self, plane)
                self.scheduled_departures.append(flight)
                destination.scheduled_arrivals.append(flight)
        print(f'Airport {self.city} schedule_flight method ends.')

    def info(self, start_date, end_date):
        """
        Prints info about flights from the start date to the end date
        """
        print(f'Airport {self.city} info method starts.')
        filtered_result = filter(lambda flight:
                                 start_date <= flight.date <= end_date)
        for result in filtered_result:
            print(result if len(filtered_result) > 0 else 'No flights in this dates.')
        print(f'Airport {self.city} info method ends.')


def main():
    winna = Airport('Winna')
    moscow = Airport('Moscow')
    istanbul = Airport('Istanbul')

    el_al = Airline('El-Al')
    renair = Airline('RenAir')

    air1 = Airplane(234, winna, el_al)
    air2 = Airplane(111, moscow, el_al)

    winna.schedule_flight(istanbul, datetime(2022, 5, 14))


main()
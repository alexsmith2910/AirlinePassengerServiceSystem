import attr
import datetime


@attr.s(slots=True, order=True)
class Flight:
    flight_id: str = attr.ib(converter=str)
    departure: str = attr.ib(converter=str)
    arrival: str = attr.ib(converter=str)
    time_to_dest: str = attr.ib(converter=str)  # dd-mm-yyyy
    flight_path: str = attr.ib(converter=str)
    passengers: str = attr.ib(converter=str)

    @staticmethod
    def load_from_database(data):
        try:
            return Flight(data["email"])
        except KeyError as e:
            print(e)  # update logger
            return None

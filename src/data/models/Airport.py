import attr
import datetime


@attr.s(slots=True, order=True)
class Airport:
    airport_id: str = attr.ib(converter=str)
    name: str = attr.ib(converter=str)
    code: str = attr.ib(converter=str)  # e.g. DXB = Dubai, LHR = London Heathrow
    connected_airports: list = attr.ib(converter=list)  # list of airports

    @staticmethod
    def load_from_database(data):
        try:
            return Airport(data["airport_id"],
                           data["name"],
                           data["code"],
                           data["connected_airports"])
        except KeyError as e:
            print(e)  # update logger
            return None

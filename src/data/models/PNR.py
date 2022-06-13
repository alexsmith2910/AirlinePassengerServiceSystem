import attr
import datetime

from src.data.models.PaymentMethod import PaymentMethod
from src.data.models.FrequentFlyerNumber import FrequentFlyerNumber


@attr.s(slots=True, order=True)
class PassengerNameRecord:
    pnr_id: str = attr.ib(converter=str)
    redress_number: str = attr.ib(converter=str)  # 9-digits
    received_from: str = attr.ib(converter=str)  # last person to edit PNR

    itinerary: list = attr.ib(converter=list)  # in-order itinerary
    ticketing: dict = attr.ib(converter=dict)  # 0: how a ticket is issued. 1: when to issue the ticket

    email: str = attr.ib(converter=str)
    phone_number: str = attr.ib(converter=str)

    forenames: str = attr.ib(converter=str)
    surname: str = attr.ib(converter=str)
    dob: str = attr.ib(converter=str)  # dd-mm-yyyy
    gender: str = attr.ib(converter=str)  # M, F, Other.

    payment_method: PaymentMethod = attr.ib(validator=attr.validators.instance_of(PaymentMethod))
    frequent_flyer_no: FrequentFlyerNumber = attr.ib(validator=attr.validators.instance_of(FrequentFlyerNumber))
    meal_preferences: dict = attr.ib(converter=dict)

    @staticmethod
    def load_from_database(data):
        try:
            return PassengerNameRecord(data["pnr_id"],
                                       data["redress_number"],
                                       data["received_from"],
                                       data["itinerary"],
                                       data["ticketing"],
                                       data["email"],
                                       data["phone_number"],
                                       data["forenames"],
                                       data["surname"],
                                       data["dob"],
                                       data["gender"],
                                       data["payment_method"],
                                       data["frequent_flyer_no"],
                                       data["meal_preferences"])
        except KeyError as e:
            print(e)  # update logger
            return None

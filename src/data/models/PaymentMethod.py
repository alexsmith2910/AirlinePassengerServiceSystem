import attr
import datetime


@attr.s(slots=True, order=True)
class PaymentMethod:
    # add payment method options here

    @staticmethod
    def load_from_database(data):
        try:
            return PaymentMethod()
        except KeyError as e:
            print(e)  # update logger
            return None

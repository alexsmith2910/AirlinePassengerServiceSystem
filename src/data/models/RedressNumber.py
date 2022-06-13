import attr
import datetime


@attr.s(slots=True, order=True)
class RedressNumber:
    # add redress number

    @staticmethod
    def load_from_database(data):
        try:
            return RedressNumber()
        except KeyError as e:
            print(e)  # update logger
            return None

import attr
import datetime


@attr.s(slots=True, order=True)
class FrequentFlyerNumber:
    # add freq flyer no

    @staticmethod
    def load_from_database(data):
        try:
            return FrequentFlyerNumber()
        except KeyError as e:
            print(e)  # update logger
            return None

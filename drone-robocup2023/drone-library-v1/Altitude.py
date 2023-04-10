from enum import IntEnum


class Altitude(IntEnum):
    """
    enumeračná trieda s výškami pre lepšiu prehľadnosť
    """
    NADLET = 170
    PODLET = 60
    REGULAR = 100
    ZODVIHNI_OBET = 40 # vyska letu do ktorej cca treba klesnúť na zdvihnutie obete, záleží od vášho prístupu zdvíhania

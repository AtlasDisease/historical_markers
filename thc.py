# --- Imports --- #

import datetime as dt
from dataclasses import dataclass
from enum import StrEnum, auto


# --- HistoricalMarkerType Enum --- #

class HistoricalMarkerType(StrEnum):
    LARGE_SUBJECT = auto()
    SMALL_SUBJECT = auto()
    MEDALLION_PLAQUE = auto()
    LARGE_CEMETERY = auto()
    SMALL_CEMETERY = auto()
    MEDALLION_PLAQUE_CEMETERY = auto()
    CENTENNIAL = auto()
    TRAVEL = auto()


# --- Location Class --- #

@dataclass(slots=True)
class Location:
    """Location Class"""
    city: str
    county: str
    state: str
    country: str
    

# --- HistoricalMarker Class --- #

@dataclass(slots=True)
class HistoricalMarker:
    name: str
    type: HistoricalMarkerType
    year: dt.date
    location: Location
    desc: str = ""

    def __str__(self) -> str:
        return f"{self.name}:\r\n{self.desc} ({self.year:%Y})"


# --- Main --- #

def main():
    thm = HistoricalMarker("Texas A&M University",
                           HistoricalMarkerType.LARGE_SUBJECT,
                           dt.date(year=1978, month=1, day=1),
                           """Texas A&M University""")
    cen_loc = Location("Bryan", "Brazos", "Texas", "U.S.A")
    cen_thm = HistoricalMarker("Site of the Town of Boonville",
                               HistoricalMarkerType.CENTENNIAL,
                               dt.date(year=1936, month=1, day=1),
                               cen_loc,
                               """Established in 1841 as county seat of
Navasota County by John Millican, John H.
Jones, J. Ferguson, E. seale, and Mordecai
Boon whose name it bears. The name
of the county was changed to Brazos in
1842. Boonville flourished until 1866 when
Bryan was established on the rairoad""")
    print(thm, "\r\n", cen_thm)


if __name__ == "__main__":
    main()
    

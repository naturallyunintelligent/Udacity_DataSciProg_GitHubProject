DATAPATH = "../data/"

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

MONTHNAMES = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

# typos - presumed to be a valid choice that has been mis-spelt
TYPOS = {
    "chicgo": "chicago",
    "chiago": "chicago",
    "chacago": "chicago",
    "chicargo": "chicago",
    "new york": "new york city",
    "nyc": "new york city",
    "newyorkcity": "new york city",
    "newyork": "new york city",
    "ny city": "new york city",
    "nycity": "new york city",
    "wash": "washington",
}
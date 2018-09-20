
def get_earliest(*argv: str) -> str:
    """returns the earliest of all the passed date strings"""
    earliest = get_earliest_helper(argv[0], argv[1])
    for i in range(2, len(argv)):
        earliest = get_earliest_helper(earliest, argv[i])
    return earliest


def get_earliest_helper(date1: str, date2: str) -> str:
    """returns the earliest of the two passed date strings"""
    date1_split = date1.split('/')
    date2_split = date2.split('/')
    date1_arr = [
        date1_split[2],  # year
        date1_split[0],  # month
        date1_split[1]   # day
    ]
    date2_arr = [
        date2_split[2],
        date2_split[0],
        date2_split[1]
    ]

    for i in range(0, 3):
        date1_part = date1_arr[i]
        date2_part = date2_arr[i]
        if date1_part > date2_part:
            return date2
        elif date1_part < date2_part:
            return date1


def get_month(date: str) -> str:
    """gets the month from the passed date string"""
    return date.split('/')[0]


def get_day(date: str) -> str:
    """gets the day from the passed date string"""
    return date.split('/')[1]


def get_year(date: str) -> str:
    """gets the year from the passed date string"""
    return date.split('/')[2]

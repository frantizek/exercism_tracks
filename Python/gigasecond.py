# determine the date and time one gigasecond after a certain date.
#
# A gigasecond is one thousand million seconds. That is a one with nine zeros after it.
#
# If you were born on January 24th, 2015 at 22:00 (10:00:00pm), 
# then you would be a gigasecond old on October 2nd, 2046 at 23:46:40 (11:46:40pm).

from datetime import datetime, timedelta

def add(date: datetime) -> datetime:
    """
    Add 1 gigasecond (10^9 seconds) to the given datetime.
    """
    return date + timedelta(seconds=1_000_000_000)
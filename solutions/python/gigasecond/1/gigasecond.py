import datetime

def add(moment):
    diff = datetime.timedelta(seconds=1_000_000_000)
    future = moment + diff
    return(future)


# function which aims to convert the users current time to seconds w.r.t. some time
# basing all these times of my reference time which is- 00:00 01/01/2010 (european time)

def dateConverter(minuteS,hourS,dayS,monthS,yearS):


    minute = float(minuteS)
    hour = float(hourS)
    day = float(dayS)
    month = float(monthS)
    year = float(yearS)


    days = float(day) - 1

    if month == 2:
        days =+ 31
    elif month == 3:
        days =+ 59
    elif month == 4:
        days =+ 90
    elif month == 5:
        days =+ 120
    elif month == 6:
        days =+ 151
    elif month == 7:
        days =+ 181
    elif month == 8:
        days =+ 212
    elif month == 9:
        days =+ 243
    elif month == 10:
        days =+ 273
    elif month == 11:
        days =+ 304
    elif month == 12:
        days =+ 334

    N= (year - 2000)
    q = (N //4) +1.0
    z = (N *365)+q-1.5
    yearInSeconds = z *(3.154*10**7)
    dayInSeconds = days * 86400
    hourInSeconds = hour * 3600
    minuteInSeconds = minute * 60

    totalSeconds = yearInSeconds + hourInSeconds + minuteInSeconds + dayInSeconds

    return totalSeconds

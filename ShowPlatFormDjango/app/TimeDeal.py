import time

def getCurrentTimeStamp():

    return time.time()


def convertDateTimeToTimeStamp(timeStamp):
    dateTime = time.strftime("%Y-%m-%d", time.localtime(timeStamp))
    dateTimeStamp = time.mktime(time.strptime(dateTime,"%Y-%m-%d"))

    return dateTimeStamp


def compareDateTime(timeStamp):

    currentDateTimeStamp = convertDateTimeToTimeStamp(getCurrentTimeStamp())
    dateTimeStamp = convertDateTimeToTimeStamp(timeStamp)

    compareTimeStamp = float(currentDateTimeStamp) - float(dateTimeStamp)

    oneDayStamp = 86400
    dayCount = compareTimeStamp/oneDayStamp

    return int(dayCount)

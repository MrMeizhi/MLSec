from django.shortcuts import render
from django.http import HttpResponse
from app.models import dbOperator
from app.TimeDeal import compareDateTime
import time
# Create your views here.
def index(request):

    return render(request,"home.html")


def getData(request):

    db = dbOperator("WYUSEC","Login")
    data = list(db.find())
    resultList = [0]*8
    finalResult = str()

    for oneQuery in data:
        name = oneQuery[u"time"]
        stamp = compareDateTime(float(name))
        if stamp < 7:
            resultList[stamp] += 1
        else:
            resultList[7] += 1

    for one in resultList:
        finalResult += str(one) + '-'
    finalResult = finalResult.rstrip('-')
    return HttpResponse(finalResult)

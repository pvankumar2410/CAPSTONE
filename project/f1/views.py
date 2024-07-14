from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import joblib
import numpy as np
loaded_rf = joblib.load("f1\static\my_random_forest.joblib")

def view_detail(request):
    myval="no data"
    raceLaps=0
    racePoints=0
    avgSpeed=0 
    practiceLaps=0
    practicePos=0
    noOfFastLap=0
    startgridNo=0
    startgridPos=0
    qualifyingLaps= 0
    stops=0
    practiceTimeSeconds=0
    startgridTimeSeconds=0
    timeTakenInFastLapsSeconds=0
    lapCount=0
    dnf=0
    pitstopHour=0
    pitstopMinute=0
    pitstopSecond=0
    if request.method == "POST":
        raceLaps = request.POST.get('raceLaps')
        racePoints= request.POST.get('racePoints')
        avgSpeed= request.POST.get('avgSpeed')
        practiceLaps= request.POST.get('practiceLaps')
        practicePos= request.POST.get('practicePos')
        noOfFastLap= request.POST.get('noOfFastLap')
        startgridNo= request.POST.get('startgridNo')
        startgridPos= request.POST.get('startgridPos')
        qualifyingLaps= request.POST.get('qualifyingLaps')
        stops= request.POST.get('stops')
        practiceTimeSeconds= request.POST.get('practiceTimeSeconds')
        startgridTimeSeconds= request.POST.get('startgridTimeSeconds')
        timeTakenInFastLapsSeconds= request.POST.get('timeTakenInFastLapsSeconds')
        lapCount=request.POST.get('lapCount')
        dnf= request.POST.get('dnf')
        pitstopHour= request.POST.get('pitstopHour')
        pitstopMinute= request.POST.get('pitstopMinute')
        pitstopSecond= request.POST.get('pitstopSecond')
        print(raceLaps,racePoints,avgSpeed, practiceLaps,practicePos,noOfFastLap,startgridNo,startgridPos,qualifyingLaps,stops,practiceTimeSeconds,startgridTimeSeconds,timeTakenInFastLapsSeconds,dnf,pitstopHour,pitstopMinute,pitstopSecond)
        prediction=loaded_rf.predict(np.array([[float(raceLaps),float(racePoints),float(avgSpeed), float(practiceLaps),int(practicePos),float(noOfFastLap),int(startgridNo),int(startgridPos),float(qualifyingLaps),int(stops),float(practiceTimeSeconds),float(startgridTimeSeconds),float(timeTakenInFastLapsSeconds),int(lapCount),int(dnf),int(pitstopHour),int(pitstopMinute),int(pitstopSecond)]]))
        print(prediction[0])
        myval=prediction[0]
        if prediction[0]==0:
            myval="NO RESULT FOUND OR INVALID DATA GIVEN"

        print("myval",myval)
    return render(request,"index.html",{'key':myval,
'raceLaps':raceLaps,
'racePoints':racePoints,
'avgSpeed':avgSpeed, 
'practiceLaps':practiceLaps,
'practicePos':practicePos,
'noOfFastLap':noOfFastLap,
'startgridNo':startgridNo,
'startgridPos':startgridPos,
'qualifyingLaps':qualifyingLaps,
'stops':stops,
'practiceTimeSeconds':practiceTimeSeconds,
'startgridTimeSeconds':startgridTimeSeconds,
'timeTakenInFastLapSeconds':timeTakenInFastLapsSeconds,
'lapCount':lapCount,
'dnf':dnf,
'pitstopHour':pitstopHour,
'pitstopMinute':pitstopMinute,
'pitstopSecond':pitstopSecond})



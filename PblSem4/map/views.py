from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models  import lecture
from datetime import time,datetime
from .forms import LectureForm

# Create your views here.
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

######################   HOME PAGE    ###################
def index(request):
    return render(request,'index.html')


###########################    MAP    ###############################
def map(request):
    context = {}
    dayy = "Thursday"
    # dayy = week[datetime.today().weekday()]
    n = datetime.now()
    # v = time(n.hour,n.minute,n.second)
    v = time(9,45,23)
    lectures_list = lecture.objects.filter(day = dayy)
    for lect in lectures_list:
        if f"{lect.classroom}status" not in context:
            context[f"{lect.classroom}status"] = "Vacant"
    
    for lect in lectures_list:
        if lect.startTime < v and lect.endTime > v:
            context[f"{lect.classroom}status"] = "Occupied"
        # else:(This part of code updates value of classroom status even if it was previously occupied at current time thus resulting in wrong status values)
        #     context[f"{lect.classroom}status"] = "Vacant"
    return render(request,'map.html',context)


########################################################################


# def login(request):
#     return render(request,'login.html')



##########################     To SHOW TIMETABLE        ###############################
def classroom(request,class_num):
    mon = lecture.objects.filter(day = "Monday" ,classroom = class_num).order_by('startTime')
    tue = lecture.objects.filter(day = "Tuesday",classroom = class_num).order_by('startTime')
    wed = lecture.objects.filter(day = "Wednesday",classroom = class_num).order_by('startTime')
    thu = lecture.objects.filter(day = "Thursday",classroom = class_num).order_by('startTime')
    fri = lecture.objects.filter(day = "Friday",classroom = class_num).order_by('startTime')
    context = {
        "classroom":class_num,
        "monday":mon,
        "mlen":range(7-len(mon)),
        "tuesday":tue,
        "tlen":range(7-len(tue)),
        "wednesday":wed,
        "wlen":range(7-len(wed)),
        "thursday":thu,
        "thlen":range(7-len(thu)),
        "friday":fri,
        "flen":range(7-len(fri))
    }
    return render(request,'timetable.html',context)


##############################  ADD LECTURE TO DATABASE   ######################################
def add_lecture(request):
    submitted = False
    if request.method == "POST" :
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("add_lecture?submitted=True")
    
    else:
        #hello
        form = LectureForm
        if 'submitted' in request.GET:
            submitted = True

    form = LectureForm
    return render(request,'AddLecture.html',{"form":form,"submitted":submitted})

###################### UPDATE EXISTING LECTURE FROM DATABASE ###################################
def update_lect(request,lecture_id):

    lect = lecture.objects.get(pk=lecture_id)
    form = LectureForm(request.POST or None,instance = lect)
    if form.is_valid():
        form.save()
        return redirect("show-timetable",class_num = lect.classroom)
    return render(request,'update_lecture.html',{"form":form,"lect":lect})

######################     DELETE EXISTING LECTURE FROM DATABASE    #########################

def delete_lect(request,lecture_id):
    lect = lecture.objects.get(pk=lecture_id)
    lect.delete()

    return redirect("show-timetable",class_num = lect.classroom)


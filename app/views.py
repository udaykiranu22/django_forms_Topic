from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def contact(request):
    ECFO = ContactForm()        # Empty Contact File Objecet
    d = {'ECFO':ECFO}
    if request.method == 'POST':
        FDO = ContactForm(request.POST)
        # Django forms validation is must
        if FDO.is_valid():
            return HttpResponse(str(FDO.cleaned_data))
        else:
            return HttpResponse('invalid data')

    return render(request, 'contact.html', d)


def Display_Topic(request):
    ETFO = TopicForm()
    d = {'ETFO': ETFO}

    if request.method == 'POST':
        tno = TopicForm(request.POST)
        if tno.is_valid():
            tn = tno.cleaned_data['topic_name']
            TO = Topic.objects.get_or_create(Topic_name = tn)
            if TO[1]:
                return HttpResponse(f'{tn} data is inserted')
            else:
                return HttpResponse(f'{tn} data is already inserted')
    return render(request, 'insert_Topic.html', d)

def Display_Webpage(request):
    EWFO = WebpageForm()
    d = {'EWFO':EWFO}

    if request.method == 'POST':
        FDO = WebpageForm(request.POST)
        if FDO.is_valid():
            tn = FDO.cleaned_data['topic_name']
            name = FDO.cleaned_data['name']
            url = FDO.cleaned_data['url']
            TO = Topic.objects.get(Topic_name = tn)
            WO = Webpage.objects.get_or_create(Topic_name = TO, Name = name, Url = url)
            if WO[1]:
                 return HttpResponse(f'{name} data is inserted')
            else:
                return HttpResponse(f'{name} data is already inserted')
    return render(request, 'insert_webpage.html', d)

def Display_AccessRecord(request):
    EAFO = AccessRecord()
    d = {'EAFO':EAFO}
    if request.method == 'POST':
        DFO = AccessRecord(request.POST)
        if DFO.is_valid():
            name = DFO.cleaned_data['name']
            a = DFO.cleaned_data['author']
            d = DFO.cleaned_data['date']
            WO = Webpage.objects.get(Name = name)
            AO = AccessRecords.objects.get_or_create(Name = WO, Author = a, Date = d)
            if AO[1]:
                return HttpResponse(f'{a} data is inserted')
            else:
                return HttpResponse(f'{a} data is already inserted')
        else:
            return HttpResponse(f' data is invalid')
    return render(request, 'insert_accessrecord.html',d)

def update_webpage(request):
    
    Webpage.objects.filter(Topic_name='volleyball').update(Url='http://new.in')
    WO = Webpage.objects.all()
    TO = Topic.objects.get(Topic_name = 'cricket')
    Webpage.objects.update_or_create(Name='kishore',defaults={'Topic_name':TO})
    WO = Webpage.objects.filter(Topic_name='cricket')
    return render(request,'display.html',{'WO':WO})


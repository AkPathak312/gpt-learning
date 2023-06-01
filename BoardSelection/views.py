from django.shortcuts import render, HttpResponse
from BoardSelection.pdfreadertest import processPdf
from .models import Topic


# Create your views here.

def home(request):
    return render(request,'home.html')

def index(request):
    queryText = 'Placeholder'
    selectedTopic = 'What is Force?'
    topicdata = Topic.objects.all().values()
    if request.method == 'POST':
        if 'textToSpeechBtn' in request.POST:
            import pyttsx3
            engine= pyttsx3.init()
            engine.say(request.POST.get("topciSummaryTextArea"))
            engine.runAndWait()
            return render(request,'topicdashboard.html',{'responseText':'','topicdata':topicdata,'topicSummary':request.POST.get("topciSummaryTextArea")})
        if 'inlineRadioOptions' in request.POST:
            queryText = 'Give 5 '+request.POST["inlineRadioOptions"]+' from '+selectedTopic
        if 'submitButton' in request.POST:
            queryText=request.POST.get('queryText')
            print(queryText)
        response = processPdf(queryText=queryText)
        return render(request,'topicdashboard.html',{'responseText':response,'topicdata':topicdata,'topicSummary':request.POST.get("topciSummaryTextArea")})
    else:
        response = processPdf('Give a summary of '+selectedTopic)
        return render(request,'topicdashboard.html',{'topicdata':topicdata,'topicSummary':response})
    

def topicsummary(request, chapter_name):
     return HttpResponse(chapter_name)
#this file created by - Harsh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    Charactercount=request.POST.get('Charactercount', 'off')
    CountOfWords=request.POST.get('CountOfWords', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (Charactercount == "on"):
        count = 0;
        for i in range(0, len(djtext)):
            if (djtext[i] != ' '):
                count = count + 1;
        params = {'purpose': 'Total number of characters in a string', 'analyzed_text': count}

    if (CountOfWords == "on"):
        countOfWords = len(djtext.split())
        params = {'purpose': 'Total number of word count', 'analyzed_text': countOfWords}


    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and Charactercount!="on" and CountOfWords!="on"):
        return HttpResponse("<h1>please select any operation and try again</h1> <br><br> <form action='/'><button type='submit'>Home page</button></form>")

    return render(request, 'analyze.html', params)
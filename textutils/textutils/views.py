from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def analyze(request):
    djText = request.POST.get('text', 'default')

    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('toupper', 'off'))
    newlineremove = (request.POST.get('lineremove', 'off'))
    charactercount = (request.POST.get('charactercount', 'off'))
    extraspaceremover = (request.POST.get('extraspcrem', 'off'))

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    analyzed = ""
    if removepunc == "on":
            
        for char in djText:
            if char not in punctuations:
                analyzed += char


        params = {
            'purpose': ' - Remove Punctuations',
            'analyzed_text': analyzed
        }

        djText = analyzed


    if fullcaps == "on":
        analyzed = ""
        analyzed = djText.upper()


        params = {
            'purpose': ' - Converted to upperCase',
            'analyzed_text': analyzed
        }
        djText = analyzed

    if  newlineremove == "on":
        analyzed = ""
        for char in djText:
            if char != "\n" and char != "\r":
                analyzed += char
            else:
                print("no")

        params = {
            'purpose': ' - Removing new line',
            'analyzed_text': analyzed
        }
        djText = analyzed
    if  charactercount == "on":
        analyzed = ""
        count = 0
        for char in djText:
            if char != " ":
                count += 1
                analyzed = "No of characters: " + str(count)
                


        params = {
            'purpose': ' - No of characters',
            'analyzed_text': analyzed
        }
        djText = analyzed    
    if  extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate (djText):
            if not(djText[index] == " " and djText[index+1] == " "):
                analyzed += char   
        
        params = {
            'purpose': ' - Extra space removed',
            'analyzed_text': analyzed
        }
        djText = analyzed


    return render(request, "analyze.html", params)

    








def capfirst(request):
    return HttpResponse("capitalize first")


def newlineremove(request):
    return HttpResponse("new line remove")


def spaceremove(request):
    return HttpResponse("space remove")


def charcount(request):
    return HttpResponse("char count")

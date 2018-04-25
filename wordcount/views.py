from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'hithere':'HelloAgain'})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordList= fulltext.split()

    worddict = {}

    for word in wordList:
        if word in worddict:
            #Increase
            worddict[word] +=1
        else:
            worddict[word] =1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordList), 'sortedwords':sortedwords})

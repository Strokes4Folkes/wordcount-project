from django.http import HttpResponse
from django.shortcuts import render
import operator

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def eggs(request):
        return HttpResponse('<h1>EGGS</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}


    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1

        else:
            #add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)


    print(fulltext)
    return render(request, "count.html",{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

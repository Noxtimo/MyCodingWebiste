from django.shortcuts import render

def home(request):


    return render(request, 'base/home.html')



def about(request):


    return render(request, 'base/about.html')


def topics(request):


    return render(request, 'base/topics.html')



def ArraysAndDateStructures(request):


    return render(request, 'base/ArraysAndDateStructures.html')
    
def twoPointers(request):


    return render(request, 'base/twoPointers.html')

def stacksAndQueues(request):


    return render(request, 'base/stacksAndQueues.html')





def binarySearch(request):


    return render(request, 'base/binarySearch.html')


def slidingWindow(request):


    return render(request, 'base/slidingWindow.html')

def linkedList(request):


    return render(request, 'base/linkedList.html')

def trees(request):


    return render(request, 'base/trees.html')

def tries(request):


    return render(request, 'base/tries.html')

def heaps(request):


    return render(request, 'base/heaps.html')


def backtracking(request):


    return render(request, 'base/backtracking.html')


def intervals(request):


    return render(request, 'base/intervals.html')


def greedy(request):


    return render(request, 'base/greedy.html')

def advancedGraphs(request):


    return render(request, 'base/advancedGraphs.html')

def graphs(request):


    return render(request, 'base/graphs.html')

def ddp(request):


    return render(request, 'base/ddp.html')

def ddptwo(request):


    return render(request, 'base/ddptwo.html')


def bitManipulation(request):


    return render(request, 'base/bitManipulation.html')


def mathAndgeometry(request):


    return render(request, 'base/mathAndgeometry.html')

    
def social_providers_page(request):
    return render(request, 'base/social_providers_page.html')


def subscribe(request):
    return render(request, 'base/subscribe.html')

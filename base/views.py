from django.shortcuts import render

def home(request):


    return render(request, 'base/home.html')



def about(request):


    return render(request, 'base/about.html')


def topics(request):


    return render(request, 'base/topics.html')
    
def social_providers_page(request):
    return render(request, 'base/social_providers_page.html')


def subscribe(request):
    return render(request, 'base/subscribe.html')

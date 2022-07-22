from django.shortcuts import render
from django.shortcuts import redirect
from rss.models import Actual,Newest,News,Show,Sport,Lifestyle,Tech,Viral
from rss.management.commands.rss import MODEL_NAMES



def home(request):
    actual = Actual.objects.all()
    context = {
        'ctx':actual
    }
    return render(request,'home.html',context)

def actual(request):
    actual = Actual.objects.all()
    context = {
        'ctx':actual
    }
    return render(request,'actual.html',context)

def newest(request):
    newest = Newest.objects.all()
    context = {
        'ctx':newest
    }
    return render(request,'newest.html',context)

def news(request):
    news = News.objects.all()
    context = {
        'ctx':news
    }
    return render(request,'news.html',context)

def show(request):
    show = Show.objects.all()
    context = {
        'ctx':show
    }
    return render(request,'show.html',context)

def sport(request):
    sports = Sport.objects.all()
    context = {
        'ctx':sports
    }
    return render(request,'sport.html',context)

def lifestyle(request):
    lifestyle = Lifestyle.objects.all()
    context = {
        'ctx':lifestyle
    }
    return render(request,'lifestyle.html',context)

def tech(request):
    tech = Tech.objects.all()
    context = {
        'ctx':tech
    }
    return render(request,'tech.html',context)

def viral(request):
    viral = Viral.objects.all()
    context = {
        'ctx':viral
    }
    return render(request,'viral.html',context)

def redirect_view(request):
    response = redirect('/home/actual/')
    return response

def search_result(request):
    rss_model = None
    if not request.META.get('HTTP_REFERER') == None:
        rss_model = request.META.get('HTTP_REFERER').split('/')[-2] # getting view name to map the model for search
        obj = MODEL_NAMES.get(str(rss_model))
        if not obj:
            return render(request,'search_result.html')
    else:
        return render(request,'search_result.html')
    if request.method == 'POST':
        searched = request.POST['searched']
        ids = obj.objects.filter(name__contains=searched)
        return render(request,'search_result.html',{'searched': searched, 'ids': ids})
    else:
        return render(request,'search_result.html')
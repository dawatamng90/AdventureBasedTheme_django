from django.http import HttpResponse
from django.shortcuts import render
from .forms import userForms
from service.models import Service
from news.models import News
from django.core.paginator import Paginator

def home(request):
    newsData = News.objects.all()
    servicesData = Service.objects.all().order_by('-service_title')
    data = {
        'servicesData':servicesData,
        'newsData':newsData
    }
    return render(request, "index.html", data)

def newsDetail(request,slug):
    
    newsDetail=News.objects.get(news_slug=slug)
    data={
        'newsDetail':newsDetail
    }
    return render(request, "newsdetails.html",data)


def about(request):
    return render(request, "about.html")


def services(request):
    #__icontains
    ServiceData = Service.objects.all()
    paginator=Paginator(ServiceData,2)
    page_number=request.GET.get('page')
    ServiceDatafinal=paginator.get_page(page_number)
    totalpage=ServiceDatafinal.paginator.num_pages
    # if request.method=="GET":
    #     st=request.GET.get('servicename')
    #     if st!=None:
    #         ServiceData = Service.objects.filter(service_title__icontains=st)
    data ={
        'servicesData':ServiceDatafinal,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, "services.html",data)


def contact(request):
    return render(request, "contact.html")

def saveEnquiry(request):
    return render(request, "contact.html")

def userform(request):
    finalans = 0
    fn = userForms()
    data = {'form': fn}
    try:
        if request.method == "POST":
            finalans = n1+n2
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            data = {
                'form': fn,
                'output': finalans
            }
    except:
        pass
    return render(request, "userform.html", data)


def calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1+n2
            elif opr == "-":
                c = n1-n2
            elif opr == "*":
                c = n1*n2
            elif opr == "/":
                c = n1/n2

    except:
        c = "Invalid Operator."

    return render(request, "calculator.html", {'c': c})


def marksheet(request):
    if request.method == "POST":
        s1 = eval(request.POST.get('subject1'))
        s2 = eval(request.POST.get('subject2'))
        s3 = eval(request.POST.get('subject3'))
        s4 = eval(request.POST.get('subject4'))
        s5 = eval(request.POST.get('subject5'))
        t = s1+s2+s3+s4+s5
        p = (t*100)/500
        if p >= 60:
            d = "First Div"
        elif p >= 48:
            d = "Second Div"
        elif p >= 35:
            d = "Third Div"
        else:
            d = "Fail"
        data = {
            'total': t,
            'percentage': p,
            'div': d
        }
        return render(request, "marksheet.html", data)

    return render(request, "marksheet.html")

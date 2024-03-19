from django.http import HttpResponse
from django.shortcuts import render
from .models import MyModel



def index(request):
    return render(request, 'message.html')


from django.core.paginator import Paginator


def my_view(request):
    my_queryset = MyModel.objects.all()
    paginator = Paginator(my_queryset, 25)  # показывать 25 объектов на странице
    page = request.GET.get('page')  # получить текущую страницу из параметров URL
    users = paginator.get_page(page)
    return render(request, 'chat.html', {'users': users})


def setcookie(request):
    html = HttpResponse("<h1>Hello</h1>")
    html.set_cookie('CookieName',
    'Hello this is your Cookies',
    max_age = None)
    return html


def showcookie(request):
    show = request.COOKIES.get('CookieName')
    if show:
        html = "Hello! {0}".format(show)
    else:
        html = "Cookie 'cookieName' is not set."
    return HttpResponse(html)

def set_cookie(request):
    html = HttpResponse("<h1>Мой сайт</h1>")
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
    else:
        visit_count = 1
    html.set_cookie('visit_count', str(visit_count))
    return html

def show_counter(request):
    visit_count = request.COOKIES.get('visit_count', '0')
    return render(request, 'counter.html', {'visit_count':
visit_count})



def deletecookie(request):
    html = HttpResponse("<h1>Hello</h1>")
    html.delete_cookie('visit_count')
    return html
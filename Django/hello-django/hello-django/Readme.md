Actions:
1) Create project (I do not have option to create app inside project)
2) (venv) PS D:\mygit\Python\Django\hello-django\hello-django> pip install django
3) (venv) PS D:\mygit\Python\Django\hello-django\hello-django> django-admin.exe startproject mysite
4) (venv) PS D:\mygit\Python\Django\hello-django\hello-django\mysite> django-admin startapp myapp
5) add myapp to settings.py (INSTALLED_APPS array)
6) (venv) PS D:\mygit\Python\Django\hello-django\hello-django\mysite> python manage.py runserver
7) check in browser: http://localhost:8000/
8) PERFORM migration : (venv) PS D:\mygit\Python\Django\hello-django\hello-django\mysite> python manage.py migrate (this will create db.sqlite3)
9) (venv) PS D:\mygit\Python\Django\hello-django\hello-django\mysite> python manage.py createsuperuser
10) Create templates folder in myapp folder
11) Inside templates folder create folder myapp (this is the name of the app)
12) Inside myapp folder create index.html
13) Add to index.html: <h1>Hello World</h1>
14) Add to views.py:
    from django.shortcuts import render

# Create your views here.
def index(request):
return render(request, 'index.html')

15) Copy urls.py from mysite folder to myapp folder
16) Inside myapp/urls.py add:
    from django.urls import path
    from . import views
    urlpatterns = [
    path('', views.index, name='index'),
    ]

17) Inside mysite/urls.py add:
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
    ]
18) Inside views.py add:
    from django.shortcuts import render

# Create your views here.
def index(request):
return render(request, 'myapp/index.html')


vuala - HOT RELOAD works by default:
check http://localhost:8000/
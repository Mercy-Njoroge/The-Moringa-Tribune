from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    date =dt.date.today()
    posts = Post.objects.all()
    return render(request, 'projects/index.html', {"date":date, "posts":posts })
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile
# Create your views here.
def index(request):
    date =dt.date.today()
    posts = Post.objects.all()
    return render(request, 'projects/index.html', {"date":date, "posts":posts })

@login_required(login_url='/accounts/login/?next=/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    posts = request.user.post_set.all()

    return render(request, 'projects/profile.html', locals())

@login_required(login_url='/accounts/login/?next=/')
def updateprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = current_user
            add.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'projects/profile_update.html',{"form":form })

@login_required(login_url='/accounts/login/?next=/')
def new_post(request):
        current_user = request.user
        if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('index')
        else:
                form = PostForm()
                return render(request,'projects/new_post.html', {"form":form})


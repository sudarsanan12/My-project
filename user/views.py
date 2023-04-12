from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm,LoginForm
from django.contrib import messages
from .models import Post, LikePost

# Create your views here.


def index(request):
    obj = Post.objects.all()
    return render(request,'index.html',{'data': obj})

def regis(request):
    
    if request.method == 'POST':
        
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/register')
        
        messages.error(request, 'Registration not complete')
    else:
        f = CustomUserCreationForm()

    return render(request, 'register.html', {'form': f})



def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/index')
        message = 'Invalid credinals!'
    return render(request, 'signin.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('/login')


def upload(request):
    
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image')
        caption = request.POST['title']
        desc = request.POST['description']
        new_post = Post.objects.create(user=user, image=image, caption=caption, desc= desc)
        new_post.save()
        if new_post:
            msg = "post updated successfully..."
            return render(request,'post_upload.html',context={'success':msg})

        else:
            return render(request,'post_upload.html')
    else:
        return render(request,'post_upload.html')
    


def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/index')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/index')

def delete(request):
    username = request.user.username
    id_no=request.GET.get('idn')
    obj = Post.objects.filter(id=id_no,user=username)
    if obj:
        obj.delete()
        return redirect('/index')
    else:
        return redirect('/index')
    
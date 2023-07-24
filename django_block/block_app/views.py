from django.shortcuts import render, redirect
from block_app.models import User, Post
from block_app.forms import UserModelForm, PostModelForm


def main_page(request):
    context = {'posts': Post.objects.all()}

    return render(request, 'mainPage.html', context)


def register(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserModelForm()

    context = {'forms': form}

    return render(request, 'register.html', context)


def login(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserModelForm()

    context = {'forms': form}

    return render(request, 'login.html', context)


def add_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostModelForm()

    context = {'forms': form}

    return render(request, 'addPost.html', context)

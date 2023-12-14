from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .form import *
from .models import * 

def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New category added')
            return redirect('all-categories')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('all-categories')
    else:
        form = CreateCategoryForm()
        context = {'form':form}
    return render(request, 'post/create_category.html', context)

def update_category(request, title):
    category = Category.objects.get(title=title)
    if request.method == 'POST':
        form = UpdateCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category information has been updated and saved')
            return redirect('all-categories')
            #return reverse("article_detail", args=[str(category.name)])
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return reverse("update-category", args=[str(category.title)])
    else:
        form = UpdateCategoryForm(instance=category)
        context = {'form':form}
    return render(request, 'post/update_category.html', context)

def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.author = request.user
            if not var.slug:
                var.slug = slugify(var.title)
            var.save()
            messages.success(request, 'New Post created.')
            return redirect('all-posts')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('create-post')
    else:
        form = CreatePostForm()
        context = {'form':form}
    return render(request, 'post/create_post.html', context)

def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            var = form.save(commit=False)
            var.slug = slugify(var.title)
            var.save()
            messages.success(request, 'Post content has been updated and saved')
            return redirect('all-posts')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return reverse("update-post", args=[str(post.slug)])
    else:
        form = UpdatePostForm(instance=post)
        context = {'form':form}
    return render(request, 'post/update_post.html', context)

def all_categories(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'post/all_categories.html', context)

def all_posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'post/all_posts.html', context)

def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'post/post_details.html', context)

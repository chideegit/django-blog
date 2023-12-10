from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Post

@login_required
def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)

def website(request):
    posts = Post.objects.filter(is_published=True)
    context = {'posts':posts}
    return render(request, 'dashboard/website.html', context)
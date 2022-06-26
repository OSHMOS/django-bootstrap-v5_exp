from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'exp/post_form.html', {'form': form})

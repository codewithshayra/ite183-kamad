from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def blog_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/post/')
    context = {
        "form": form,
        'form_type': 'Create'
    }
    return render(request, "blog/blog_create.html", context)


def blog_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/post/')
    context = {
        "form": form,
        'form_type': 'Update'
    }
    return render(request, "blog/blog_create.html", context)


def blog_list(request):
    post = Post.objects.all().order_by('-publish_date')  # Order by publish_date
    context = {
        'blog_list': post
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, id):
    each_post = Post.objects.get(id=id)
    context = {
        'blog_detail': each_post
    }
    return render(request, "blog/blog_detail.html", context)


def blog_delete(request, id):
    each_post = Post.objects.get(id=id)
    each_post.delete()
    return HttpResponseRedirect('/post/')


def vote_blog(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        vote_type = request.POST.get('vote_type')

        if vote_type == 'upvote':
            post.upvotes += 1
        elif vote_type == 'downvote':
            post.downvotes += 1
        else:
            # If no valid vote_type is provided
            return HttpResponseBadRequest("Invalid vote type.")

        post.save()
        return redirect('/post/', id=post.id)

    return HttpResponseBadRequest("Invalid request method.")
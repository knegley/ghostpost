from django.shortcuts import render, HttpResponseRedirect, reverse
from ghost_post_app.forms import AddPost
from ghost_post_app.models import Post
# Create your views here.


def add_post_view(request):
    form = AddPost()
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            Post.objects.create(post=data.get(
                "post"), boast_or_roast_choice=data.get("boast_or_roast_choice"))

            return HttpResponseRedirect(redirect_to=reverse("home"))

    return render(request, "add_post_form.html", {"form": form})


def home_view(request):
    posts = Post.objects.all()[::-1]
    return render(request, "home.html", {"posts": posts})


def boast_view(request):
    boasts = [post for post in Post.objects.all(
    ) if post.boast_or_roast_choice == "B"][::-1]
    # boasts = Post.objects.filter(boast_or_roast_choice="B")
    return render(request, "boast_posts.html", {"boasts": boasts})


def roast_view(request):
    roasts = [post for post in Post.objects.all(
    ) if post.boast_or_roast_choice == "R"][::-1]
    # roasts = Post.objects.filter(boast_or_roast_choice="R")
    return render(request, "roast_posts.html", {"roasts": roasts})


def sorted_view(request):

    posts = sorted(Post.objects.all(),
                   key=lambda x: x.vote_total(), reverse=True)

    return render(request, "sorted.html", {"posts": posts})


def vote_view(request, post_id, vote_value):

    post = Post.objects.filter(id=post_id)
    up_vote_total = post.first().up_vote
    down_vote_total = post.first().down_vote
    vote_incrementer = -1 if not vote_value else vote_value

    if vote_incrementer < 0:
        post.update(down_vote=(down_vote_total+vote_incrementer))
    else:
        post.update(up_vote=(up_vote_total+vote_incrementer))

    # vote_total = post.first().vote_total()

    # post.update(vote_total=vote_total)
    # print(request)

    return HttpResponseRedirect(redirect_to=reverse("home"))

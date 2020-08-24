from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from ghostpost_app.models import BoastsRoastsModel
from ghostpost_app.forms import AddPostForm

# https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys/16630719#16630719
from django.core.management.utils import get_random_secret_key

# Create your views here.
# Homepage that displays boasts and roasts, sorted by time submitted (hint --> https://docs.djangoproject.com/en/3.0/ref/models/querysets/#order-by (Links to an external site.)Links to an external site.)


def index_view(request):
    posts = BoastsRoastsModel.objects.filter().order_by('-post_datetime')
    return render(request, 'index.html', {'page_title': 'GhostPost: Homepage', 'posts': posts})


def addpost_view(request):
    if request.method == "POST":
        addpost_form = AddPostForm(request.POST)
        if addpost_form.is_valid():
            addform_data = addpost_form.cleaned_data
            private_key = get_random_secret_key()  # https://tech.serhatteker.com/post/2020-01/django-create-secret-key/
            post = BoastsRoastsModel.objects.create(
                is_boast=addform_data.get('is_boast'),
                post_content=addform_data.get('post_content'),
                privatesecret_key=private_key
            )
            return render(request, 'addpost.html', {'page_title': 'GhostPost', 'post': post})
        addpost_form = AddPostForm()
        return render(request, 'addpost.html', {'page_title': 'GhostPost: Posting Form', 'addpost_form': addpost_form})


def boasts_view(request):
    boasts = BoastsRoastsModel.objects.filter(is_boast=True).order_by('-post_datetime')
    return render(request, 'boasts.html', {'page_title': 'GhostPost: The Boasts', 'boasts': boasts})


def roasts_view(request):
    roasts = BoastsRoastsModel.objects.filter(is_boast=False).order_by('-post_datetime')
    return render(request, 'roasts.html', {'page_title': 'GhostPost: The Roasts', 'roasts': roasts})


def upvote_view(request, upvote_id):
    upvote = BoastsRoastsModel.objects.get(id=upvote_id)
    upvote.upvotes += 1
    upvote.save()
    return redirect('/')


def downvote_view(request, downvote_id):
    downvote = BoastsRoastsModel.objects.get(id=downvote_id)
    downvote.downvotes += 1
    downvote.save()
    return redirect('/')


# https://docs.python.org/3/howto/sorting.html
def sortbyvotescore_view(request):
    sorted_votes = sorted(BoastsRoastsModel.objects.all(), key=lambda sorted_votes: sorted_votes.vote_score, reverse=True)
    return render(request, 'sortedvotes.html', {'page_title': 'GhostPost: Sorted Posts By Vote Score', 'sorted_votes': sorted_votes})


"""
Add a post deletion method that works for both boasts and roasts on the detail page. "Wait, how will we delete if it's anonymous?", I hear you ask. When a boast or a roast is created, it should have a random 6 character string associated with it (so that it's hard to guess). Every post now has two URLs... but one is public and one is private. For example, a valid post could have these two URLs:
localhost:8000/posts/1
localhost:8000/posts/abcdef
The one that ends in an ID should display a "public" version of the detail page; just the post itself. The one that ends in the "secret key" should be the same content, but with an additional button that allows you to delete the content. (Hint: have the button link to a different view that can delete a post by ID)
When the object is created, the magic string should be passed back to the front end in a link and given to the user; something like "Keep this link secure; this is your private link for managing this post!"
"""


def delete_view(request, deletepost_id):
    BoastsRoastsModel.objects.filter(id=deletepost_id).delete()
    return redirect('/')


def privatepost_view(request, ps_key):
    private_post = BoastsRoastsModel.objects.get(privatesecret_key=ps_key)
    return render(request, 'privatepost.html', {{'page_title': 'GhostPost: Private Post', 'private_post': private_post}})

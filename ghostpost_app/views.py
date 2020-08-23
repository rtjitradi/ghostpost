from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from ghostpost_app.models import BoastsRoastsModel
from ghostpost_app.forms import AddPostForm

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
            BoastsRoastsModel.objects.create(
                is_boast=addform_data.get('is_boast'),
                post_content=addform_data.get('post_content')
            )
            return HttpResponseRedirect(reverse('homepage'))
        addpost_form = AddPostForm()
        return render(request, 'addpost.html', {'page_title': 'GhostPost: Post Boast or Roast Form', 'addpost_form': addpost_form})


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

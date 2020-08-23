from django.db import models
from django.utils import timezone

"""
One model to represent both boasts and roasts
-Boolean to tell whether it's a boast or a roast
-CharField to put the content of the post in
-IntegerField for up votes
-IntegerField for down votes
-DateTimeField for submission time

Add a post deletion method that works for both boasts and roasts on the detail page. "Wait, how will we delete if it's anonymous?", I hear you ask. When a boast or a roast is created, it should have a random 6 character string associated with it (so that it's hard to guess). Every post now has two URLs... but one is public and one is private. For example, a valid post could have these two URLs:
localhost:8000/posts/1
localhost:8000/posts/abcdef
The one that ends in an ID should display a "public" version of the detail page; just the post itself. The one that ends in the "secret key" should be the same content, but with an additional button that allows you to delete the content. (Hint: have the button link to a different view that can delete a post by ID)
When the object is created, the magic string should be passed back to the front end in a link and given to the user; something like "Keep this link secure; this is your private link for managing this post!"
"""
# Create your models here.
# Attended Study Hall and was working together with Sohail, Kevin, and Joanna (we finished it separately)


class BoastsRoastsModel(models.Model):
    # Thanks Joe for the guidance (shared with the group at study hall), refer to https://docs.djangoproject.com/en/3.1/ref/models/fields/
    is_boast = models.BooleanField()
    post_content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    post_datetime = models.DateTimeField(default=timezone.now)
    privatesecret_key= models.CharField(max_length=50) # https://docs.djangoproject.com/en/3.0/ref/settings/ and also refer to https://stackoverflow.com/questions/40856593/django-secret-key-settings

    def __str__(self):
        return self.post_content

    # Ability to sort content based on vote score (hint: you may need to calculate the vote score)
    # https://docs.python.org/3/library/functions.html#property
    @property
    def vote_score(self):
        vote_total = self.upvote - self.downvote
        return vote_total

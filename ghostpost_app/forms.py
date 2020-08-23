from django import forms


# https://docs.djangoproject.com/en/3.1/ref/models/fields/
class AddPostForm(forms.ModelForm):
    BOAST_OR_ROAST_CHOICES = [(True, 'boast'), (False, 'roast')]
    is_boast = forms.ChoiceField(choices=BOAST_OR_ROAST_CHOICES)
    post_content = forms.CharField(max_length=280)

from django import forms

from twitteruser.models import TwitterUser


class TweetsForm(forms.Form):

    message = forms.CharField(max_length=140)
    author = forms.ModelChoiceField(queryset=TwitterUser.objects.all())


# class AddTweetForm(forms.Form):

#     text = forms.CharField(widget=forms.Textarea)

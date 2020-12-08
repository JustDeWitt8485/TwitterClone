
from django.shortcuts import HttpResponseRedirect, render, reverse

from .forms import TweetsForm

from tweet.models import Tweets

# Create your views here.


def add_tweet(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = TweetsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweets.objects.create(
                message=data['message'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = TweetsForm()
    return render(request, html, {'form': form})





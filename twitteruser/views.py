from authentication.views import login_view, logout_view


from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render, reverse, redirect

from tweet.models import Tweets
from tweet.views import add_tweet

from twitteruser.forms import SignUpForm
from twitteruser.models import TwitterUser

# Create your views here.


@login_required
def index(request):
    html = 'index.html'
    tweets = Tweets.objects.all().order_by('publish_date')
    context = {'tweets': tweets}
    return render(request, html, context)


def profile_view(request, author_id):
    html = 'profile.html'
    the_author = TwitterUser.objects.get(id=author_id)
    tweets = Tweets.objects.filter(author=the_author).order_by('publish_date')
    total_follows = the_author.total_follows()
    context = {'author': the_author, 'tweets': tweets, 'total_follows': total_follows}
    return render(request, html, context)


def follow_view(request, author_id):
    fol = TwitterUser.objects.get(id=author_id)
    fol.follow.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))


def tweet_view(request, tweet_id):
    html = 'tweet.html'
    tweets = Tweets.objects.filter(id=tweet_id).order_by('publish_date')
    context = {'tweets': tweets}
    return render(request, html, context)


def sign_up(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create_user(
                username=data['username'],
                name=data['name'],
                email=data['email'],
                password=data['password'],
            )
        
            return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, html, {'form': form})

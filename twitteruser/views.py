from authentication.views import login_view, logout_view


from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, render, reverse

from tweet.models import Tweets
from tweet.views import add_tweet

from twitteruser.forms import SignUpForm
from twitteruser.models import TwitterUser

# Create your views here.


def index(request):
    html = 'index.html'
    tweets = Tweets.objects.all().order_by('publish_date')
    return render(request, html, {'tweets': tweets})


def profile_view(request, author_id):
    the_author = TwitterUser.objects.get(id=author_id)
    return render(
        request, 'profile.html', {'author': the_author}
    )


def sign_up(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            TwitterUser.objects.create(
                user=new_user,
                name=data['name'],
                email=data['email'],
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, html, {'form': form})

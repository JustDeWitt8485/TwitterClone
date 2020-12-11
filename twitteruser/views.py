from authentication.views import LoginView, logout_view


from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, render, reverse, redirect
from django.views.generic import TemplateView, View

from tweet.models import Tweets
from tweet.views import add_tweet

from twitteruser.forms import SignUpForm
from twitteruser.models import TwitterUser

# Create your views here.


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        html = 'index.html'
        tweets = Tweets.objects.all().order_by('publish_date')
        context = {'tweets': tweets}
        return render(request, html, context)


# def profile_view(request, author_id):
#     html = 'profile.html'
#     the_author = TwitterUser.objects.get(id=author_id)
#     tweets = Tweets.objects.filter(author=the_author).order_by('publish_date')
#     total_follows = the_author.total_follows()
#     context = {'author': the_author, 'tweets': tweets, 'total_follows': total_follows}
#     return render(request, html, context)


def follow_view(request, author_id):
    fol = TwitterUser.objects.get(id=author_id)
    fol.follow.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))


def tweet_view(request, tweet_id):
    html = 'tweet.html'
    tweets = Tweets.objects.filter(id=tweet_id).order_by('publish_date')
    context = {'tweets': tweets}
    return render(request, html, context)


# def profile_view(request, author_id):
#     the_author = TwitterUser.objects.get(id=author_id)
#     return render(
#         request, 'profile.html', {'author': the_author}
#     )


class ProfileView(View):
    def get(self, request, author_id):
        html = 'profile.html'
        the_author = TwitterUser.objects.get(id=author_id)
        tweets = Tweets.objects.filter(author=the_author).order_by('publish_date')
        total_follows = the_author.total_follows()
        context = {'author': the_author, 'tweets': tweets, 'total_follows': total_follows}
        return render(request, html, context)


# def sign_up(request):
#     html = 'generic_form.html'
#     form = SignUpForm()

#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_user = TwitterUser.objects.create_user(
#                 username=data['username'],
#                 password=data['password'],
#             )
#             TwitterUser.objects.create(
#                 user=new_user,
#                 name=data['name'],
#                 email=data['email'],
#             )
#             return HttpResponseRedirect(reverse('homepage'))

#     return render(request, html, {'form': form})


class SignUp(View):

    form_class = SignUpForm

    def get(self, request):
        html = 'generic_form.html'
        form = self.form_class
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create_user(
                username=data['username'],
                name=data['name'],
                email=data['email'],
                password=data['password'],
            )
            return HttpResponseRedirect(reverse('homepage'))

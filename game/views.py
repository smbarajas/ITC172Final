from django.shortcuts import render, get_object_or_404
from .models import Review, GameGenre
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'game/index.html')

def resources (request):
    type_list=Resource.objects.all()
    return render (request, 'game/reviews.html', {'type_list': type_list})

def meetings (request):
    meetings_list = Games.objects.all()
    return render (request, 'game/games.html', {'games_list': games_list})

def gamedetail (request, id):
    detail = get_object_or_404(Meeting, pk=id)
    context = {'detail': detail}
    return render (request, 'game/gamedetails.html', context=context)

# review form view
@login_required
def newResource(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'game/newreview.html', {'form': form})


#login/logout functionality
def loginmessage(request):
    return render(request, 'game/loginmessage.html')

def logoutmessage(request):
    return render(request, 'game/logoutmessage.html')
from django.shortcuts import render, get_object_or_404, redirect
from .forms import GameForm
from .models import Game, Collection

# Create your views here.


def home(request):
    collections = Collection.objects.all()
    # use the django ORM to get all instances of Game
    return render(request, 'index.html', {'collections': collections})


def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    return render(
        request,
        'collection_detail.html',
        {'collection': collection}
    )


def create_game(request, coll_pk):
    collection = get_object_or_404(Collection, pk=coll_pk)
    if request.method == 'POST':
        form = GameForm(request.POST)
        new_game = form.save(commit=False)
        new_game.collection = collection
        new_game.save()
        return redirect('home')
    form = GameForm()
    return render(request, 'create_game.html', {'form': form})

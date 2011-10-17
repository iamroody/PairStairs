from pairstairs.models import Programmer, Pair
from django.shortcuts import render_to_response

def index(request):
    pairs = Pair.objects.all()
    programmers = Programmer.objects.all()
    return render_to_response('pairstairs/index.html', {
        'programmers': programmers,
        'pairs': pairs,
        })


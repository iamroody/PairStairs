from django.template.context import RequestContext
from pairstairs.models import Programmer, Pair
from django.shortcuts import render_to_response, redirect

def stairs(request):
    pairs = Pair.objects.all()
    programmers = Programmer.objects.all()
    print programmers.count()
    return render_to_response('pairstairs/index.html', {
        'programmers': programmers,
        'pairs': pairs,
        })

def add(request):
    if request.method == 'POST':
        names = request.POST['programmer_names'].split(',')
        for name in names:
            Programmer(name= name).save()
        return redirect(stairs)
    return render_to_response("pairstairs/add.html", RequestContext(request))


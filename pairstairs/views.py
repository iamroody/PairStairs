from django.template.context import RequestContext
from pairstairs.models import Programmer, Pair
from django.shortcuts import render_to_response, redirect

def create_matrix(pairs, programmers):
    pass


def stairs(request):
    pairs = list(Pair.objects.all())
    programmers = list(Programmer.objects.all())
    return render_to_response('pairstairs/index.html', RequestContext(request,
            {'programmers':programmers,
             'programmers_for_columns': programmers[0:-1],
             'programmers_for_rows': programmers[1:]}))

def add(request):
    if request.method == 'POST':
        names = request.POST['programmer_names'].split(',')
        for name in names:
            Programmer(name= name).save()
        return redirect(stairs)
    return render_to_response("pairstairs/add.html", RequestContext(request))


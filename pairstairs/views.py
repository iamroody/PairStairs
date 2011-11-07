from django.template.context import RequestContext
from pairstairs.models import Programmer, Pair
from django.shortcuts import render_to_response, redirect

def create_pair_matrix(programmers):
    pairs = []
    for programmer in programmers[1:]:
        for programmer_1 in programmers[0:-1]:
            if programmer != programmer_1:
                try:
                    pairs.append(Pair.objects.get(programmer_1 = programmer, programmer_2 = programmer_1))
                except :
                    pairs.append(Pair(programmer_1=programmer, programmer_2=programmer_1, count = 0))
            else:
                break
    return pairs

def stairs(request):
    programmers = Programmer.objects.all()
    programmers_list = list(programmers)
    pair_matrix = create_pair_matrix(programmers_list)
    return render_to_response('pairstairs/index.html', RequestContext(request,
            {'programmers':programmers,
             'pair_matrix':pair_matrix,
             'programmers_for_columns': programmers_list[0:-1],
             'programmers_for_rows': programmers_list[1:]}))

def reset(request):
    Pair.objects.all().delete()
    Programmer.objects.all().delete()
    return redirect(stairs)

def add(request):
    if request.method == 'POST':
        names = request.POST['programmer_names'].split(',')
        for name in names:
            Programmer(name= name).save()
        return redirect(stairs)
    return render_to_response("pairstairs/add.html", RequestContext(request))

def add_count(request, firstMember_id, secondMember_id):
    programmer1 = Programmer.objects.get(id=firstMember_id)
    programmer2 = Programmer.objects.get(id=secondMember_id)
    try:
        pair = Pair.objects.get(programmer_1 = programmer1, programmer_2 = programmer2)
        pair.count += 1
        pair.save()
    except :
        Pair(programmer_1 = programmer1, programmer_2 = programmer2, count = 1).save()
    return redirect(stairs)

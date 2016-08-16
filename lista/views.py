from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Item
from .forms import donorForm
from django.shortcuts import redirect
from django.db.models import Q
from random import randint
from django.template import RequestContext


# Create your views here.
def items_list(request, choice=None):
    if choice=='notbooked':
         items = Item.objects.filter(Q(donor__exact='') | Q(donor__isnull=True))
    elif choice=='booked':
        items = Item.objects.exclude(donor__exact='').exclude(donor__isnull=True)
    elif choice=='random':
        random_index = randint(0,Item.objects.count() - 1)
        random_el = Item.objects.all()[random_index]
        items =[]
        items.append(random_el)
    else: items = Item.objects.all()
    return render(request,'items_list.html',{'items':items})
    


def donate(request,pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = donorForm(request.POST,instance=item)
        if form.is_valid():
            item=form.save(commit=False)
            item.save()
            return redirect('items_list')
    else:
        form = donorForm()
    return render(request, 'donor.html', {'item': item, 'form':form})

def info(request):
    return render(request,'info.html')
    
    
def bad_request(request):
    response = render_to_response(
        '400.html',
        context_instance=RequestContext(request)
    )
    
    response.status_code = 400
    
    return response
from django.shortcuts import render, get_object_or_404
from .models import Item
from .forms import donorForm
from django.shortcuts import redirect
from django.db.models import Q

# Create your views here.
def items_list(request, choice=None):
    if choice=='notBooked':
         items = Item.objects.filter(Q(donor__exact='') | Q(donor__isnull=True))
         #items = Item.objects.filter(donor__exact='')
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
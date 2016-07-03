from django.shortcuts import render, get_object_or_404
from .models import Item
from .forms import donorForm
from django.shortcuts import redirect

# Create your views here.
def items_list(request):
    items = Item.objects.all()
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
from django.shortcuts import render
from .models import Item

# Create your views here.
def items_list(request):
    items = Item.objects.all()
    return render(request,'items_list.html',{'items':items})

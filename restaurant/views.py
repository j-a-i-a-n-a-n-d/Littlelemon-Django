# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)


def menu(request):
    menu_data = Menu.objects.all()
    main_data = dict()
    main_data = {"menu": menu_data}
    print(main_data)
    return render(request, 'menu.html', main_data)


def displayMenuItems(request, pk):
    if pk:
        menu_ = Menu.objects.get(pk=pk)
        menu_items = dict()
        menu_items = {"menu_item": menu_}
    else:
        menu_items = {}
    print(menu_items, " ", menu_items["menu_item"])
    return render(request, 'menu_items.html', menu_items)

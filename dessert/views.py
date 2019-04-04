from django.shortcuts import render

# Create your views here.
def dessert(request):
    return render(request, "dessert.html")
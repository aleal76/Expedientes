from django.shortcuts import render

# Create your views here.
def exptes_list(request):
    return render(request, 'exptes/exptes_list.html')
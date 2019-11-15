from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,"index.html")


def display(request):
    team=request.POST.getlist('checks[]')
    dict={"palyers":team}
    return render(request,"team.html",dict)

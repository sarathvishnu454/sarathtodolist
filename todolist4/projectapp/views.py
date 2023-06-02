from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .forms import updateform
from .models import todolist


def index(request):
    return HttpResponse("Hello World")
def html1(request):
    if request.method=="POST":
        name=request.POST.get("todo",)
        date=request.POST.get("date",)
        priority=request.POST.get("priority")
        m=todolist(name=name,date=date,priority=priority)
        m.save()
        return redirect("/")
    a = todolist.objects.all()
    return render(request, "html2.html", {'a': a})
# def index1(request):
#     return render(request,'html2.html')

def updatehtml(request, id):
    c = todolist.objects.get(id=id)
    form = updateform(request.POST or None, request.FILES, instance=c)
    if form.is_valid():
        form.save()
        return redirect('html1')
    else:
        form = updateform(instance=c)
    return render(request, 'update.html', {'c': c, 'form': form})

def delete(request, id):
    if request.method == "POST":
        d = todolist.objects.get(id=id)
        d.delete()
        return redirect("html1")
    return render(request, "delete.html")
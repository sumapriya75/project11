from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,"sample.html")

def demo(request):
    return render(request,"demo.html")
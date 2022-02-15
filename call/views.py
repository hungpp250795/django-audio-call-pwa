from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def call_demo(request):
    return render(request, 'call-demo.html')
def staff(request):
    return render(request, 'staff.html')
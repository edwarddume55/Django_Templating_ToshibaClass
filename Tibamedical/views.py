from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def inner(request):
    return  render(request, 'inner-page.html')

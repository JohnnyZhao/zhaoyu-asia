from django.shortcuts import render_to_response as render

def home(request):
    return render('mysite/home.html', {})

from django.shortcuts import render

def timetable_view(request):
    return render(request, 'home.html')

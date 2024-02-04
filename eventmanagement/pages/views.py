from django.shortcuts import render
from events.models import Event

# Create your views here.
def index(request):
    events = Event.objects.order_by('event_date').filter(is_published=True)[:3]

    context = {
        'events' : events,
    }
    return render(request,'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html')
from django.shortcuts import render, redirect
from .models import Participant
from django.contrib import messages 

# Create your views here.
def participant(request):
    if request.method == 'POST':
        event_id = request.POST['event_id']
        event = request.POST['event']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_participated = Participant.objects.all().filter(event_id=event_id,user_id=user_id)
            if has_participated:
                messages.error(request, 'You have already registered for the event')
                return redirect('/events/' + event_id)

        participant = Participant(event_id=event_id,event=event,name=name,email=email,phone=phone,message=message,user_id=user_id)
        participant.save()

        messages.success(request, 'You have successfully registered for the event')

        return redirect('/events/'+ event_id)


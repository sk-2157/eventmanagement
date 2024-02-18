import base64
from django.shortcuts import render, redirect
from .models import Participant
from django.contrib import messages 
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def participant(request):
    if request.method == 'POST':
        event_id = request.POST['event_id']
        event = request.POST['event']
        name = request.POST['name']
        email = request.POST['email']
        #phone = request.POST['phone']
        user_id = request.POST['user_id']
        captured_image_data_url = request.POST.get('captured_image')
        captured_image_path = f'media/{event}/{name}.png'
        with open(captured_image_path, 'wb') as destination:
            destination.write(base64.b64decode(captured_image_data_url.split(',')[1]))



        if request.user.is_authenticated:
            user_id = request.user.id
            has_participated = Participant.objects.all().filter(event_id=event_id,user_id=user_id)
            if has_participated:
                messages.error(request, 'You have already registered for the event')
                return redirect('/events/' + event_id)

        participant = Participant(event_id=event_id,event=event,name=name,email=email,user_id=user_id,p_photo=captured_image_path)
        participant.save()

        messages.success(request, 'You have successfully registered for the event')

        return redirect('/events/'+ event_id)


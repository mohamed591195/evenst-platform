from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .serializers import EventSerializer
from .models import Event
from .forms import AddEventForm
import json


class HomeView(TemplateView):
    template_name = 'main/home.html'

    
class ListOwnedEventsView(LoginRequiredMixin, TemplateView):
    template_name = 'main/home.html'


class ListJoinedEventsView(LoginRequiredMixin, TemplateView):
    template_name = 'main/home.html'


class EventsSetPagination(PageNumberPagination):
    page_size = 8
    

class ListEventsView(ListAPIView):
    serializer_class = EventSerializer
    pagination_class = EventsSetPagination

    def get_queryset(self):

        user = self.request.user

        if user.is_authenticated:

            if self.request.GET.get('requestJoined'):
                return user.events_joined.all()

            elif self.request.GET.get('requestOwned'):
                return user.events_created.all()

        return Event.objects.all()


class CreateUpdateEventView(LoginRequiredMixin, FormView):

    form_class = AddEventForm
    template_name = 'main/create_event.html'

    success_url = reverse_lazy('owned_events_view')
   
    def get_form_kwargs(self):
        
        kwargs = super().get_form_kwargs()

        event_id = self.kwargs.get('event_id')

        if event_id:
            event = Event.objects.filter(id=event_id, owner=self.request.user).first()
            kwargs.update({'instance': event})

        return kwargs
        
    def form_valid(self, form):

        event_obj = form.save(commit=False)
        event_obj.owner = self.request.user
        event_obj.save()

        return super().form_valid(form)


@login_required
def attend_event(request):

    user = request.user

    if request.method == 'POST':

        event_id = request.POST.get('eventId')
        event = Event.objects.filter(id=event_id).first()

        action = ''

        if event:
            if user in event.participants.all():
                event.participants.remove(user)
                action = 'removed'
            else:
                event.participants.add(user)
                action = 'added'
            
            return JsonResponse({'action': action}, status=status.HTTP_202_ACCEPTED)
    
    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)


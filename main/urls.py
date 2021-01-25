from django.urls import path
from .views import (
    ListEventsView,
    HomeView,
    ListOwnedEventsView,
    ListJoinedEventsView,
    CreateUpdateEventView,
    attend_event
)

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('my-events/', ListOwnedEventsView.as_view(), name='owned_events_view'),
    path('joined-events/', ListJoinedEventsView.as_view(), name='joined_events_view'),
    path('add-event/', CreateUpdateEventView.as_view(), name='create_event_view'),
    path('edit-event/<int:event_id>/', CreateUpdateEventView.as_view(), name='edit_event_view'),
]


# ajax-paths
urlpatterns += [
    path('events-serialized/', ListEventsView.as_view()),
    path('attend-event/', attend_event)
]
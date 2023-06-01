from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('inscription', views.inscription, name='inscription'),
    path('saveParticipant', views.saveParticipant, name='saveParticipant'),
    path('updateParticipant/<int:id>', views.updateParticipant, name='updateParticipant'),
    path('deleteParticipant/<int:id>', views.deleteParticipant, name='deleteParticipant')




]
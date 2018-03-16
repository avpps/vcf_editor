from django.conf.urls import url

from editor import views

app_name = 'editor'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^load_cards/$', views.load_cards, name='load_cards'),
    url(r'^modify_card/$', views.modify_card, name='modify_card'),
    url(r'^delete_card/$', views.delete_card, name='delete_card'),
]

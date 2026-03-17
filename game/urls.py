from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('monster/work08/', views.Work08View.as_view(), name="monster_work08"),
    path('monster/work09/', views.Work09View.as_view(), name="monster_work09"),
    path('monster/work10/', views.Work10View.as_view(), name="monster_work10"),
    path('monster/work11/', views.Work11View.as_view(), name="monster_work11"),
    path('monster/work12/', views.Work12View.as_view(), name="monster_work12"),
    path('monster/work13/', views.Work13View.as_view(), name="monster_work13"),
    path('monster/work14/', views.Work14View.as_view(), name="monster_work14"),
    path('player/list/', views.PlayerListView.as_view(), name="player_list"),
    path('job/list/', views.JobListView.as_view(), name="job_list"),
    path('player/create/', views.PlayerCreateView.as_view(), name="player_create"),
    path('character/list/', views.CharacterListView.as_view(), name="character_list"),
    path('weapon/list/', views.WeaponListView.as_view(), name="weapon_list"),
    path('user/list/', views.UserListView.as_view(), name="user_list"),
    path('user/create/', views.UserCreateView.as_view(), name="user_create"),
]
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard sections
    path('', views.Map.as_view(), name='map'),
    path('specificmaps', views.MapsList.as_view(), name='mapslist'),
    path('dashboard', views.mainDashboard.as_view(), name='dashboard'),
    path('specificdashboards', views.DashboardsList.as_view(), name='dashboardslist'),

    # Forms
    path('addpostion', views.CreatePosition.as_view(), name='addpin'),
    path('adddamage', views.CreateDamage.as_view(), name='addarea'),

    # Detail views
    path('position/<slug:pk>/', views.PositionDetail.as_view(), name='position'),
    path('damages/<slug:pk>/', views.DamageDetail.as_view(), name='damage'),

    # List views
    # path('mypositions', views.myPositions.as_view(), name='myPositions'),
    # path('mydamages', views.myDamages.as_view(), name='myDamages'),

    # Update views
    path('updateposition/<slug:pk>/', views.UpdatePosition.as_view(), name='updatePosition'),
    path('updatedamage/<slug:pk>/', views.UpdateDamage.as_view(), name='updateDamage'),
    path('updateneedstatus/<slug:pk>/', views.UpdateNeedStatus.as_view(), name='updateNeedStatus'),

    # Delete views
    path('deleteposition/<slug:pk>/', views.DeletePosition.as_view(), name='deletePosition'),
    path('deletedamage/<slug:pk>/', views.DeleteDamage.as_view(), name='deleteDamage'),
    path('deleteneed/<slug:pk>/', views.DeleteNeed.as_view(), name='deleteNeed'),
    
    # Data
    path('areas', views.Areas.as_view()),
    path('positions', views.Positions.as_view()),
    path('damages', views.Damages.as_view()),

    # User specific views
    path('<str:username>/dashboard/', views.userDashboard.as_view(), name='userDashboard'),
    
    # Development
    path('map', views.FullScreenMap.as_view())
]
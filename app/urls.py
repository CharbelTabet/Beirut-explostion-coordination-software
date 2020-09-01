from django.urls import path
from . import views

urlpatterns = [
    # Map views
    path('', views.Map.as_view(), name='map'),
    path('mapslist', views.MapsList.as_view(), name='mapslist'),

    # Dashboard views
    path('dashboard', views.mainDashboard.as_view(), name='dashboard'),
    path('<str:username>/dashboard/', views.userDashboard.as_view(), name='userDashboard'),
    path('dashboardslist', views.DashboardsList.as_view(), name='dashboardslist'),

    # Create views
    path('addpostion', views.CreatePosition.as_view(), name='addpin'),
    path('adddamage', views.CreateDamage.as_view(), name='addarea'),

    # Read views
    path('position/<slug:pk>/', views.PositionDetail.as_view(), name='position'),
    path('damages/<slug:pk>/', views.DamageDetail.as_view(), name='damage'),

    # Update views
    path('position/update/<slug:pk>/', views.UpdatePosition.as_view(), name='updatePosition'),
    path('damage/update/<slug:pk>/', views.UpdateDamage.as_view(), name='updateDamage'),
    path('needstatus/update/<slug:pk>/', views.UpdateNeedStatus.as_view(), name='updateNeedStatus'),

    # Delete views
    path('position/delete/<slug:pk>/', views.DeletePosition.as_view(), name='deletePosition'),
    path('damage/delete/<slug:pk>/', views.DeleteDamage.as_view(), name='deleteDamage'),
    path('need/delete/<slug:pk>/', views.DeleteNeed.as_view(), name='deleteNeed'),
    
    # Data
    path('areas', views.Areas.as_view()),
    path('positions', views.Positions.as_view()),
    path('damages', views.Damages.as_view()),

    # User specific views
]
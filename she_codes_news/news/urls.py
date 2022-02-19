from django.urls import path
from . import views
from .views import UpdateStoryView, DeletePostView


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/edit-story', views.UpdateStoryView.as_view(), name='editstory'),
    path('catergory/<str:catergory>', views.CatergoryView.as_view(), name= 'catergory'),
    path('<int:pk>/deletestory', views.DeletePostView.as_view(), name='deletestory'),
]

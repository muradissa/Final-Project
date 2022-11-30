from django.urls import path
from .views import CreatAnchorsView, CreatWallView, EnterParametersView, main, startSimulation
from .views import AnchorView,WallView

urlpatterns = [
    path('', main),
    path('anchors', AnchorView.as_view()),
    path('wall', WallView.as_view()),
    path('create-wall',CreatWallView.as_view()),
    path('create-anchors',CreatAnchorsView.as_view()),
    path('enter-parameter',EnterParametersView.as_view()),
    path('start',startSimulation.as_view()),
    #path('start',CreatWallView.as_view()),
   
]
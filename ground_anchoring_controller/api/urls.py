from django.urls import path
from .views import CreatAnchorsView, CreatWallView, EnterParametersView, getHighMoment, main, simulationQuality, startSimulation ,getImage
from .views import AnchorView,WallView

urlpatterns = [
    path('', main),
    path('anchors', AnchorView.as_view()),
    path('wall', WallView.as_view()),
    path('create-wall',CreatWallView.as_view()),
    path('create-anchors',CreatAnchorsView.as_view()),
    path('enter-parameter',EnterParametersView.as_view()),
    path('start',startSimulation.as_view()),
    path('quality',simulationQuality.as_view()),
    path('high-moment',getHighMoment.as_view()),
    path('plot-moment',getImage.as_view()),
    #path('start',CreatWallView.as_view()),
   
]
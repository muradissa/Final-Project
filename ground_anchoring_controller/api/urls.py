from django.urls import path
from .views import CreatAnchorsView, CreatWallView, EnterParametersView, getHighMoment, getHighMoment2d, getImage1, getImage2, getImage3, getImage4, getImage5, getImage6, getImage7, simulationQuality, startSimulation ,getImage,getImageNumerical
from .views import AnchorView,WallView



urlpatterns = [
    path('anchors', AnchorView.as_view()),
    path('wall', WallView.as_view()),
    path('create-wall',CreatWallView.as_view()),
    path('create-anchors',CreatAnchorsView.as_view()),
    path('enter-parameter',EnterParametersView.as_view()),
    path('start',startSimulation.as_view()),
    path('quality',simulationQuality.as_view()),
    path('high-moment',getHighMoment.as_view()),
    path('plot-moment',getImage.as_view()),
    path('high-moment2d',getHighMoment2d.as_view()),
    path('plot-moment1',getImage1.as_view()),
    path('plot-moment2',getImage2.as_view()),
    path('plot-moment3',getImage3.as_view()),
    path('plot-moment4',getImage4.as_view()),
    path('plot-moment5',getImage5.as_view()),
    path('plot-moment6',getImage6.as_view()),
    path('plot-moment7',getImage7.as_view()),
    path('plot-moment-numerical',getImageNumerical.as_view()),
    #path('start',CreatWallView.as_view()),
   
]
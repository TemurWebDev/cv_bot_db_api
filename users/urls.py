from django.urls import path
from .views import UserApiView,UserUpdateApiView,UserView,AdminUpdateView,AdminView,ChannelUpdateView,ChannelView,CvView,CV_View,SkillView,EducationView,PersonalView,WorkView,SkillApiView,LanguageView,EducationApiView,PersonalApiView,WorkApiView,LanguageApiView,Educationedit


urlpatterns = [
    path('telegramuser/',UserApiView.as_view()),
    path('user/<str:user_id>/',UserView.as_view()),
    path('userupdate/<int:pk>/',UserUpdateApiView.as_view()),
    path('admin/',AdminView.as_view()),
    path('admin/delete/<str:user_id>/',AdminUpdateView.as_view()),
    path('channel/',ChannelView.as_view()),
    path('channel/delete/<str:channel_id>/',ChannelUpdateView.as_view()),
    path('cv/',CvView.as_view()),
    path('cv/<str:user_id>/',CV_View.as_view()),
    path('skilcreate/',SkillApiView.as_view()),
    path('skil/<str:user_id>/',SkillView.as_view()),
    path('educationcreate/',EducationApiView.as_view()),
    path('education/<str:user_id>/',EducationView.as_view()),
    path('educationedit/<str:user_id>/<int:id>/',Educationedit.as_view()),
    path('personalcreate/',PersonalApiView.as_view()),
    path('personalinfo/<str:user_id>/',PersonalView.as_view()),
    path('workcreate/',WorkApiView.as_view()),
    path('work/<str:user_id>/',WorkView.as_view()),
    path('languagecreate/',LanguageApiView.as_view()),
    path('language/<str:pk>/',LanguageView.as_view()),

]
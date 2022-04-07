from django.urls import path,include
from . import views

# pybo앱을 사용하겠다.
app_name='pybo'



urlpatterns=[
    path('',views.index,name="index"),
    path("<int:question_id>/",views.detail,name="detail"),
    path("answer/create/<int:question_id>/",views.answer_create,name="answer_create"),
    path('question/create/', views.question_create, name='question_create'),
    path('tour_info/', views.tour_info,name='tour_info'),
    path('tour_street/', views.tour_street,name='tour_street'),
    path('restaurant/', views.restaurant,name='restaurant'),
    path('tour_motel/', views.tour_motel,name='tour_motel'),
    path('tour_street/<int:tour_street_id>',views.tour_street_detail,name="tour_street"),
    path('tour_motel/<int:tour_motel_id>',views.tour_motel_detail,name="tour_motel"),
    path('tour_info/<int:tour_info_id>',views.tour_info_detail,name="tour_info"),
    path('restaurant/<int:restaurant_id>',views.restaurant_detail,name="restaurant"),
    path('motivation', views.motivation,name='motivation'),
    path('process', views.process,name='process'),
    path('troubleShooting', views.troubleShooting,name='troubleShooting'),
    path("goal",views.goal,name="goal" ),
]
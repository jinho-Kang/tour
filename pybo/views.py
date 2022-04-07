from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Question,Restaurant, TourInfo, TourMotel, TourStreet
from .forms import QuestionForm,AnswerForm
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
import pymysql
from django.core.paginator import Paginator
import pandas as pd
import googlemaps
import folium
import time
from tqdm.notebook import tqdm
import numpy as np




def index(request):
    return render(request,"pybo/index.html")

def detail(request,question_id):
    question_list=get_object_or_404(Question,pk=question_id)
    context={"question":question_list}
    return render(request,"pybo/question_detail.html",context)


def answer_create(request,question_id):
    question=get_object_or_404(Question,pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}

    return render(request, 'pybo/question_detail.html', context)  




def question_create(request):
    # pybo 질문등록
    if request.method=="POST":
        form=QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.create_date=timezone.now()
            question.save()
            return redirect("pybo:index")
    else:
        form=QuestionForm()
    context={'form':form}

    return render(request,'pybo/question_form.html',context)



def tour_info(request):
    template_name="../templates/paging_info.html"

    map=folium.Map(location=[37.5502,126.982],
              zoom_start=12)

    page = request.GET.get('page', '1')  # 페이지

    list_of_ids = []
    if page!="1":
        sum=int(page)*10
        for i in range(sum-9,int(page)*10+1):
            list_of_ids.append(i)
    else:
        sum=1
        for i in range(sum,int(page)*10+1):
            list_of_ids.append(i)

    tour_info = TourInfo.objects.filter(id__in=list_of_ids)
    for n in tour_info:
        folium.Marker(
        location=[n.위도,n.경도],
            tooltip=n.관광안내소명,
            popup='<pre>' + n.소재지도로명주소 + '</pre>'
        ).add_to(map)
    maps=map._repr_html_()

    tour_info_list=TourInfo.objects.order_by("id")
    paginator = Paginator(tour_info_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request,template_name,{"tour_info_maps":maps,"tour_info":page_obj})

def tour_street(request):
    template_name="../templates/paging_street.html"
    
    map=folium.Map(location=[37.5502,126.982],
              zoom_start=12)
    # 페이지가 바뀔때마다 모델을 다 불러오면 너무 비효율적이다.
    #  tour_street=TourStreet.objects.all()
    page = request.GET.get('page', '1')  # 페이지

    list_of_ids = []
    if page!="1":
        sum=int(page)*10
        for i in range(sum-9,int(page)*10+1):
            list_of_ids.append(i)
    else:
        sum=1
        for i in range(sum,int(page)*10+1):
            list_of_ids.append(i)

    tour_street = TourStreet.objects.filter(id__in=list_of_ids)
    for n in tour_street:
        folium.Marker(
        location=[n.위도,n.경도],
            tooltip=n.검색키워드,
            popup='<pre>' + n.지번주소 + '</pre>'
        ).add_to(map)
    maps=map._repr_html_()
    tour_street_list=TourStreet.objects.order_by("id")
    paginator = Paginator(tour_street_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request,template_name,{"tour_street_maps":maps,"tour_street":page_obj})


def restaurant(request):
    template_name="../templates/paging_restaurant.html"
    
    map=folium.Map(location=[37.5502,126.982],
              zoom_start=12)
    page = request.GET.get('page', '1')  # 페이지

    list_of_ids = []
    if page!="1":
        sum=int(page)*10
        for i in range(sum-9,int(page)*10+1):
            list_of_ids.append(i)
    else:
        sum=1
        for i in range(sum,int(page)*10+1):
            list_of_ids.append(i)

    restaurant = Restaurant.objects.filter(id__in=list_of_ids)
    
    for n in restaurant:
        print(n.가게이름,n.위도,n.경도)
        folium.Marker(
        location=[n.위도,n.경도],
            tooltip=n.가게이름,
            popup='<pre>' + n.주소 + '</pre>'
        ).add_to(map)
    maps=map._repr_html_()

    restaurant_list=Restaurant.objects.order_by("id")
    paginator = Paginator(restaurant_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request,template_name,{"restaurant_maps":maps,"restaurant":page_obj})


def tour_motel(request):
    template_name="../templates/paging_motel.html"

    map=folium.Map(location=[37.5502,126.982],
              zoom_start=12)  
    
    page = request.GET.get('page', '1')  # 페이지

    list_of_ids = []
    if page!="1":
        sum=int(page)*10
        for i in range(sum-9,int(page)*10+1):
            list_of_ids.append(i)
    else:
        sum=1
        for i in range(sum,int(page)*10+1):
            list_of_ids.append(i)
    
    tour_motel = TourMotel.objects.filter(id__in=list_of_ids)
    for n in tour_motel:
        folium.Marker(
        location=[n.위도,n.경도],
            tooltip=n.사업장명,
            popup='<pre>' + n.지번주소 + '</pre>'
        ).add_to(map)

    maps=map._repr_html_()

    tour_motel_list=TourMotel.objects.order_by("id")
    paginator = Paginator(tour_motel_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request,template_name,{"tour_motel_maps":maps,"tour_motel":page_obj})

def tour_street_detail(request,tour_street_id):
    tour_street_list=get_object_or_404(TourStreet,pk=tour_street_id)
    context={"tour_street":tour_street_list}
    return render(request,"pybo/tour_street_detail.html",context)


def tour_motel_detail(request,tour_motel_id):
    tour_motel_list=get_object_or_404(TourMotel,pk=tour_motel_id)
    context={"tour_motel":tour_motel_list}
    return render(request,"pybo/tour_motel_detail.html",context)


def tour_info_detail(request,tour_info_id):
    tour_info_list=get_object_or_404(TourInfo,pk=tour_info_id)
    context={"tour_info":tour_info_list}
    return render(request,"pybo/tour_info_detail.html",context)


def restaurant_detail(request,restaurant_id):
    restaurant_list=get_object_or_404(Restaurant,pk=restaurant_id)
    context={"restaurant":restaurant_list}
    return render(request,"pybo/restaurant_detail.html",context)


def motivation(request):
    return render(request,"pybo/motivation.html")
def process(request):
    return render(request,"pybo/process.html")
def troubleShooting(request):
    return render(request,"pybo/troubleShooting.html")
def goal(request):
    return render(request,"pybo/goal.html")    
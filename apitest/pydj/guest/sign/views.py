# encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Event, Guest

# Create your views here.
def index(request):
    return render(request, 'index.html')

# 登录事件
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将 session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

# 发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')  # 读取浏览器 session
    return render(request, "event_manage.html", {"user": username, "events": event_list})

# 发布会名称搜索
@login_required
def sreach_name(request):
    username = request.session.get('user', '')  # 读取浏览器session
    sreach_name = request.GET.get("name", "")  # 页面中获取输入的搜索关键字
    sreach_name_bytes = sreach_name.encode(encoding="utf-8")
    event_list = Event.objects.filter(name__contains=sreach_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})

# 嘉宾管理
@login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(guest_list, 1)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range(e.g.9999), deliver last page of results
        contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user": username, "guests": contacts})

# 嘉宾手机号搜索
@login_required
def sreach_phone(request):
    username = request.session.get('user', '')
    sreach_phone = request.GET.get("phone", "")
    # sreach_phone_bytes = sreach_phone.encode(encoding='utf-8')
    guest_list = Guest.objects.filter(phone__contains=sreach_phone)
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})

# 签到页面
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})

# 签到事件
@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone', '')
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': '手机号为空或不存在'})
    result = Guest.objects.filter(phone=phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': '该用户未参加此次发布会'})
    result = Guest.objects.get(phone=phone)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "已签到"})
    else:
        Guest.objects.filter(phone=phone).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': '签到成功!', 'guest': result})

# 退出登录
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/logout/')
    return response
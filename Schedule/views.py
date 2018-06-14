from django.shortcuts import render, HttpResponse
from . import models
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def crawler(request):
    for count in range(442):
        count = count + 1
        url = 'http://zhjw.scu.edu.cn/courseSearchAction.do'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cookie': 'safedog-flow-item=; _ga=GA1.3.88698885.1525926882; hibext_instdsigdipv2=1; JSESSIONID=bdcaX1-PHqz8Rh6doQ9pw; trdipcktrffcext=1; _gid=GA1.3.1720640769.1528969261',
            'Connection': 'keep-alive',
            'Host': 'zhjw.scu.edu.cn',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Referer': 'http://zhjw.scu.edu.cn/courseSearchAction.do'
        }

        datas = {
            'pageNumber': count,
            'actionType': 2
        }
        response = requests.post(url, headers=headers, data=datas)
        print(response.status_code)
        soup = BeautifulSoup(response.content.decode(
            'GBK', 'ignore'), 'html.parser')
        table = soup.find('table', class_='displayTag')
        trs = table.find_all('tr', class_='odd')
        for tr in trs:
            tds = tr.find_all('td')
            time = tds[9].string.split('~')
            class_start = time[0]
            class_end = time[1]
            models.Schdule.objects.create(academy=tds[0].string.strip(),
                                          course_number=tds[1].string.strip(),
                                          course_name=tds[2].string.strip(),
                                          course_list=tds[3].string.strip(),
                                          credit_hour=tds[4].string.strip(),
                                          test_type=tds[5].string.strip(),
                                          teacher=tds[6].string.strip(),
                                          course_week=tds[7].string.strip(),
                                          course_day=tds[8].string.strip(),
                                          course_time=tds[9].string.strip(),
                                          campus=tds[10].string.strip(),
                                          teaching_building=tds[11].string.strip(),
                                          classroom=tds[12].string.strip(),
                                          course_capacity=tds[13].string.strip(),
                                          course_limit=tds[15].string.strip(),
                                          course_start=class_start.strip(),
                                          course_end=class_end.strip()

                                          )

    return render(request, 'crawler.html')


def register(request):
    if request.method == 'POST':
        account = request.POST['account']
        password = request.POST['password']
        if models.User.objects.filter(user_name=account):
            message = '账号已存在'
            request.session['message'] = message
            return redirect('/login')
        else:
            in_password = make_password(password)
            models.User.objects.create(
                user_name=account, user_password=in_password)
            message = '注册成功'
            request.session['message'] = message
            return redirect('/login')


@csrf_exempt
def choose(request):
    if request.is_ajax():
        status = 1
        result = "succuss"
        test = [{"status": 1}]
        # return HttpResponse(
        #     json.dumps({
        #         "status": status,
        #         "result": result,
        #     }), content_type='application/json')
        return HttpResponse(json.dumps(test), content_type='application/json')
    return render(request, 'choose.html')


def login(request):
    if request.method == 'POST':
        account = request.POST['account']
        password = request.POST['password']
        try:
            user = models.User.objects.get(user_name=account)
            bool_password = check_password(password, user.user_password)
            if bool_password:
                request.session['account'] = user.user_name
                return redirect('/index')
            else:
                message = '密码错误'
                return render(request, 'login.html', {'message': message})
        except:
            message = '账号不存在'
            return render(request, 'login.html', {'message': message})
    if 'message' in request.session:
        message = request.session['message']
        del request.session['message']
        return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


@csrf_exempt
def index(request):
    if 'account' in request.session:
        if request.is_ajax():
            course_number = request.POST['course_number']
            if models.Schdule.objects.filter(course_number=course_number):
                schdules = models.Schdule.objects.filter(
                    course_number=course_number)
                datas = []
                for schdule in schdules:
                    dt = {
                        "academy": schdule.academy,
                        "course_number": schdule.course_number,
                        "course_name": schdule.course_name,
                        "course_list": schdule.course_list,
                        "credit_hour": schdule.credit_hour,
                        "test_type": schdule.test_type,
                        "teacher": schdule.teacher,
                        "course_week": schdule.course_week,
                        "course_day": schdule.course_day,
                        "course_time": schdule.course_time,
                        "campus": schdule.campus,
                        "teaching_building": schdule.teaching_building,
                        "classroom": schdule.classroom,
                        "course_capacity": schdule.course_capacity,
                        "course_limit": schdule.course_limit,
                        "course_start": schdule.course_start,
                        "course_end": schdule.course_end
                    }
                    datas.append(dt)
                print(datas)
                return HttpResponse(json.dumps(datas), content_type='application/json')
            else:
                message = '该课程不存在'
                return HttpResponse(message)
        return render(request, 'index.html')
    return redirect('/login')


def init(request):
    if 'account' in request.session:
        return redirect('/index')
    return redirect('/login')


def logout(request):
    del request.session['account']
    return redirect('/login')

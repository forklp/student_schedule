from django.shortcuts import render
from Schedule import models
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect


# Create your views here.
def crawler(request):
    for count in range(442):
        count = count + 1
        url = 'http://zhjw.scu.edu.cn/courseSearchAction.do'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cookie': 'safedog-flow-item=; _ga=GA1.3.88698885.1525926882; hibext_instdsigdipv2=1; _gid=GA1.3.318244352.1528272496; JSESSIONID=bcd2RNIamcZHl64_hiupw',
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
            models.Schdule.objects.create(academy=tds[0].string,
                                          course_number=tds[1].string,
                                          course_name=tds[2].string,
                                          course_list=tds[3].string,
                                          credit_hour=tds[4].string,
                                          test_type=tds[5].string,
                                          teacher=tds[6].string,
                                          course_week=tds[7].string,
                                          course_day=tds[8].string,
                                          course_time=tds[9].string,
                                          campus=tds[10].string,
                                          teaching_building=tds[11].string,
                                          classroom=tds[12].string,
                                          course_capacity=tds[13].string,
                                          course_limit=tds[15].string,
                                          course_start=class_start,
                                          course_end=class_end

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
            models.User.objects.create(user_name=account, user_password=in_password)
            message = '注册成功'
            request.session['message'] = message
            return redirect('/login')
    return render(request, 'login.html')


def choose(request):
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


def index(request):
    if 'account' in request.session:
        return render(request, 'index.html')
    return redirect('/login')


def init(request):
    if 'account' in request.session:
        return redirect('/index')
    return redirect('/login')


def logout(request):
    del request.session['account']
    return redirect('/login')
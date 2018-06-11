from django.shortcuts import render
from Schedule import models
import requests
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout


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
    return render(request, 'register.html')


def choose(request):
    return render(request, 'choose.html')


def index(request):
    return render(request, 'login.html')

# student_schedule
模拟选课系统

PS：不要改动templates和sdtatic文件夹之外的文件，以免合并是出现问题

html文件写在templates文件，js,css,等文件放在static文件夹



工程运行




在工程文件夹下(有manage.py文件的那一层)，启用命令行,命令python manage.py runserver启动，在网页中输入对应url打开网页

url


登录 /login


注册 /register


选课页面 /choose




数据库字段名


可在models.py文件中查看



form表单提交数据


action属性表示数据提交到的url，action='.'表示提交到当前页面，action='/register/'表示提交到register页面


from表单使用post方法时，要写{% csrf_token %}验证



git提交命令


git add *


git commit -m "提交"


git pull


git push origin master


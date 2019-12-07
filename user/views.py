from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from user.models import User


#
# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'register.html')
#
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repassword = request.POST.get('repassword')
#         if password == repassword:
#             user = User.objects.create(username=username, password=password)
#             if user:
#                 return HttpResponse('注册成功！')
#         return HttpResponse('注册失败！')

class UserView(View):
    def get(self, request, uid):
        user = User.objects.get(pk=uid)
        return JsonResponse({'status': 200, 'user': user.to_dict()})

    def post(self, request,uid):
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if password == repassword:
            user = User.objects.create(username=username, password=password)
            if user:
                return JsonResponse({'status': 200, 'msg': '注册成功'})
        return JsonResponse({'status': 200, 'msg': '注册失败'})

# def login(request):
#     if request.method=='POST':
#         pass
#     else:
#         pass

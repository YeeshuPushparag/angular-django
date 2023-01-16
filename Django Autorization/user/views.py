from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from .forms import ProfileForm, UserUpdate, ProfileUpdate
from rest_framework.renderers import JSONRenderer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        form = ProfileForm(request.POST, request.FILES, instance=myuser.profile)
        if form.is_valid():
            form.save()
        refresh = RefreshToken.for_user(myuser)
        return JsonResponse({'refresh': str(refresh), 'access':str(refresh.access_token)})

    return HttpResponse("invalid")

@login_required
def update(request):
    if request.method == 'POST':
        user = UserUpdate(request.POST, instance=request.user)
        profile = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if user.is_valid() and profile.is_valid():
            user.save()
            profile.save()
            return HttpResponse("profile updated")
        return HttpResponse("error")
    return HttpResponse("invalid")

@csrf_exempt
def loginuser(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        print(loginpassword,loginusername)
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return JsonResponse({'refresh': str(refresh), 'access':str(refresh.access_token)})
        else:
            return JsonResponse({"password":str(loginpassword),"username":str(loginusername)})
    return JsonResponse({"data":"invalid"})


def logoutuser(request):
    logout(request)
    return HttpResponse("logout successfully")










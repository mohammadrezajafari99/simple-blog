from django.shortcuts import redirect, render
from .models import UserProfile
from .forms import UpdateProfileForm,RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group

def profile(request,pk):
    user_profile=UserProfile.objects.get(profile_id=pk)

    dic={
        'profile':user_profile
    }

    return render(request,'profiles/profile.html',dic)




def account(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)
    user_account=request.user.userprofile
    dic={'account':user_account}

    return render(request,'profiles/profile.html',dic)






def updateprofile(request):
    profile=request.user.userprofile
    form =UpdateProfileForm(instance=profile)


    if request.method == 'POST':
        form=UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
          form.save()
          messages.info(request,'you updated your profile')
          return redirect('account')

    dic={
        'form':form,
    }
    return render(request,'profiles/update.html',dic)





def deleteprofile(request):
    profile=request.user.userprofile  ##username of user || model userProfile
    
    noob=UpdateProfileForm(instance=profile)

    if request.method =="POST":
    
       # userprofile=UserProfile.objects.get(user=profile)
        user=request.user
        user.delete()
        #messages.error(request,'Your profile has been deleted') ## اول باید یوزر پاک کنی تا پروفایلش بعد پاک بشه
        return redirect('index')

    dic={'ss':noob}

    return render(request,'profiles/deleteprofile.html',dic)



def register_user(request):
    form=RegisterForm()

    if request.method=="POST":  
        form=RegisterForm(request.POST)
        if form.is_valid():
         #   username=request.POST['username']
         #   email=request.POST['email']
         #   subject='welcome to my site'
         #   message= f'hi {username}  we will help you to find what your looking for'
         #   from_email=settings.EMAIL_HOST_USER
         #   recipient_list=[email]
         #   send_mail(subject,message,from_email,recipient_list,fail_silently=False)
            user = form.save()
            username=form.cleaned_data['username']
            group=Group.objects.get(name='Customer')
            user.groups.add(group)
            
            messages.success(request,'Account was created for ',username)
            return redirect('login')
    dic={'form':form}
    return render(request,'profiles/register.html',dic)






def login_user(request):
    if request.method=="POST":
          username=request.POST.get('username')
          password=request.POST.get('password')
          user=authenticate(request,username=username,password=password)
          if user is not None:
             login(request , user)
            
             return redirect('index')

          else:
             messages.info(request,'invalid credentials')


    
    dic={}
    return render(request,'profiles/login.html',dic)




def logout_user(request):
    logout(request)
    return redirect('index')

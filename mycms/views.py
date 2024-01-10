from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from  profiles.decorators import allowed_users,unauthenticated_user


def index(request):
    posts=Post.objects.all()
    context={'posts':posts}
    
    
    return render(request,'mycms/index.html',context)




@login_required(login_url='login')
def panel(request):
    user_account=request.user.userprofile
    
    dic={'pro':user_account}

    return render(request,'panel/panel2.html',dic)







@login_required(login_url='login')
def detail(request,slug):
    post=Post.objects.get(slug=slug)
    posts=Post.objects.exclude(post_id__exact=post.post_id)[:5]
  
    context={'post':post,'posts':posts}
    return render(request,'mycms/detail.html',context)




# @allowed_users(['admin'])
def createpost(request):
    
    
    profile= request.user.userprofile ## current user
   
    form=PostForm

    if request.method =='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.slug=slugify(post.title)
            post.writer = profile
            post.save()
            return redirect('index')
    dic={
        'form':form
    }
    return render(request,'mycms/create.html',dic)






def updatepost(request,slug):
    post=Post.objects.get(slug=slug)
    form =PostForm(instance=post)

    if request.method == "POST":
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail',slug =post.slug)


    dic={'form':form}

    return render(request,'mycms/update.html',dic)





def deletepost(request,slug):
  post=Post.objects.get(slug=slug)
  form= PostForm(instance=post)
  if request.method == "POST":
      post.delete()
      return redirect('index')

  dic={
      'form':form
  }
  return render(request,'mycms/delete.html',dic)



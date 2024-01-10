from django.http import HttpResponse
from django.shortcuts import redirect



def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.is_authenticated:
            return redirect('index')
        else:
            return view_func(request,*args,**kwargs)
        
    return wrapper_func




def allowed_users(allowed_roles=[]):
    def decorator(view_func):
      def wrapper_func(request,*args,**kwargs):
          group=None
          if request.user.groups.exists():
              group=request.user.groups.all()[0].name  ##اولی اسمش بگو
          if group in allowed_roles:
              return view_func(request,*args,**kwargs)
          else:
              return HttpResponse("you are not authorizd to view page")

      return wrapper_func
    return decorator




def admin_only(view_func):

     def wrapper_func(request,*args,**kwargs):
          group=None
          if request.user.groups.exists():
              group=request.user.groups.all()[0].name  ##اولی اسمش بگو
          if group == 'Customer':
              return redirect('')
          
          if group == 'admin':
          
             return view_func(request,*args,**kwargs)

     return wrapper_func



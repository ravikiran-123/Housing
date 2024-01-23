from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


# def role_required(allowed_roles=[]):
#     def decorator(view_func):
#         def Wrap(request, *args,**kwargs):
#             if request.Role.role in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return PermissionDenied
#         return Wrap
#     return decorator     

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None

            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not Authorised')
            
        return wrapper_func
    return decorator
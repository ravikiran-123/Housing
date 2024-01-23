from django.shortcuts import render,redirect,  get_object_or_404
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from django.contrib import messages, auth
from django.contrib.auth.models import User,Group
from django.core.mail import send_mail
from django.http import FileResponse, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from django.urls import reverse
from .forms import SearchForm
# from .decorators import role_required
from django.db.models import Q
from django.conf import settings
from . models import *
from .forms import SignUpForm,LoginForm


def Base(request):
    banner=Banner.objects.first()
    return render(request,'base.html',{'banners':banner})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg=None
    if request.method=='POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')# Redirect users to the index page
            else:
                msg='invalid Credentials'
        else:
            msg='error validating form'
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def register_view(request):
    msg=None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg='User Created'
            return redirect('login/')
        else:
            msg='form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'auth/register.html', {'form': form,'msg':msg})

# def logout_view(request):
    
#     return redirect('/housing/')


# from .mixins import MessaHandler
# import random
# from django.db.models import Q
# import json
# from .mixins import generate_otp, send_otp_via_textlocal, verify_otp

# def send_otp(request):
#     # if request.method == 'POST':
#         # phone_number = request.POST.get('phone_number')
#         otp = generate_otp()
#     #     response = send_otp_via_textlocal(settings.YOUR_API_KEY, settings.YOUR_SENDER_ID, phone_number, otp)

#     #     if response['status'] == 'success':
#     #         PhoneOTP.objects.update_or_create(phone_number=phone_number, defaults={'otp_code': otp})
#     #         return redirect('verify_otp')
#     #     else:
#     #         return render(request, 'otp_failed.html')
#     # return render(request, 'send_otp_form.html')
#         response = {'status': 'Yes'} if otp else {'status': 'No'}

#         return JsonResponse(response)

# def verify_otp(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         user_otp = request.POST.get('user_otp')

#         try:
#             otp_obj = PhoneOTP.objects.get(phone_number=phone_number)
#             if verify_otp(user_otp, otp_obj.otp_code):
#                 return render(request, 'otp_verified.html', {'phone_number': phone_number})
#             else:
#                 return render(request, 'otp_verification_failed.html')
#         except PhoneOTP.DoesNotExist:
#             return render(request, 'otp_verification_failed.html')
#     return render(request, 'verify_otp_form.html')



# # # Create your views here.
# def login_view(request):
#     if request.method=='POST':
#         phone_number=request.POST.get('phone_number')
#         profile=Profile.objects.filter(phone_number=phone_number)
#         if not profile.exists():
#             return redirect('/register/')
        
#         profile[0].otp =random.randint(1000, 9999)
#         profile[0].save()
#         meassage_handler=MessaHandler(phone_number,profile[0].otp).send_otp_on_phone()

#         return redirect(f'/otp/{profile[0].uid}')


#     return render(request,'login.html')

# def register_view(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         phone_number=request.POST.get('phone_number')
#         user=User.objects.create(username=username)
#         profile=Profile.objects.create(user=user,phone_number=phone_number)

#         return redirect('/login/')
    
#     return render(request,'register.html')

# def otp(request,uid):
#     if request.method=='POST':
#         otp=request.POST.get('otp')
#         profile= Profile.objects.get(uid = uid)
#         if otp ==  profile.otp:
#             login(request, profile.user)
#             return redirect('/')
        
#         return redirect(f'/otp/{uid}')

#     return render (request, 'otp.html')

def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        is_agent = request.POST.get('is_agent', False)
        is_user = request.POST.get('is_user', False)
        is_builder = request.POST.get('is_builder', False)
        is_flatmate = request.POST.get('is_flatmate', False)
        is_owner = request.POST.get('is_owner', False)

        if is_agent == 'on':
            is_agent = True
            is_staff = True
        elif is_owner == 'on':
            is_owner = True
            is_staff = True
        elif is_builder == 'on':
            is_builder = True
            is_staff = True
        elif is_flatmate == 'on':
            is_flatmate = True
            is_staff = True
        elif is_user == 'on':
            is_user = True
            is_staff = False
        else:
            is_user = False
            is_agent = False
            is_builder = False
            is_flatmate = False
            is_owner = False  

              
        # Check if passwords match
        if password == password2:
            #  Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email already exists')
                    return redirect('register')
                else:
                    # Everything passed
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name,
                                                    is_user=is_user, is_agent=is_agent, is_owner=is_owner,
                                                      is_builder=is_builder, is_flatmate=is_flatmate ,is_staff=is_staff)
                    
                    messages.success(request, 'You are now registered and can Log In')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            if user.is_agent:
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                return redirect('admin/')
            elif user.is_owner:
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                return redirect('admin/')
            elif user.is_builder:
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                return redirect('admin/')
            elif user.is_flatmate:
                group = Group.objects.get(name='Flatmate')
                user.groups.add(group)
                return redirect('admin/')
            else:
                return redirect ('/housing/')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('housing')
    else:
        return render(request, 'accounts/login.html')


def logout(request):

    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('/housing/')


def main_Housingcontact(request):
    if request.method=="POST":
        post=HousingContact()
        form_data=request.POST
        post.user = request.user
        post.name=form_data.get('name')
        post.phone_no=form_data.get('phone_no')
        post.email=form_data.get('email')
        product_id=form_data.get("product_id")
        my_model = ProjectDetail.objects.get(developer_id=product_id)
        post.project_details = my_model
        send_mail(
            'Customer Details from Contact-Form',
            f'Project-Name:{my_model.developer_name}\nName:{post.name}\nPhone:{post.phone_no}\nEmail:{post.email}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        send_mail(
            'Customer Details from Contact Form',
            f'Project-Name:{my_model.developer_name}\nName: {post.name}\nPhone: {post.phone_no}\nEmail: {post.email}',
            settings.EMAIL_HOST_USER,
            [my_model.Agent.email],  # Assuming you have a 'user' field in your Contact model
            fail_silently=False,
        )
        post.save()
        return redirect('/housing/thank/')
    else:
        return render(request,'Buypage_housingexperts.html')





def main_contact(request):
    if request.method=="POST":
        post=Contact()
        form_data=request.POST
        post.user = request.user
        post.name=form_data.get('name')
        post.phone_no=form_data.get('phone_no')
        post.email=form_data.get('email')
        product_id=form_data.get("product_id")
        my_model = ProjectDetail.objects.get(id=product_id)
        post.project_details = my_model
        
        send_mail(
            'Customer Details from Contact-Form',
            f'Project-Name:{my_model.name}\nName:{post.name}\nPhone:{post.phone_no}\nEmail:{post.email}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        send_mail(
            'Customer Details from Contact Form',
            f'Project-Name:{my_model.name}\nName: {post.name}\nPhone: {post.phone_no}\nEmail: {post.email}',
            settings.EMAIL_HOST_USER,
            [my_model.Agent.email],  # Assuming you have a 'user' field in your Contact model
            fail_silently=False,
        )
        post.save()
        return redirect('/housing/thank/')
    else:
        return render(request,'index.html')
    
def main_RentContact(request):
    if request.method=="POST":
        post=RentContact()
        form_data=request.POST
        post.user = request.user
        post.name=form_data.get('name')
        post.phone_no=form_data.get('phone_no')
        post.email=form_data.get('email')
        product_id=form_data.get("product_id")
        rent_project = RentProjectDetail.objects.get(id=product_id)
        post.rentproject_details = rent_project
        send_mail(
            'Customer Details from Contact-Form',
            f'Project-Name:{rent_project.name}\nName:{post.name}\nPhone:{post.phone_no}\nEmail:{post.email}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        send_mail(
            'Customer Details from Contact Form',
            f'Project-Name:{rent_project.name}\nName: {post.name}\nPhone: {post.phone_no}\nEmail: {post.email}',
            settings.EMAIL_HOST_USER,
            [rent_project.Agent.email],  # Assuming you have a 'user' field in your Contact model
            fail_silently=False,
        )
        post.save()
        return redirect('/housing/thank/')
    else:
        return render(request,'rent.html')
    
def main_CommercialContact(request):
    if request.method=="POST":
        post=CommercialContact()
        form_data=request.POST
        post.user = request.user
        post.name=form_data.get('name')
        post.phone_no=form_data.get('phone_no')
        post.email=form_data.get('email')
        product_id=form_data.get("product_id")
        commercial_project = CommercialProjectDetail.objects.get(id=product_id)
        post.commercialproject_details = commercial_project
        send_mail(
            'Customer Details from Contact-Form',
            f'Project-Name:{commercial_project.name}\nName:{post.name}\nPhone:{post.phone_no}\nEmail:{post.email}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        send_mail(
            'Customer Details from Contact Form',
            f'Project-Name:{commercial_project.name}\nName: {post.name}\nPhone: {post.phone_no}\nEmail: {post.email}',
            settings.EMAIL_HOST_USER,
            [commercial_project.Agent.email],  # Assuming you have a 'user' field in your Contact model
            fail_silently=False,
        )
        post.save()
        return redirect('/housing/thank/')
    else:
        return render(request,'commercial.html')

def main_Plotcontact(request):
    if request.method=="POST":
        post=PlotContact()
        form_data=request.POST
        post.user = request.user
        post.name=form_data.get('name')
        post.phone_no=form_data.get('phone_no')
        post.email=form_data.get('email')
        product_id=form_data.get("product_id")
        plots_project = PlotsProjectDetail.objects.get(id=product_id)
        post.plotsproject_details = plots_project
        send_mail(
            'Customer Details from Contact-Form',
            f'Project-Name:{plots_project.name}\nName:{post.name}\nPhone:{post.phone_no}\nEmail:{post.email}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        send_mail(
            'Customer Details from Contact Form',
            f'Project-Name:{plots_project.name}\nName: {post.name}\nPhone: {post.phone_no}\nEmail: {post.email}',
            settings.EMAIL_HOST_USER,
            [plots_project.Agent.email],  # Assuming you have a 'user' field in your Contact model
            fail_silently=False,
        )
        post.save()
        return redirect('/housing/thank/')
    else:
        return render(request,'plots.html')
    
def enquiry(request):
    if request.method=="POST":
        post=Enquiry_Form()
        form_data=request.POST
        post.name=form_data.get('name')
        post.phone_no=form_data.get('phone_no')
        post.email=form_data.get('email')
        post.message=form_data.get('message')
        send_mail(
            'Customer Details from Enquiry-Form',
            f'Name:{post.name}\nPhone:{post.phone_no}\nEmail:{post.email}\nMessage:{post.message}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        post.save()
        return redirect('/housing/thank/')
    else:
        return render(request,'index.html')

def download_brochure(request):
    if request.method=="POST":
        post=DownloadForm()
        form_data = request.POST
        post.name=form_data.get('name')
        post.Mobile_number=form_data.get('mobile_number')
        post.email=form_data.get('email')
        product_name=form_data.get("product_name")
        my_model = ProjectDetail.objects.get(name=product_name)
        file_path = my_model.File_upload.path
        file_name = my_model.File_upload.name
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
        send_mail(
            'Customer Details from brochure',
            f'Project-Name:{my_model.name}\nUser-Name:{post.name}\nPhone:{post.Mobile_number}\nEmail:{post.email}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        send_mail(
            'Customer Details from Contact Form',
            f'Project-Name:{my_model.name}\nName: {post.name}\nPhone: {post.Mobile_number}\nEmail: {post.email}',
            settings.EMAIL_HOST_USER,
            [my_model.Agent.email],  # Assuming you have a 'user' field in your Contact model
            fail_silently=False,
        )
        post.save()
        return response

def plotdownload_brochure(request):
    if request.method=="POST":
       
        post=DownloadForm()
        form_data = request.POST
        post.name=form_data.get('name')
        post.Mobile_number=form_data.get('mobile_number')
        post.email=form_data.get('email')
        product_name=form_data.get("product_name")
        my_model = PlotsProjectDetail.objects.get(name=product_name)
        file_path = my_model.File_upload.path
        file_name = my_model.File_upload.name
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
        send_mail(
            'Customer Details from brochure',
            f'Project-Name:{my_model.name}\nUser-Name:{post.name}\nPhone:{post.Mobile_number}\nEmail:{post.email}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        send_mail(
            'Customer Details from Contact Form',
            f'Project-Name:{my_model.name}\nName: {post.name}\nPhone: {post.Mobile_number}\nEmail: {post.email}',
            settings.EMAIL_HOST_USER,
            [my_model.Agent.email],  # Assuming you have a 'user' field in your Contact model
            fail_silently=False,
        )
        post.save()
        return response

def thank(request):
    return render(request, "thankyou.html")

def comment(request):
    if request.method=="POST":
        post=CommentForm()
        form_data=request.POST
        post.name=form_data.get('name')
        post.phone_no=form_data.get('phone_no')
        post.email=form_data.get('email')
        post.message=form_data.get('message')
        send_mail(
            'Customer Details from Comment-Form',
            f'Name:{post.name}\nPhone:{post.phone_no}\nEmail:{post.email}\nMessage:{post.message}',
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        post.save()
        return redirect('/thank/')
    else:
        return render(request,'articles.html')




def get_suggestions(request):
    query = request.GET.get('query')
    suggestions = []

    if query:
        # Assuming ProjectDetail, RentProjectDetail, CommercialProjectDetail,
        # and PlotsProjectDetail have a common field 'name' for suggestions.
        suggestions = (
            ProjectDetail.objects.filter(Q(city__icontains=query) |Q(developer_name__icontains=query) | Q(address__icontains=query)) or
            RentProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query)) or
            CommercialProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query)) or
            PlotsProjectDetail.objects.filter(Q(city__icontains=query)|Q(developer_name__icontains=query) | Q(address__icontains=query)) 
        ).values_list('name', flat=True)

    return JsonResponse({'suggestions': list(suggestions)})


def searchProperty(request):
    query = request.GET.get('query')
    payload=[]

    if query:
        results = ProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query) | Q(developer_name__icontains=query) ) or RentProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query)) or CommercialProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query)) or PlotsProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query) | Q(developer_name__icontains=query))
        for result in results:
            payload.append({
                'city':result.city,
                'address':result.address,
                'developer_name':result.developer_name
            })
    return JsonResponse({
        'status':True,
        'payload':payload,})

def search(request):
    form=SearchForm(request.GET)
    query = request.GET.get("query", "")
    results=[]
    if query:
        results = ProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query) | Q(developer_name__icontains=query)) or RentProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query)) or CommercialProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query)) or PlotsProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query) | Q(developer_name__icontains=query)) 
        if query:
             RecentSearch.objects.create(query=query)
    for property in results:
        if isinstance(property, ProjectDetail):
            property.model_name = 'projectdetail'
        elif isinstance(property, RentProjectDetail):
            property.model_name = 'rentprojectdetail'
        elif isinstance(property, CommercialProjectDetail):
            property.model_name = 'commercialprojectdetail'
        elif isinstance(property, PlotsProjectDetail):
            property.model_name = 'plotsprojectdetail'
        else:
            property.model_name = 'unknown'
    recent_searches = RecentSearch.objects.order_by('-timestamp')[:3]
    choice_objects=ProjectDetail.objects.all()
    logo=Logo.objects.first()
    banner=Banner.objects.first()
    details=Contact_Details.objects.first()
    return render(request,'property_search_results.html',{"choices":choice_objects,"properties":results,"form":form,"query":query,'recent_searches': recent_searches,"banners":banner,"logos":logo,"detail":details})

def search_suggestions(request):
    # queryset_list = ProjectDetail.objects.all()
    form=SearchForm(request.GET)
    query = request.GET.get("query", "")
    results=[]
    if query:
        results = ProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query) | Q(developer_name__icontains=query)) or RentProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query)) or CommercialProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query)) or PlotsProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query) | Q(developer_name__icontains=query)) or FlatmateProjectDetail.objects.filter(Q(city__icontains=query) | Q(address__icontains=query) | Q(Project_by__icontains=query))

        if query:
             RecentSearch.objects.create(query=query)

    recent_searches = RecentSearch.objects.order_by('-timestamp')[:3]
    choice_objects=ProjectDetail.objects.all()

    return render(request,'property_search_results.html',{"choices":choice_objects,"results":results,"form":form,"query":query,'recent_searches': recent_searches})



# def add_residential(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         image_file = request.FILES.get("image")
#         logo_image_file = request.FILES.get("log_image")

#         new_residential = residential.objects.create(
#             project_details = data.get('project_details'),
#             type = data.get("project_type"),
#             image = image_file,
#             logo_image= logo_image_file,
#             name=data.get("name"),
#             project_by = data.get('project_by'),
#             year_estd=data.get('year_estd'),
#             no_of_projects=data.get("no_of_projects"),
#             description=data.get("description"),
#             title=data.get("title"),
#             address=data.get("address"),
#             city=data.get("city"),
#             price=data.get("price"),
#             no_of_bhks=data.get("no_of_bhks")
#         )

#         return render(request, "index.html")

#     return render(request, "newResidential.html")


# @login_required(login_url='login')
# @allowed_users(allowed_roles=["Admin"])
def home(request):
    developers_with_projects = []
    for developer in DeveloperDetails.objects.filter(developer_type='Buy').all().order_by("-id")[:6]:
        projects = ProjectDetail.objects.filter(developers=developer).all()[:2]
        developers_with_projects.append({'developer': developer, 'projects': projects})
    residence_objects=NewsDetails.objects.all()
    expert_objects=HousingExperts.objects.filter(is_buy=True).order_by("-id")[:6]
    project_objects=ProjectDetail.objects.filter(is_active=True,is_sale=True, is_featured=True).all()
    spot_objects=ProjectDetail.objects.filter(is_active=True, is_featured=True,is_sale=True).all().order_by("-id")[:6]
    focus_objects=ProjectDetail.objects.filter(is_active=True,is_sale=True,is_featured=True).all().order_by("-id")[:6]
    feature_objects=ProjectDetail.objects.filter(is_active=True, is_featured=True).all().order_by("-id")[:6]
    trending_objects=ProjectDetail.objects.filter(is_active=True,is_sale=True, is_featured=True).all().order_by("-id")[:20]
    recent_objects=ProjectDetail.objects.filter(is_active=True, is_featured=True,is_sale=True).all().order_by("-id")[:6]
    developer_objects=DeveloperDetails.objects.filter(developer_type='Buy').all().order_by("-id")[:6]
    feature_details=Featuredcollections.objects.filter(feature_type='Buy').all().order_by("-id")[:6]
    feature_count=Featuredcollections.objects.filter(feature_type='Buy').all().count()
    featured_collections = Featuredcollections.objects.annotate(project_count=models.Count('project_details'))
    map_objects=ProjectDetail.objects.order_by("-id")[:6]
    choice_objects=ProjectDetail.objects.all()
    features_count=ProjectDetail.objects.count
    logo=Logo.objects.first()
    banner=Banner.objects.first()
    details=Contact_Details.objects.first()
    return render(request,'index.html',{"developers_with_projects":developers_with_projects,"feature_counts":feature_count,"banners":banner,"choices":choice_objects,"residences":residence_objects,"focuses":focus_objects,"features":feature_objects,
                                        "experts":expert_objects,"feature_objects":feature_details,"recents":recent_objects,"trendings":trending_objects,"topprojects":project_objects,"spots":spot_objects,
                                        "developers":developer_objects,"maps":map_objects,"logos":logo,
                                        "detail":details,"features_counts":features_count,'featured_collections': featured_collections
                                        })
            
def rent(request):  
    rent=Featuredcollections.objects.filter(feature_type='Rent').all()
    features_count=RentProjectDetail.objects.count
    expert_objects=HousingExperts.objects.filter(is_rent=True).order_by("-id")[:6]
    residence_objects=NewsDetails.objects.all()
    rent_objects=RentProjectDetail.objects.order_by("-id")[:6]
    map_objects=RentProjectDetail.objects.order_by("-id")[:6]
    logo=Logo.objects.first()
    banner=Banner.objects.first()
    details=Contact_Details.objects.first()
    return render(request,'rent.html',{"banners":banner,"rents":rent,"features_counts":features_count,"residences":residence_objects,"leases":rent_objects,"logos":logo,"detail":details,"maps":map_objects,"experts":expert_objects})

def Commercial(request):  
    objects=CommercialProjectDetail.objects.filter(commercial_type='Recently Added properties for sale').all()
    commercial_details=CommercialProjectDetail.objects.filter(commercial_type='Recently Added properties for Rent').all()
    expert_objects=HousingExperts.objects.filter(is_commercial=True).order_by("-id")[:6]   
    residence_objects=NewsDetails.objects.all()
    logo=Logo.objects.first()
    banner=Banner.objects.first()
    details=Contact_Details.objects.first()
    return render(request,'commercial.html',{"banners":banner,"commercial_details":objects,"commercial_objects":commercial_details,"residences":residence_objects,"experts":expert_objects,"logos":logo,"detail":details})


def Plots(request):  
    developers_with_projects = []
    for developer in DeveloperDetails.objects.filter(developer_type='Plots').all().order_by("-id")[:6]:
        projects = PlotsProjectDetail.objects.filter(developers=developer).all()[:2]
        developers_with_projects.append({'developer': developer, 'projects': projects})
    plot=Featuredcollections.objects.filter(feature_type='Plots').order_by("-id")[:6]
    features_count=CommercialProjectDetail.objects.count
    developer_objects=DeveloperDetails.objects.filter(developer_type='Plots').all()
    plot_objects=PlotsProjectDetail.objects.filter(is_active=True,is_sale=True).all()
    feature_objects=PlotsProjectDetail.objects.filter(is_active=True, is_featured=True).all()
    expert_objects=HousingExperts.objects.filter(is_plot=True).order_by("-id")[:6]  
    residence_objects=NewsDetails.objects.all()
    banner=Banner.objects.first()
    logo=Logo.objects.first()
    details=Contact_Details.objects.first()
    return render(request,'plots.html',{"banners":banner,"features_counts":features_count,"features":feature_objects,"developers_with_projects":developers_with_projects,"plots":plot,"plot_details":plot_objects,"logos":logo,"detail":details,"developer_details":developer_objects,"residences":residence_objects,"experts":expert_objects})


def Flatmate(request, flatmate_choices='Boys'):  
    if flatmate_choices=='Boys':
        flat=FlatmateChoice.objects.all()
    elif flatmate_choices=='Girls':
        flat=FlatmateChoice.objects.all()
    elif flatmate_choices=='Food Available':
        flat=FlatmateChoice.objects.all()
    elif flatmate_choices=='Private Room':
        flat=FlatmateChoice.objects.all()

    flat_objects=FlatmateProjectDetail.objects.order_by("-id").all()
    residence_objects=NewsDetails.objects.filter(news_type='Flatmate').all()
    logo=Logo.objects.first()
    details=Contact_Details.objects.first()
    return render(request,'flatmate.html',{"flats":flat,"flat_details":flat_objects,"residences":residence_objects,"logos":logo,"detail":details})


def BuypageDevelopers(request,product_id):
    project = get_object_or_404(DeveloperDetails, id=product_id)
    developer_details=ProjectDetail.objects.filter(developers_id=product_id).prefetch_related('gallery_set','details_set')
    logo=Logo.objects.first()
    details=Contact_Details.objects.first()
    developer_objects=DeveloperDetails.objects.filter(developer_type='Buy').all()
    expert_objects=HousingExperts.objects.filter(expert_type='Plots').order_by("-id")[:6]
    items_per_page = 10
    paginator = Paginator(developer_details, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"developers.html",{"project":project,"feature_objects":page,"experts":expert_objects,"logos":logo,"detail":details,"developers":developer_objects})



def PlotpageDevelopers(request,product_id):
    project = get_object_or_404(DeveloperDetails, id=product_id)
    developer_details=PlotsProjectDetail.objects.filter(developers_id=product_id)
    logo=Logo.objects.first()
    details=Contact_Details.objects.first()
    items_per_page = 1
    paginator = Paginator(developer_details, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"plotdevelopers.html",{"project":project,"feature_objects":page,"logos":logo,"detail":details})


def BuyFeaturecollections(request,product_id):
    
    Expert=HousingExperts.objects.filter(expert_type='Buy').first()
    feature_details=ProjectDetail.objects.filter(Features_id=product_id).prefetch_related('gallery_set','details_set')
    logo=Logo.objects.first()
    details=Contact_Details.objects.first()
    items_per_page = 10
    paginator = Paginator(feature_details, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"featuredcollection.html",{"expert":Expert,"feature_objects":page,"logos":logo,"detail":details})

def RentFeaturecollections(request,product_id):
    Expert=HousingExperts.objects.filter(expert_type='Rent').first()
    feature_details=RentProjectDetail.objects.filter(Features_id=product_id).prefetch_related('rentgallery_set','rentdetails_set')
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    items_per_page = 10 
    paginator = Paginator(feature_details, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"rentfeaturedcollections.html",{"expert":Expert,"feature_objects":page,"logos":logo,"detail":details})

def CommercialFeaturecollections(request,product_id):
    Expert=HousingExperts.objects.filter(expert_type='Commercial').first()
    feature_details=CommercialProjectDetail.objects.filter(Features_id=product_id).prefetch_related('commercialgallery_set','commercialdetails_set')
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    items_per_page = 10 
    paginator = Paginator(feature_details, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"commercialfeaturedcollections.html",{"expert":Expert,"feature_objects":page,"logos":logo,"detail":details})

def Commercialcollections(request,product_name, product_id):
    url = reverse('Buy_projects', kwargs={'product_id':product_id,'product_name': product_name})
    Expert=HousingExperts.objects.filter(expert_type='Commercial').first()
    feature_details=CommercialProjectDetail.objects.filter(Features_id=product_id).prefetch_related('commercialgallery_set','commercialdetails_set')
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    items_per_page = 10 
    paginator = Paginator(feature_details, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"commercialfeaturedcollections.html",{"expert":Expert,"feature_objects":page,"logos":logo,"detail":details})



def PlotFeaturecollections(request,product_id):
    Expert=HousingExperts.objects.filter(expert_type='Plot').first()
    feature_details=PlotsProjectDetail.objects.filter(Features_id=product_id).prefetch_related('plotgallery_set','plotdetails_set')
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    items_per_page = 10
    paginator = Paginator(feature_details, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"plotsfeaturedcollections.html",{"expert":Expert,"feature_objects":page,"logos":logo,"detail":details})

def FlatmatePageChoice(request,product_id):
    flat_details=FlatmateProjectDetail.objects.filter(Flatmates_id=product_id)
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    items_per_page = 10  
    paginator = Paginator(flat_details, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"flatmatecollections.html",{"feature_objects":page,"logos":logo,"detail":details})

def Buypage_Experts(request,experts_id):
    Expert=HousingExperts.objects.get(id=experts_id)
    product_objects=Expert.project_details
    # product_objects=ProjectDetail.objects.filter(product_id=Experts_id)
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,"Buypage_housingexpert.html",{"product_details":product_objects,"experts":Expert,"logos":logo,"detail":details})


def rentpage_Experts(request,product_id):
    expert_objects=HousingExperts.objects.get(id=product_id)
    product_objects=RentProjectDetail.objects.filter(Experts_id=product_id)
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,"rentpage_housingexpert.html",{"product_details":product_objects,"experts":expert_objects,"logos":logo,"detail":details})


def commercialpage_Experts(request,product_id):
    expert_details=HousingExperts.objects.get(id=product_id)
    product_objects=CommercialProjectDetail.objects.filter(Experts_id=product_id)
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,"commercialpage_housingexpert.html",{"product_details":product_objects,"experts":expert_details,"logos":logo,"detail":details})


def plotspage_Experts(request,product_id):
    Expert=HousingExperts.objects.get(id=product_id)
    product_objects=PlotsProjectDetail.objects.filter(Experts_id=product_id)
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,"plotspage_housingexpert.html",{"product_details":product_objects,"experts":Expert,"logos":logo,"detail":details})


def News_details(request,product_name):
    product_objects=NewsDetails.objects.prefetch_related("comment_set").get(name=product_name)
    residence_objects=NewsDetails.objects.all()
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,"articles.html",{"product_details":product_objects,"sources":residence_objects,"logos":logo,"detail":details})

def News(request,product_id,product_name):
    url = reverse('News', kwargs={'product_id':product_id,'product_name': product_name})
    product_objects=NewsDetails.objects.prefetch_related("comment_set").get(name=product_name)
    residence_objects=NewsDetails.objects.all()
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,"articles.html",{"product_details":product_objects,"sources":residence_objects,"logos":logo,"detail":details})

def All_News(request):
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    residence_objects=NewsDetails.objects.all()
    return render(request,"news.html",{"news":residence_objects,"logos":logo,"detail":details})
 
def contactpage(request):
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,'contact.html',{"detail":details,"logos":logo})


def Buy_projects(request, product_name, product_id):
    url = reverse('Buy_projects', kwargs={'product_id':product_id,'product_name': product_name})
    
    project_objects=ProjectDetail.objects.prefetch_related("gallery_set","details_set","amenities_set","floorplan_set","projectadvantages_set","faq_set").get(name=product_name)
    developer_objects=DeveloperDetails.objects.filter(developer_type='Buy').first()
    ready_to_move_projects = ProjectDetail.objects.filter(developers=developer_objects, possession_status='Ready to move')
    in_3_years_projects = ProjectDetail.objects.filter(developers=developer_objects, possession_status='In 3 years')
    beyond_3_years_projects = ProjectDetail.objects.filter(developers=developer_objects, possession_status='Beyond 3 years')
    source_objects=ProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()

    return render(request,"property.html",{"project_details":project_objects,"sources":source_objects,"detail":details,"logos":logo,"developers":developer_objects,"ready_to_move_projects": ready_to_move_projects,
        "in_3_years_projects": in_3_years_projects,
        "beyond_3_years_projects": beyond_3_years_projects,})



def projects(request, product_name):
    project_objects=ProjectDetail.objects.prefetch_related("gallery_set","details_set","amenities_set","floorplan_set","projectadvantages_set","faq_set").get(name=product_name)
    developer_objects=DeveloperDetails.objects.filter(developer_type='Buy').first()
    ready_to_move_projects = ProjectDetail.objects.filter(developers=developer_objects, possession_status='Ready to move')
    in_3_years_projects = ProjectDetail.objects.filter(developers=developer_objects, possession_status='In 3 years')
    beyond_3_years_projects = ProjectDetail.objects.filter(developers=developer_objects, possession_status='Beyond 3 years')
    source_objects=ProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    # floorplans = project_objects.floorplan_set.all()
    floorplans = project_objects.floorplan_set.order_by('Configuration', 'sq_ft')
    configuration_data = {}
    for floorplan in floorplans:
        config = floorplan.Configuration
        sq_ft = floorplan.sq_ft
        image_url = floorplan.image.url

        if config not in configuration_data:
            configuration_data[config] = {}

        if sq_ft not in configuration_data[config]:
            configuration_data[config][sq_ft] = []

        configuration_data[config][sq_ft].append(image_url)
    
    return render(request,"property.html",{"project_details":project_objects,"sources":source_objects,"detail":details,"logos":logo, "developers":developer_objects,"ready_to_move_projects": ready_to_move_projects,
        "in_3_years_projects": in_3_years_projects,
        "beyond_3_years_projects": beyond_3_years_projects,
        "floorplans":configuration_data})


def list_property(request):
    list_objects=ProjectDetail.objects.all()
    listing_objects=RentProjectDetail.objects.all()
    commercial_listings=CommercialProjectDetail.objects.all()
    plot_listings=PlotsProjectDetail.objects.all()
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    banner=Banner.objects.first()
    return render(request, 'listproperty.html',{"banners":banner,'list_products':list_objects,"listings":listing_objects,"commercial_listings":commercial_listings,"plot_listings":plot_listings,"detail":details,"logos":logo})

def rent_projects(request,product_name, product_id):
    url = reverse('rent_projects', kwargs={'product_id': product_id, 'product_name': product_name})
    rent_objects=RentProjectDetail.objects.prefetch_related("rentgallery_set","rentdetails_set","rentamenities_set","rentfurnishings_set").get(name=product_name)
    commercial=Featuredcollections.objects.filter(feature_type='Commercial').all()
    source_objects=RentProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,'rent_property.html',{"rent_details":rent_objects,"commercials":commercial,"sources":source_objects,"detail":details,"logos":logo})

def rent_houses(request,product_name):
    rent_objects=RentProjectDetail.objects.prefetch_related("rentgallery_set","rentdetails_set","rentamenities_set","rentfurnishings_set").get(name=product_name)
    commercial=Featuredcollections.objects.filter(feature_type='Commercial').all()
    source_objects=RentProjectDetail.objects.order_by("-id")[:3]
    features_count=CommercialProjectDetail.objects.count

    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,'rent_property.html',{"rent_details":rent_objects,"features_counts":features_count,"commercials":commercial,"sources":source_objects,"detail":details,"logos":logo})




def Commercial_projects(request,product_name, product_id):
    url = reverse('commercial_projects', kwargs={'product_id': product_id, 'product_name': product_name})
    commercial_objects=CommercialProjectDetail.objects.prefetch_related("commercialgallery_set","commercialdetails_set","commercialamenities_set").get(name=product_name)
    source_objects=CommercialProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,'commercial_property.html',{'commercial_details':commercial_objects,"sources":source_objects,"detail":details,"logos":logo})

def Commercial_Features(request,product_name):
    commercial_objects=CommercialProjectDetail.objects.prefetch_related("commercialgallery_set","commercialdetails_set","commercialamenities_set").get(name=product_name)
    source_objects=CommercialProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,'commercial_property.html',{'commercial_details':commercial_objects,"sources":source_objects,"detail":details,"logos":logo})



def Plots_projects(request,product_name,product_id):
    url = reverse('plots_projects', kwargs={'product_id': product_id, 'product_name': product_name})
    plot_objects=PlotsProjectDetail.objects.prefetch_related("plotgallery_set","plotdetails_set","plotamenities_set","plotfloorplan_set","plotadvantages_set","plotfaq_set").get(name=product_name)
    developer_objects=DeveloperDetails.objects.filter(developer_type='Plots').first()
    ready_to_move_projects = PlotsProjectDetail.objects.filter(developers=developer_objects, possession_status='Ready to move')
    in_3_years_projects = PlotsProjectDetail.objects.filter(developers=developer_objects, possession_status='In 3 years')
    beyond_3_years_projects = PlotsProjectDetail.objects.filter(developers=developer_objects, possession_status='Beyond 3 years')
    source_objects=PlotsProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,'plots_property.html',{'plots_details':plot_objects,"sources":source_objects,"detail":details,"logos":logo,"developers":developer_objects,"ready_to_move_projects": ready_to_move_projects,
        "in_3_years_projects": in_3_years_projects,
        "beyond_3_years_projects": beyond_3_years_projects})

def Plotprojects(request,product_name):
    plot_objects=PlotsProjectDetail.objects.prefetch_related("plotgallery_set","plotdetails_set","plotamenities_set","plotfloorplan_set","plotadvantages_set","plotfaq_set").get(name=product_name)
    developer_objects=DeveloperDetails.objects.filter(developer_type='Plots').first()
    ready_to_move_projects = PlotsProjectDetail.objects.filter(developers=developer_objects, possession_status='Ready to move')
    in_3_years_projects = PlotsProjectDetail.objects.filter(developers=developer_objects, possession_status='In 3 years')
    beyond_3_years_projects = PlotsProjectDetail.objects.filter(developers=developer_objects, possession_status='Beyond 3 years')
    source_objects=PlotsProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    floorplans = plot_objects.plotfloorplan_set.order_by('Configuration', 'sq_yd')
    configuration_data = {}
    
    for floorplan in floorplans:
        config = floorplan.Configuration
        sq_yd = floorplan.sq_yd
        image_url = floorplan.image.url

        if config not in configuration_data:
            configuration_data[config] = {}

        if sq_yd not in configuration_data[config]:
            configuration_data[config][sq_yd] = []

        configuration_data[config][sq_yd].append(image_url)
    return render(request,'plots_property.html',{'plots_details':plot_objects,"sources":source_objects,"detail":details,"logos":logo,"developers":developer_objects,"ready_to_move_projects": ready_to_move_projects,
        "in_3_years_projects": in_3_years_projects,
        "beyond_3_years_projects": beyond_3_years_projects,
        "floorplans":configuration_data})

def Flatmate_projects(request,product_name,product_id):
    url = reverse('flatmate_projects', kwargs={'product_id': product_id, 'product_name': product_name})
    flat_objects=FlatmateProjectDetail.objects.prefetch_related("flatmategallery_set","flatmatedetails_set","flatmateamenities_set","flatmatecommonrooms_set","flatmatehouserules_set").get(name=product_name)
    source_objects=FlatmateProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,'flatmate_property.html',{'flats_details':flat_objects,"sources":source_objects,"detail":details,"logos":logo})

def Flatmateprojects(request,product_name):
    flat_objects=FlatmateProjectDetail.objects.prefetch_related("flatmategallery_set","flatmatedetails_set","flatmateamenities_set","flatmtecommonrooms_set","flatmatehouserules_set").get(name=product_name)
    source_objects=FlatmateProjectDetail.objects.order_by("-id")[:3]
    details=Contact_Details.objects.first()
    logo=Logo.objects.first()
    return render(request,'flatmate_property.html',{'flats_details':flat_objects,"sources":source_objects,"detail":details,"logos":logo})




# @csrf_protect
# @login_required(login_url='login')
# def save_project(request):
#     if request.method == 'POST':
        
#         project_id = request.POST.get('project_id')
#         content_type = request.POST.get('content_type')
#         action = request.POST.get('action') 
#         user = request.user

#         try:
#             content_type = ContentType.objects.get(app_label='housingapp', model="content_type")
#             project_model = content_type.model_class()
            
#             project = get_object_or_404(project_model, id=project_id)

#             if action == 'like':
#                 SavedProperty.objects.get_or_create(user=user, content_type=content_type, object_id=project_id)
#             elif action == 'unlike':
#                 SavedProperty.objects.filter(user=user, content_type=content_type,object_id=project_id).delete()

#             return JsonResponse({'success': True})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error_message': str(e)})



@csrf_protect
@login_required(login_url='login')
def like_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        action = request.POST.get('action')  # Get the action ('like' or 'unlike')
        user = request.user

        try:
            project = get_object_or_404(ProjectDetail, id=project_id)

            if action == 'like':
                LikedProject.objects.create(user=user, project=project)
            elif action == 'unlike':
                LikedProject.objects.filter(user=user, project=project).delete()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error_message': str(e)})
        
@csrf_protect
@login_required(login_url='login')
def rent_like_project(request):
    if request.method == 'POST':

        project_id = request.POST.get('project_id')
        action = request.POST.get('action')  # Get the action ('like' or 'unlike')
        user = request.user

        try:
            project = get_object_or_404(RentProjectDetail, id=project_id)

            if action == 'like':
                RentLikedProject.objects.create(user=user, project=project)
            elif action == 'unlike':
                RentLikedProject.objects.filter(user=user, project=project).delete()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error_message': str(e)})
        
@csrf_protect
@login_required(login_url='login')
def commercial_like_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        action = request.POST.get('action')  # Get the action ('like' or 'unlike')
        user = request.user

        try:
            project = get_object_or_404(CommercialProjectDetail, id=project_id)

            if action == 'like':
                CommercialLikedProject.objects.create(user=user, project=project)
            elif action == 'unlike':
                CommercialLikedProject.objects.filter(user=user, project=project).delete()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error_message': str(e)})
        
@csrf_protect
@login_required(login_url='login')
def plot_like_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        action = request.POST.get('action')  # Get the action ('like' or 'unlike')
        user = request.user

        try:
            project = get_object_or_404(PlotsProjectDetail, id=project_id)

            if action == 'like':
                PlotLikedProject.objects.create(user=user, project=project)
            elif action == 'unlike':
                PlotLikedProject.objects.filter(user=user, project=project).delete()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error_message': str(e)})
        
@login_required(login_url='login')
def delete_project(request, project_id):
    user = request.user
    project = ProjectDetail.objects.get(pk=project_id)

    try:
        saved_project = LikedProject.objects.get(user=user, project=project)
        saved_project.delete()
        return JsonResponse({'success': True})
    except LikedProject.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Project not found in saved properties.'})

# @login_required(login_url='login')
def rent_delete_project(request, project_id):

    user = request.user
    project = RentProjectDetail.objects.get(pk=project_id)

    try:
        saved_project = RentLikedProject.objects.get(user=user, project=project)
        saved_project.delete()
        return JsonResponse({'success': True})
    except LikedProject.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Project not found in saved properties.'})

@login_required(login_url='login')
def commercial_delete_project(request, project_id):
    user = request.user
    project = CommercialProjectDetail.objects.get(pk=project_id)

    try:
        saved_project = CommercialLikedProject.objects.get(user=user, project=project)
        saved_project.delete()
        return JsonResponse({'success': True})
    except LikedProject.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Project not found in saved properties.'})


@login_required(login_url='login')
def plot_delete_project(request, project_id):
    user = request.user
    project = PlotsProjectDetail.objects.get(pk=project_id)

    try:
        saved_project = PlotLikedProject.objects.get(user=user, project=project)
        saved_project.delete()
        return JsonResponse({'success': True})
    except LikedProject.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Project not found in saved properties.'})





# @csrf_protect
# @login_required(login_url='login')
# def save_project(request):
#     if request.method == 'POST':
#         project_id = request.POST.get('project_id')
#         project_type = request.POST.get('project_type')
#         action = request.POST.get('action')  
#         user = request.user

#         try:
#             saved_project = get_object_or_404(SavedProject, user=user)
#             # Determine the project type and update the corresponding field
#             if project_type == ProjectDetail:
#                 project_field = ProjectDetail
#             elif project_type == :
#                 project_field = 'rentproject'
#             elif project_type == 'commercialproject':
#                 project_field = 'commercialproject'
#             elif project_type == 'plotsproject':
#                 project_field = 'plotsproject'
#             else:
#                 return JsonResponse({'success': False, 'error_message': 'Invalid project type'})

#             # Determine the action and update the saved project
#             if action == 'like':
#                 setattr(saved_project, project_field, project_id)
#             elif action == 'unlike':
#                 setattr(saved_project, project_field, None)

#             saved_project.save()

#             return JsonResponse({'success': True})
#         except SavedProject.DoesNotExist:
#             return JsonResponse({'success': False, 'error_message': 'SavedProject not found for the user'})

#     return JsonResponse({'success': False, 'error_message': 'Invalid request method'})



def saved_properties(request):
    threshold_datetime = timezone.now() - timezone.timedelta(minutes=30)
    
    # Filter and delete expired saved properties
    LikedProject.objects.filter(saved_at__lt=threshold_datetime).delete()
    RentLikedProject.objects.filter(saved_at__lt=threshold_datetime).delete()
    CommercialLikedProject.objects.filter(saved_at__lt=threshold_datetime).delete()
    PlotLikedProject.objects.filter(saved_at__lt=threshold_datetime).delete()
    
    if request.user.is_authenticated:
        # Continue with your view logic to display saved properties
        saved_properties = LikedProject.objects.filter(user=request.user)
        rent_saved_properties = RentLikedProject.objects.filter(user=request.user)
        commercial_saved_properties = CommercialLikedProject.objects.filter(user=request.user)
        plot_saved_properties = PlotLikedProject.objects.filter(user=request.user)

        details = Contact_Details.objects.first()
        logo = Logo.objects.first()

        return render(request, 'saved_properties.html', {
            'saved_properties': saved_properties,
            'rent_saved_properties': rent_saved_properties,
            'commercial_saved_properties': commercial_saved_properties,
            'plot_saved_properties': plot_saved_properties,
            'logos': logo,
            'detail': details
        })
    else:
        # User is not authenticated, display a message or handle as per your requirement
        details = Contact_Details.objects.first()
        logo = Logo.objects.first()

        return render(request, 'saved_properties.html', {
            'logos': logo,
            'detail': details,
            'no_saved_properties_message': 'You need to be logged in to view saved properties.'
        })
# views.py
import random
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import PhoneOTP


def send_otp(request):
    if request.method == 'POST':

        phone_number = request.POST.get('phone_number')

        # Generate a random 6-digit OTP
        otp = ''.join(random.choices('0123456789', k=6))
        
        # Store the OTP in the session for later verification
        request.session['otp'] = otp

        # Save the phone number and OTP to the database
        user_profile, created = PhoneOTP.objects.get_or_create(phone_number=phone_number)
        user_profile.otp = otp
        user_profile.save()

        # Replace with your Textlocal sender ID
        sender_id = 'YOUR_SENDER_ID'

        # Textlocal API endpoint for sending WhatsApp messages
        api_url = "https://api.textlocal.in/sendwhatsapp/"

        # Prepare the data to send in the request
        data = {
            'apikey': settings.YOUR_API_KEY,
            'number':  phone_number,
            'message': f'Your OTP is: {otp}',
            'sender': sender_id,
        }
        print(data)
        # Send the OTP via WhatsApp using Textlocal API
        response = requests.post(api_url, data=data)

        if response.status_code == 200:
            return JsonResponse({'message': 'OTP sent successfully.'})
        else:
            return JsonResponse({'message': 'Failed to send OTP.'})

def verify_otp(request):
    if request.method == 'POST':
        user_input_otp = request.POST.get('otp')
        # Retrieve the OTP from the session
        stored_otp = request.session.get('otp', '')

        if user_input_otp == stored_otp:
            return JsonResponse({'message': 'OTP verification successful.'})
        else:
            return JsonResponse({'message': 'OTP verification failed.'})
        

        
def phone_number_entry(request):
    return render(request, 'send_otp_form.html')

def otp_login(request):
    return render(request, 'otp_input.html')

def otp_success(request):
    return render(request, 'otp_verified.html')

def otp_failure(request):
    return render(request, 'otp_failed.html')


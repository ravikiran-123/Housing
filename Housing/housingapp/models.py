from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User,Group,Permission
import uuid
from ckeditor.fields import RichTextField
from embed_video.fields  import  EmbedVideoField
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# from multiselectfield import MultiSelectField
# Create your models here.

# class Profile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
#     phone_number=models.CharField(max_length=13)
#     otp=models.CharField(max_length=100,null=True,blank=True)
#     uid=models.UUIDField(default=uuid.uuid4)

class Banner(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.ImageField(blank=False,null=False, upload_to='Banner_images')

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_builder = models.BooleanField(default=False)
    is_flatmate = models.BooleanField(default=False)

    class Meta:
        permissions = []



class PhoneOTP(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)



class RecentSearch(models.Model):
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
    
class Enquiry_Form(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=40,default="")
    message=models.TextField(blank=False,null=False,default="")

    def __str__(self):
        return self.name
    
class DownloadForm(models.Model):
    name=models.CharField(max_length=40,blank=False)
    Mobile_number = models.CharField(max_length=12,blank=True)
    email = models.EmailField(max_length=40,default="")
    

    def __str__(self):
        return self.name

class CommentForm(models.Model):
    name = models.CharField(max_length=20, default="")
    Mobile_number = models.CharField(max_length=10,blank=True)
    email = models.EmailField(max_length=40,default="")
    message=models.TextField(blank=False,null=False,default="")

    def __str__(self):
        return self.name

class Logo(models.Model):
    image=models.ImageField(blank=True,null=True,upload_to='Logo_images')

    def __str__(self):
        return "Logo"
    
class Contact_Details(models.Model):
    address = models.CharField(max_length=100, default="")
    Mobile_number = models.CharField(max_length=13,blank=True)
    email = models.EmailField(max_length=40,default="")
    map=models.TextField(blank=False,null=False)

    def __str__(self):
        return self.address




News_choices={
    ('Buy','Buy'),
    ('Rent','Rent'),
    ('Commercial','Commercial'),
    ('Plots','Plots'),
}

Developer_choices={
    ('Buy','Buy'),
    ('Plots','Plots'),
}
    
status_choices={
    ('Ready to move','Ready to move'),
    ('In 3 years','In 3 years'),
    ('Beyond 3 years','Beyond 3 years')

}
Section_choices={
    ('In Spotlight','In Spotlight'),
    ('TopProjects','TopProjects'),
    ('RecentlyAdded','RecentlyAdded'),
    ('Featured Projects','Featured Projects'),
    ('Projects in Focus','Projects in Focus'),
    ('Trending Projects','Trending Projects'), 
    ('Featured Colletions','Featured Colletions'),
    ('Featured Developers','Featured Developers ')
}

configuration_choices={
    ('1BHK','1BHK'),
    ('2BHK','2BHK'),
    ('3BHK','3BHK'),
    ('4BHK','4BHK'),
}

House_choices = (
        ('Apartment', 'Apartment'),
        ('Independent Floor', 'Independent Floor'),
        ('Independent House', 'Independent House'),
        ('Villa', 'Villa'),
 )

class DeveloperDetails(models.Model):
    developer_type=models.CharField(max_length=20,choices=Developer_choices, default='Buy')
    image=models.ImageField(blank=False,null=False,upload_to='Developer_images')
    developer_name=models.CharField(max_length=100,blank=False)
    established_year=models.CharField(max_length=20)
    total_projects=models.CharField(max_length=10)
    city=models.CharField(max_length=40,blank=False,null=False)
    # area=models.CharField(max_length=30,blank=False,null=False)
    description=models.TextField(blank=False)

    def __str__(self):
        return self.developer_name


class Featuredcollections(models.Model):
    feature_type=models.CharField(max_length=20,choices=News_choices, default='Buy')
    image=models.ImageField(blank=False,null=False,upload_to='Developer_images')
    name=models.CharField(max_length=30,blank=False)
    Description=models.CharField(max_length=500,blank=False)

    def project_count(self):
        return self.projectdetail_set.count()

    def __str__(self):
        return self.name

class HousingExperts(models.Model):
    image=models.ImageField(blank=False,null=False,upload_to='Developer_images')
    developer_name=models.CharField(max_length=30,blank=False)
    established_year=models.CharField(max_length=20,blank=False)
    description=models.TextField(blank=False,null=False)
    total_projects=models.CharField(max_length=20,blank=False)
    city=models.CharField(max_length=40,blank=False,null=False)
    area=models.CharField(max_length=30,blank=False,null=False)
    is_buy = models.BooleanField(default=False)
    is_rent = models.BooleanField(default=False)
    is_commercial = models.BooleanField(default=False)
    is_plot = models.BooleanField(default=False)

   


    def __str__(self):
        return self.developer_name


class ProjectDetail(models.Model):
    Agent=models.ForeignKey(User,on_delete=models.CASCADE)
    Experts=models.ForeignKey(HousingExperts, on_delete=models.CASCADE)
    Features=models.ForeignKey(Featuredcollections, on_delete=models.CASCADE,related_name='project_details')
    developers=models.ForeignKey(DeveloperDetails, on_delete=models.CASCADE, related_name="developerdetails")
    Property_Type=models.CharField(max_length=20,  default="Residential")
    Looking_for = models.CharField(max_length=20, choices=House_choices, default="Apartment")
    possession_status=models.CharField(max_length=20,choices=status_choices, default='Ready to move')
    # project_type=models.CharField(max_length=20,choices=Section_choices, default='TopProjects')
    image=models.ImageField(blank=True,null=True,upload_to='residential_images')
    logo_image=models.ImageField(blank=True,null=True,upload_to='residential_images')
    name=models.CharField(max_length=100,blank=True,null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    developer_name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=2000,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    price=models.CharField(max_length=100,blank=True,null=True)
    Configuration=models.CharField(max_length=100,blank=True,null=True)
    Avg_price=models.CharField(max_length=100,blank=True,null=True)
    property_name=models.CharField(max_length=100,blank=True,null=True)
    amenities_name=models.CharField(max_length=100,blank=True,null=True)
    video_image=models.ImageField(blank=True,null=True,upload_to='video_images')
    video=models.TextField(blank=False,null=False,default='https://www.youtube.com/embed/tgbNymZ7vqY')
    map_location=models.CharField(max_length=100,blank=True,null=True)
    lc_map=models.TextField(blank=False, default="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3806.012976551304!2d78.429541!3d17.459093!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xd4a220dc7610156d!2sBrigade%20Citadel!5e0!3m2!1sen!2sin!4v1632476420684!5m2!1sen!2sin&rel=0")
    locality_video=models.TextField(blank=False,null=False,default='https://www.youtube.com/embed/tgbNymZ7vqY')
    locality_description=models.TextField(blank=True,null=True)
    masterplan=models.ImageField(blank=True,null=True,upload_to='masterplan_images')
    brouchure_image1=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    brouchure_image2=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    brouchure_image3=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    brouchure_image4=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    brouchure_image5=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    File_upload=models.FileField(blank=False,upload_to='Files')
    is_active = models.BooleanField(verbose_name="Is Active?",default=False)
    is_featured = models.BooleanField(verbose_name="Is Featured?",default=False)
    is_sale= models.BooleanField(verbose_name="Is Sale?",default=False)


    class Meta:
        permissions = (("can_publish_projectdetail", "Can publish project detail"),
        # You can add other custom permissions as required
        )
        
    def __str__(self):
        return self.name

class Gallery(models.Model):
    project_details=models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='gallery_images')

class Details(models.Model):
    project_details=models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(blank=True,null=True)

class Amenities(models.Model):
    project_details=models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='Amenities_images')
    name=models.CharField(max_length=100,blank=True,null=True)
    # description=models.TextField(blank=True,null=True)


class FloorPlan(models.Model):
    project_details=models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    Configuration = models.CharField(max_length=20, choices=configuration_choices, default="1BHK")
    sq_ft=models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(blank=True,null=True,upload_to='floorplan_images')
    

    def __str__(self):
        return self.Configuration


class ProjectAdvantages(models.Model):
    project_details=models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,blank=True,null=True)
    content1=models.CharField(max_length=100,blank=True,null=True)
    content2=models.CharField(max_length=100,blank=True,null=True)
    content3=models.CharField(max_length=100,blank=True,null=True)

class FAQ(models.Model):
    project_details=models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,blank=True,null=True)
    Description=RichTextField(blank=True,null=True)



    


"""Rent page Model"""
 
class RentProjectDetail(models.Model):
    Agent=models.ForeignKey(User,on_delete=models.CASCADE)
    Experts=models.ForeignKey(HousingExperts, on_delete=models.CASCADE)
    Features=models.ForeignKey(Featuredcollections, on_delete=models.CASCADE)
    Property_Type = models.CharField(max_length=20, default="Residential")
    Looking_for = models.CharField(max_length=20, choices=House_choices, default="Apartment")
    image=models.ImageField(blank=True,null=True,upload_to='rent_images')
    logo_image=models.ImageField(blank=True,null=True,upload_to='rent_images')
    name=models.CharField(max_length=100,blank=True,null=True)
    sub_title=models.CharField(max_length=100,blank=True,null=True)
    developer_name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=2000,blank=True,null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    address=models.TextField(blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    price=models.CharField(max_length=100,blank=True,null=True)
    Configuration=models.CharField(max_length=100,blank=True,null=True)
    amenities_name=models.CharField(max_length=100,blank=True,null=True)
    map_location=models.CharField(max_length=100,blank=True,null=True)
    lc_map=models.TextField(blank=False, default="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3806.012976551304!2d78.429541!3d17.459093!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xd4a220dc7610156d!2sBrigade%20Citadel!5e0!3m2!1sen!2sin!4v1632476420684!5m2!1sen!2sin&rel=0")
    locality_video=models.TextField(blank=False,null=False,default='https://www.youtube.com/embed/tgbNymZ7vqY')
    locality_description=models.TextField(blank=True,null=True)

    class Meta:
        permissions = (("can_publish_rentprojectdetail", "Can publish rent project detail"),
        # You can add other custom permissions as required
        )  

    def __str__(self):
        return self.name

class RentGallery(models.Model):
    rent_details=models.ForeignKey(RentProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='gallery_images')

    def __str__(self):
        return 'RENTGALLERY'

class RentDetails(models.Model):
    rent_details=models.ForeignKey(RentProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


class RentAmenities(models.Model):
    rent_details=models.ForeignKey(RentProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='Amenities_images')
    name=models.CharField(max_length=100,blank=True,null=True)
    # description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class RentFurnishings(models.Model):
    rent_details=models.ForeignKey(RentProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='Furnishings_images')
    name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name





commercial_choices = (
        ('Office', 'Office'),
        ('Retail Shop', 'Retail Shop'),
        ('Ware House', 'Ware House'),
        ('Showroom ', 'Showroom'),
 )

"""Commercial Page Models Start"""


Section2_choices={
    ('Recently Added properties for sale','Recently Added properties for sale'),
    ('Recently Added properties for Rent','Recently Added properties for Rent'),
}

class CommercialProjectDetail(models.Model):
    Agent=models.ForeignKey(User,on_delete=models.CASCADE)
    Experts=models.ForeignKey(HousingExperts, on_delete=models.CASCADE)
    Features=models.ForeignKey(Featuredcollections, on_delete=models.CASCADE)
    Property_Type = models.CharField(max_length=20, default="Commercial")
    Looking_for = models.CharField(max_length=20, choices=commercial_choices, default="Office")
    commercial_type=models.CharField(max_length=40,choices=Section2_choices, default='Recently Added properties for sale')
    image=models.ImageField(blank=True,null=True,upload_to='Commercial_images')
    logo_image=models.ImageField(blank=True,null=True,upload_to='Commercial_images')
    main_title=models.CharField(max_length=100,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    developer_name=models.CharField(max_length=100,blank=True,null=True)
    # year_estd=RichTextField(max_length=100,blank=True,null=True)
    # no_of_projects=RichTextField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=2000,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    price=models.CharField(max_length=100,blank=True,null=True)
    Configuration=models.CharField(max_length=100,blank=True,null=True)
    Avg_price=models.CharField(max_length=100,blank=True,null=True)
    # property_name=models.CharField(max_length=100,blank=True,null=True)
    # amenities_name=models.CharField(max_length=100,blank=True,null=True)
    # video_image=models.ImageField(blank=True,null=True,upload_to='video_images')
    # video=models.TextField(blank=False,null=False,default='https://www.youtube.com/embed/tgbNymZ7vqY')
    # map_location=models.CharField(max_length=100,blank=True,null=True)
    # lc_map=models.TextField(blank=False, default="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3806.012976551304!2d78.429541!3d17.459093!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xd4a220dc7610156d!2sBrigade%20Citadel!5e0!3m2!1sen!2sin!4v1632476420684!5m2!1sen!2sin&rel=0")
    # brouchure_image1=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    # brouchure_image2=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    # brouchure_image3=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    # brouchure_image4=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    # brouchure_image5=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    # File_upload=models.FileField(blank=False,upload_to='Files')

    class Meta:
        permissions = (("can_publish_commercialprojectdetail", "Can publish commercial project detail"),
        # You can add other custom permissions as required
        )


    def __str__(self):
        return self.name

class CommercialGallery(models.Model):
    commercial_details=models.ForeignKey(CommercialProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='gallery_images')

class CommercialDetails(models.Model):
    commercial_details=models.ForeignKey(CommercialProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(blank=True,null=True)

class CommercialAmenities(models.Model):
    commercial_details=models.ForeignKey(CommercialProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='Amenities_images')
    name=models.CharField(max_length=100,blank=True,null=True)
    # description=models.TextField(blank=True,null=True)

# class CommercialFloorPlan(models.Model):
#     plot_details=models.ForeignKey(CommercialProjectDetail, on_delete=models.CASCADE)
#     image=models.ImageField(blank=True,null=True,upload_to='floorplan_images')

# class CommercialAdvantages(models.Model):
#     plot_details=models.ForeignKey(CommercialProjectDetail, on_delete=models.CASCADE)
#     title=models.CharField(max_length=100,blank=True,null=True)
#     content1=models.CharField(max_length=100,blank=True,null=True)
#     content2=models.CharField(max_length=100,blank=True,null=True)
#     content3=models.CharField(max_length=100,blank=True,null=True)

# class CommercialReviews(models.Model):
#     plot_details=models.ForeignKey(CommercialProjectDetail, on_delete=models.CASCADE)
#     image=models.ImageField(blank=True,null=True,upload_to='Reviews_images')
#     image1=models.ImageField(blank=True,null=True,upload_to='Reviews_images')
#     title=models.CharField(max_length=100,blank=True,null=True)
#     date=models.CharField(max_length=100,blank=True,null=True)
#     description=models.TextField(blank=True,null=True)


"""Plots page Models Start"""


plot_choices = (
    ('Plots', 'Plots'),
    ('Agricultural Lands', 'Agricultural Lands'),
 )




class PlotsProjectDetail(models.Model):
    Agent=models.ForeignKey(User,on_delete=models.CASCADE)
    Experts=models.ForeignKey(HousingExperts, on_delete=models.CASCADE)
    Features=models.ForeignKey(Featuredcollections, on_delete=models.CASCADE)
    developers=models.ForeignKey(DeveloperDetails, on_delete=models.CASCADE)
    Property_Type = models.CharField(max_length=20, choices=plot_choices, default="Office")   
    possession_status=models.CharField(max_length=20,choices=status_choices, default='Ready to move')
    image=models.ImageField(blank=True,null=True,upload_to='plot_images')
    logo_image=models.ImageField(blank=True,null=True,upload_to='plot_images')
    name=models.CharField(max_length=100,blank=True,null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    developer_name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=2000,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    price=models.CharField(max_length=100,blank=True,null=True)
    Configuration=models.CharField(max_length=100,blank=True,null=True)
    Avg_price=models.CharField(max_length=100,blank=True,null=True)
    property_name=models.CharField(max_length=100,blank=True,null=True)
    amenities_name=models.CharField(max_length=100,blank=True,null=True)
    masterplan=models.ImageField(blank=True,null=True,upload_to='masterplan_images')
    video_image=models.ImageField(blank=True,null=True,upload_to='video_images')
    video=models.TextField(blank=False,null=False,default='https://www.youtube.com/embed/tgbNymZ7vqY')
    map_location=models.CharField(max_length=100,blank=True,null=True)
    lc_map=models.TextField(blank=False, default="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3806.012976551304!2d78.429541!3d17.459093!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xd4a220dc7610156d!2sBrigade%20Citadel!5e0!3m2!1sen!2sin!4v1632476420684!5m2!1sen!2sin&rel=0")
    locality_video=models.TextField(blank=False,null=False,default='https://www.youtube.com/embed/tgbNymZ7vqY')
    locality_description=models.TextField(blank=True,null=True)
    brouchure_image1=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    brouchure_image2=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    brouchure_image3=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    brouchure_image4=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    brouchure_image5=models.ImageField(blank=True,null=True,upload_to='brouchure_images')
    File_upload=models.FileField(blank=False,upload_to='Files')
    is_active = models.BooleanField(verbose_name="Is Active?",default=False)
    is_featured = models.BooleanField(verbose_name="Is Featured?",default=False)
    is_sale= models.BooleanField(verbose_name="Is Sale?",default=False)

    class Meta:
        permissions = (("can_publish_plotsprojectdetail", "Can publish plots project detail"),
        # You can add other custom permissions as required
        )

    def __str__(self):
        return self.name

class PlotGallery(models.Model):
    plot_details=models.ForeignKey(PlotsProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='gallery_images')

class PlotDetails(models.Model):
    plot_details=models.ForeignKey(PlotsProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(blank=True,null=True)

class PlotAmenities(models.Model):
    plot_details=models.ForeignKey(PlotsProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='Amenities_images')
    name=models.CharField(max_length=100,blank=True,null=True)
    

class PlotFloorPlan(models.Model):
    plot_details=models.ForeignKey(PlotsProjectDetail, on_delete=models.CASCADE)
    Configuration = models.CharField(max_length=20,  default="Residential Plot")
    sq_yd=models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(blank=True,null=True,upload_to='floorplan_images')
    

    def __str__(self):
        return self.Configuration

class PlotAdvantages(models.Model):
    plot_details=models.ForeignKey(PlotsProjectDetail, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,blank=True,null=True)
    content1=models.CharField(max_length=100,blank=True,null=True)
    content2=models.CharField(max_length=100,blank=True,null=True)
    content3=models.CharField(max_length=100,blank=True,null=True)

class PlotFAQ(models.Model):
    plot_details=models.ForeignKey(PlotsProjectDetail, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,blank=True,null=True)
    Description=RichTextField(blank=True,null=True)

    
flatmate_options={
    ("Boys","Boys"),
    ("Girls","Girls"),
    ("Food Available","Food Available"),
    ("Private Room","Private Room")
}

class FlatmateChoice(models.Model):
    flatmate_choices = models.CharField(max_length=20, choices=flatmate_options, default="Boys")   
    image=models.ImageField(blank=False,null=False,upload_to='Flat_images')

    def __str__(self):
        return self.flatmate_choices

class FlatmateProjectDetail(models.Model):
    Agent=models.ForeignKey(User,on_delete=models.CASCADE)
    Flatmates=models.ForeignKey(FlatmateChoice, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='flat_images')
    logo_image=models.ImageField(blank=True,null=True,upload_to='flat')
    name=models.CharField(max_length=100,blank=True,null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    project_by=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    price=models.CharField(max_length=100,blank=True,null=True)
    sharing=models.CharField(max_length=100,blank=True,null=True)
    lc_map=models.TextField(blank=False, default="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3806.012976551304!2d78.429541!3d17.459093!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xd4a220dc7610156d!2sBrigade%20Citadel!5e0!3m2!1sen!2sin!4v1632476420684!5m2!1sen!2sin&rel=0")


    class Meta:
        permissions = (("can_publish_flatmateprojectdetail", "Can publish flatmate project detail"),
        # You can add other custom permissions as required
        )

    def __str__(self):
        return self.name
    

class FlatmateGallery(models.Model):
    flatmate_details=models.ForeignKey(FlatmateProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='gallery_images')

class FlatmateDetails(models.Model):
    flatmate_details=models.ForeignKey(FlatmateProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(blank=True,null=True)

class FlatmateAmenities(models.Model):
    flatmate_details=models.ForeignKey(FlatmateProjectDetail, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,upload_to='Amenities_images')
    name=models.CharField(max_length=100,blank=True,null=True)

class FlatmateCommonRooms(models.Model):
    flatmate_details=models.ForeignKey(FlatmateProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)

class FlatmateHouseRules(models.Model):
    flatmate_details=models.ForeignKey(FlatmateProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)

""" News pages Model Start"""

class NewsDetails(models.Model):
    main_title=models.CharField(max_length=500,blank=False,null=False)
    image=models.ImageField(blank=False,null=False,upload_to='News_images')
    name=models.CharField(max_length=500,blank=False,null=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    article_by=models.CharField(max_length=40,blank=False,null=False)
    description=RichTextField(blank=False,null=False)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    details=models.ForeignKey(NewsDetails, on_delete=models.CASCADE)
    image=models.ImageField(blank=False,null=False,upload_to='News_images')
    name=models.CharField(max_length=500,blank=False,null=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    description=RichTextField(blank=False,null=False)

# class NewsArticles(models.Model):
#     details=models.ForeignKey(NewsDetails, on_delete=models.CASCADE)
#     image=models.ImageField(blank=False,null=False,upload_to='News_images')
#     title=RichTextField(blank=False,null=False)
#     description=RichTextField(blank=False,null=False)
#     article_by=models.CharField(max_length=40,blank=False,null=False)
#     list_date = models.DateTimeField(default=datetime.now, blank=True)

class LikedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

class RentLikedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(RentProjectDetail, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

class CommercialLikedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(CommercialProjectDetail, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

class PlotLikedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(PlotsProjectDetail, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)




class SavedProperty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    saved_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project_details=models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=40,default="")

    def __str__(self):
        return self.name
    
class RentContact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rentproject_details=models.ForeignKey(RentProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=40,default="")

    def __str__(self):
        return self.name

class CommercialContact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    commercialproject_details=models.ForeignKey(CommercialProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=40,default="")

    def __str__(self):
        return self.name
    
class PlotContact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    plotsproject_details=models.ForeignKey(PlotsProjectDetail, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=40,default="")

    def __str__(self):
        return self.name
    
class HousingContact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    housing_experts=models.ForeignKey(HousingExperts, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=40,default="")

    def __str__(self):
        return self.name
    

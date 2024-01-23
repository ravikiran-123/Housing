from django.contrib import admin
from .models import *
from .views import *
from django.forms import SelectMultiple
from django import forms


# Register your models here.
admin.site.register(Banner)
admin.site.register(User)

class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 1

class NewsDetailsAdmin(admin.ModelAdmin):
    inlines = [CommentsInline,]

class GalleryImagesInline(admin.StackedInline):
    model = Gallery
    extra = 1   

class ProjectAdvantagesInline(admin.StackedInline):
    model = ProjectAdvantages
    extra = 1

class DetailsInline(admin.StackedInline):
    model = Details
    extra = 1

class AmenitiesInline(admin.StackedInline):
    model = Amenities
    extra = 1




class FloorPlanInline(admin.StackedInline):
    model = FloorPlan



class FAQInline(admin.StackedInline):
    model = FAQ
    extra = 1

# class HousingExpertInline(admin.StackedInline):
#     model = HousingExperts
#     extra = 1 

class ProjectDetailInline(admin.StackedInline):
    model = ProjectDetail
    extra = 1

class RentProjectDetailInline(admin.StackedInline):
    model = RentProjectDetail
    extra = 1

class CommercialProjectDetailInline(admin.StackedInline):
    model = CommercialProjectDetail
    extra = 1

class PlotsProjectDetailInline(admin.StackedInline):
    model = PlotsProjectDetail
    extra = 1

# class HousingExpertsAdmin(admin.ModelAdmin):
#     def formfield_for_dbfield(self, db_field, request, **kwargs):
#         if db_field.name == 'expert_type':
#             kwargs['widget'] = SelectMultiple(attrs={'size': 5})  # You can customize 'size' as needed
#         return super().formfield_for_dbfield(db_field, request, **kwargs)


class ProjectDetailAdmin(admin.ModelAdmin):
    
    inlines = [GalleryImagesInline,DetailsInline,AmenitiesInline,FloorPlanInline,FAQInline]
    
    def get_queryset(self, request):
        qs = super(ProjectDetailAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Agent=request.user)
    
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "Agent":
            kwargs["initial"] = request.user.id
              # Set the initial value to the currently logged-in user
            kwargs["queryset"] = User.objects.filter(pk=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

   
    
   



class RentGalleryImagesInline(admin.StackedInline):
    model = RentGallery
    extra = 1

class RentFurnishingsInline(admin.StackedInline):
    model = RentFurnishings
    extra = 1

class RentDetailsInline(admin.StackedInline):
    model = RentDetails
    extra = 1

class RentAmenitiesInline(admin.StackedInline):
    model = RentAmenities
    extra = 1

class RentProjectDetailAdmin(admin.ModelAdmin):
    inlines = [RentGalleryImagesInline,RentDetailsInline,RentAmenitiesInline,RentFurnishingsInline,]

    def get_queryset(self, request):
        qs = super(RentProjectDetailAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Agent=request.user)
    
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "Agent":
            kwargs["initial"] = request.user.id 
            kwargs["queryset"] = User.objects.filter(pk=request.user.id) # Set the initial value to the currently logged-in user
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    


class PlotAmenitiesInline(admin.StackedInline):
    model = PlotAmenities
    extra = 1

class PlotGalleryImagesInline(admin.StackedInline):
    model = PlotGallery
    extra = 1

class PlotAdvantagesInline(admin.StackedInline):
    model = PlotAdvantages
    extra = 1
    
class PlotDetailsInline(admin.StackedInline):
    model = PlotDetails
    extra = 1

class PlotFloorPlanInline(admin.StackedInline):
    model = PlotFloorPlan
    extra = 1

class PlotFAQInline(admin.StackedInline):
    model = PlotFAQ
    extra = 1


class PlotsProjectDetailAdmin(admin.ModelAdmin):
    inlines = [PlotGalleryImagesInline,PlotAdvantagesInline,PlotDetailsInline,PlotAmenitiesInline,PlotFloorPlanInline,PlotFAQInline]

    def get_queryset(self, request):
        qs = super(PlotsProjectDetailAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Agent=request.user)

        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "Agent":
            kwargs["initial"] = request.user.id 
            kwargs["queryset"] = User.objects.filter(pk=request.user.id) # Set the initial value to the currently logged-in user
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CommercialGalleryInline(admin.StackedInline):
    model = CommercialGallery
    extra = 1

class CommercialDetailsInline(admin.StackedInline):
    model = CommercialDetails
    extra = 1

class CommercialAmenitiesInline(admin.StackedInline):
    model = CommercialAmenities
    extra = 1



class CommercialProjectDetailAdmin(admin.ModelAdmin):
    inlines=[CommercialGalleryInline,CommercialDetailsInline,CommercialAmenitiesInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Agent=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "Agent":
            kwargs["initial"] = request.user.id 
            kwargs["queryset"] = User.objects.filter(pk=request.user.id) # Set the initial value to the currently logged-in user
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    

class FlatmateGalleryInline(admin.StackedInline):
    model = FlatmateGallery
    extra = 1

class FlatmateDetailsInline(admin.StackedInline):
    model = FlatmateDetails
    extra = 1

class FlatmateAmenitiesInline(admin.StackedInline):
    model = FlatmateAmenities
    extra = 1

class FlatmateCommonRoomsInline(admin.StackedInline):
    model = FlatmateCommonRooms
    extra = 1

class FlatmateHouseRulesInline(admin.StackedInline):
    model = FlatmateHouseRules
    extra = 1

class FlatmateProjectDetailAdmin(admin.ModelAdmin):
    inlines=[FlatmateGalleryInline,FlatmateDetailsInline,FlatmateAmenitiesInline,FlatmateCommonRoomsInline,FlatmateHouseRulesInline]





class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'email', 'project_name']

    def get_queryset(self, request):
        # Only show contact details for the projects added by the currently logged-in user
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Assuming the ProjectDetail model has a ForeignKey 'admin' field
        project_details_for_user = ProjectDetail.objects.filter(Agent=request.user)
        return qs.filter(project_details__in=project_details_for_user)

    def project_name(self, obj):
        return obj.project_details.name

    project_name.short_description = 'Project Name'

class RentContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'email', 'project_name']
    def get_queryset(self, request):
        # Only show contact details for the projects added by the currently logged-in user
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Assuming the ProjectDetail model has a ForeignKey 'admin' field
        rentproject_details_for_user = RentProjectDetail.objects.filter(Agent=request.user)
        return qs.filter(rentproject_details__in=rentproject_details_for_user)

    def project_name(self, obj):
        return obj.rentproject_details.name

    project_name.short_description = 'Project Name'

class CommercialContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'email', 'project_name']
    def get_queryset(self, request):
        # Only show contact details for the projects added by the currently logged-in user
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Assuming the ProjectDetail model has a ForeignKey 'admin' field
        commercialproject_details_for_user = CommercialProjectDetail.objects.filter(Agent=request.user)
        return qs.filter(commercialproject_details__in=commercialproject_details_for_user)

    def project_name(self, obj):
        return obj.commercialproject_details.name

    project_name.short_description = 'Project Name'

class PlotContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'email', 'project_name']
    def get_queryset(self, request):
        # Only show contact details for the projects added by the currently logged-in user
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Assuming the ProjectDetail model has a ForeignKey 'admin' field
        plotsproject_details_for_user = PlotsProjectDetail.objects.filter(Agent=request.user)
        return qs.filter(plotsproject_details__in=plotsproject_details_for_user)

    def project_name(self, obj):
        return obj.plotsproject_details.name

    project_name.short_description = 'Project Name'



#  class YourModelAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(author=request.user)
    
# class BuyModelAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(BuyModelAdmin,self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(author=request.user)


# admin.site.register(CommercialProjectDetail, YourModelAdmin)
# admin.site.register(ProjectDetail, BuyModelAdmin)
admin.site.register(FlatmateProjectDetail, FlatmateProjectDetailAdmin)
admin.site.register(FlatmateChoice)
admin.site.register(FloorPlan)
admin.site.register(NewsDetails, NewsDetailsAdmin)
admin.site.register(Logo)
# admin.site.register(Property_Type)
# admin.site.register(Properties)
admin.site.register(Contact_Details)
admin.site.register(HousingExperts)
admin.site.register(Featuredcollections)
admin.site.register(DeveloperDetails)
admin.site.register(Contact, ContactAdmin)
admin.site.register(RentContact, RentContactAdmin)
admin.site.register(CommercialContact, CommercialContactAdmin)
admin.site.register(PlotContact, PlotContactAdmin)
admin.site.register(Enquiry_Form)
admin.site.register(CommentForm)
admin.site.register(ProjectDetail,ProjectDetailAdmin)
admin.site.register(RentProjectDetail,RentProjectDetailAdmin)
admin.site.register(CommercialProjectDetail,CommercialProjectDetailAdmin)
admin.site.register(PlotsProjectDetail,PlotsProjectDetailAdmin)



@admin.register(DownloadForm)
class EnquiryAdmin(admin.ModelAdmin):
    list_display=('name','Mobile_number','email')
    ordering=('name',)
    search_fields=('name',)
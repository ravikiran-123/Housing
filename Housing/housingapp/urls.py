from django.urls import path
from django.contrib.auth.views import LogoutView
from housingapp import views
# from.views import PropertyAutocompleteView
from django.conf import settings


urlpatterns = [
    path('housing/',views.home, name='home'),
    # path('housing/home/',views.home, name='home'),
    path('base/',views.Base,name='Base'),
    path('housing/rent/',views.rent,name='rent'),
    path('housing/commercial/',views.Commercial,name='Commercial'),
    path('housing/plots/',views.Plots,name='plots'),
    path('flatmates/',views.Flatmate,name='flatmates'),
    path('housing/properties/',views.list_property,name="list_property"),
    path('housing/news/', views.All_News,name='all_news'),
    path('housing/details/<str:product_name>/',views.News_details,name='News_details'),
    path('housing/details/<str:product_name>/details/<int:product_id>/',views.News,name='News'),
    path('housing/rent/details/<str:product_name>/',views.News_details,name='News_details'),
    path('housing/commercial/details/<str:product_name>/',views.News_details,name='News_details'),
    path('housing/plots/details/<str:product_name>/',views.News_details,name='News_details'),
    path('flatmate/details/<str:product_name>/',views.News_details,name='News_details'),
    path('housing/projects/<str:product_name>/',views.Buy_projects,name='Buy_projects'),
    path('housing/Buy/<str:product_name>/',views.projects,name='projects'),
    path('housing/experts/<int:product_id>/projects/<str:product_name>/',views.Buy_projects,name='Buy_projects'),
    path('housing/collections/<int:product_id>/projects/<str:product_name>/',views.Buy_projects,name='Buy_projects'),
    path('housing/developers/<int:product_id>/projects/<str:product_name>/',views.Buy_projects,name='Buy_projects'),
    path('housing/rent/leases/<str:product_name>/',views.rent_projects,name='rent_projects'),
    path('housing/rent/rents/<str:product_name>/',views.rent_houses,name='rent_houses'),
    path('housing/rent/rentexperts/<int:product_id>/leases/<str:product_name>/',views.rent_projects,name='rent_projects'),
    path('housing/rent/collections/<int:product_id>/leases/<str:product_name>/',views.rent_projects,name='rent_projects'),

    path('housing/commercial/projects/<str:product_name>/',views.Commercial_projects,name='commercial_projects'),
    path('housing/commercial/Features/<str:product_name>/',views.Commercial_Features,name='Commercial_Features'),
    path('housing/commercial/commercialexperts/<int:product_id>/projects/<str:product_name>/',views.Commercial_projects,name='commercial_projects'),
    path('housing/commercial/collections/<int:product_id>/projects/<str:product_name>/',views.Commercial_projects,name='commercial_projects'),

    path('housing/plots/residential-plots/<str:product_name>/',views.Plotprojects,name='Plotprojects'),
    path('housing/plots/residentialplots/<str:product_name>/',views.Plotprojects,name='Plotprojects'),
    path('housing/plots/plotsexperts/<int:product_id>/residential-plots/<str:product_name>/',views.Plots_projects,name='plots_projects'),
    path('housing/plots/collections/<int:product_id>/residential-plots/<str:product_name>/',views.Plots_projects,name='plots_projects'),
    path('housing/plots/plotsdevelopers/<int:product_id>/residential-plots/<str:product_name>/',views.Plots_projects,name='plots_projects'),

    path('flatmates/residential-flats/<str:product_name>/',views.Flatmateprojects,name='Flatmateprojects'),
    path('flatmates/residentialflats/<str:product_name>/',views.Flatmateprojects,name='Flatmateprojects'),
    path('flatmates/choices/<int:product_id>/residential-flats/<str:product_name>/',views.Flatmate_projects,name='flatmate_projects'),
   

    path('housing/collections/<int:product_id>/',views.BuyFeaturecollections,name='BuyFeaturecollections'),
    path('housing/rent/collections/<int:product_id>/',views.RentFeaturecollections,name='RentFeaturecollections'),
    path('housing/commercial/collections/<int:product_id>/',views.CommercialFeaturecollections,name='collections'),

    path('housing/rent/rents/<str:product_name>/collections/<int:product_id>/',views.Commercialcollections,name='collections'),
    path('housing/plots/collections/<int:product_id>/',views.PlotFeaturecollections,name='PlotFeaturecollections'),
    path('flatmates/choices/<int:product_id>/',views.FlatmatePageChoice,name='FlatmatePageChoice'),


    path('housing/experts/<str:product_name>/',views.Buypage_Experts, name="Experts"),
    path('housing/rent/rentexperts/<int:product_id>/',views.rentpage_Experts, name="RentExperts"),
    path('housing/commercial/commercialexperts/<int:product_id>/',views.commercialpage_Experts, name="CommercialExperts"),
    path('housing/plots/plotsexperts/<int:product_id>/',views.plotspage_Experts, name="PlotsExperts"),


    path('housing/properties/Buy/<str:product_name>/',views.projects, name="projects"),
    path('housing/properties/rents/<str:product_name>/',views.rent_houses, name="rent_houses"),
    path('housing/properties/Features/<str:product_name>/',views.Commercial_Features, name="Commercial_Features"),
    path('housing/properties/residentialplots/<str:product_name>/',views.Plotprojects, name="Plotprojects"),


    path('housing/developers/<int:product_id>/',views.BuypageDevelopers, name="BuypageDevelopers"),
    path('housing/plots/plotsdevelopers/<int:product_id>/',views.PlotpageDevelopers, name="PlotpageDevelopers"),

    path('housing/contact/',views.main_contact,name='contact'),
    path('housing/rentcontact/',views.main_RentContact,name='main_RentContact'),
    path('housing/commercialcontact/',views.main_CommercialContact,name='main_CommercialContact'),
    path('housing/plotcontact/',views.main_Plotcontact,name='main_Plotcontact'),
    path('housing/housingcontact/',views.main_Housingcontact,name='housingcontact'),
    path('housing/enquiry/',views.enquiry,name='enquiry'),
    path('housing/comment-form/',views.comment,name="comment-form"),
    path('housing/contactpage/',views.contactpage,name="contactpage"),
    path('housing/thank/', views.thank, name="thank"),
    path('housing/property-search/', views.search, name='property_search'),
    path('housing/property-search/Buy/<str:product_name>/',views.projects,name='projects'),
    # path('get_suggestions/', views.autocomplete_suggestions, name='get_suggestions'),
    # path('search_suggestions/', views.search_suggestions, name='search_suggestions'),

    # path('new-search/', views.new_search, name='search'),
    # path('residential/', views.add_residential, name='search'),
    path('housing/login/', views.login, name='login'),
    path('housing/register/', views.register, name='register'),
    path('housing/logout/', views.logout, name='logout'),
    # path('otp/<uid>/',views.otp,name='otp'),
    # path('housing/logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    # path('send-otp/', views.send_otp, name='send_otp'),
    # path('verify-otp/', views.verify_otp, name='verify_otp'),
    # path('housing/logout/', views.logout, name='login_view'),
    # path('register/', views.register_view, name='register_view'),
    path('housing/like_project/', views.like_project, name='like_project'),
    path('housing/rent_like_project/', views.rent_like_project, name='rent_like_project'),
    path('housing/commercial_like_project/', views.commercial_like_project, name='commercial_like_project'),
    path('housing/plot_like_project/', views.plot_like_project, name='plot_like_project'),
    path('housing/delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('housing/rent_delete_project/<int:project_id>/', views.rent_delete_project, name='rent_delete_project'),
    path('housing/commercial_delete_project/<int:project_id>/', views.commercial_delete_project, name='commercial_delete_project'),
    path('housing/plot_delete_project/<int:project_id>/', views.plot_delete_project, name='plot_delete_project'),
    path('housing/search/',views.searchProperty,name='searchProperty'),
    # path('housing/save_project/',views.save_project,name='save_project'),

    path('housing/send-otp/', views.send_otp, name='send-otp'),
    path('housing/verify-otp/', views.verify_otp, name='verify-otp'),
    path('housing/phone-entry/',views.phone_number_entry,name='phone_number_entry'),
    path('housing/otp-login/', views.otp_login, name='otp-login'),
    path('housing/success/', views.otp_success, name='otp-success'),
    path('housing/failure/', views.otp_failure, name='otp-failure'),
    path('housing/saved/', views.saved_properties, name='saved_properties'),
    path('housing/suggestions/',views.get_suggestions, name='get_suggestions'),


    path('housing/download_brochure/', views.download_brochure, name="download_brochure"),
    path('housing/plotdownload_brochure/', views.plotdownload_brochure, name="plotdownload_brochure"),


]
from django.urls import path
from . import views 

urlpatterns = [
    path('የ6ወር_ስኮርካርድ_እቅድ_ቅፅ/', views.የ6ወር_ስኮርካርድ_እቅድ_ቅፅ, name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ'),
    path('የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1/', views.የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1, name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1'),
    path('የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2/', views.የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2, name='የ6ወር_የባህሪ_ቅፅ_2'),
    path('የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3/', views.የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3, name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3'),
    path('የድርጊት_መርሃ_ግብር_ቅፅ/', views.የድርጊት_መርሃ_ግብር_ቅፅ, name='የድርጊት_መርሃ_ግብር_ቅፅ'),
    path('formAdd/', views.formAdd, name='formAdd'),
    path('formView/', views.formView, name='formView'),
    path('printForm/', views.printForm, name='printForm'),
    path('homepage/', views.homepage, name='homepage'),
    path('userList/', views.userList, name='userList'),
    path('deleteUser/<int:id>/', views.deleteUser, name='deleteUser'),
    path('editUser/<int:id>/', views.editUser, name='editUser'),
    # path('accommodation/', views.accommodation, name='accommodation'),
    # path('elements/', views.elements, name='elements'),
    # path('contact/', views.contact, name='contact'),
]
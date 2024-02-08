from django.urls import path
from . import views 

urlpatterns = [
    ## Admin ##
    path('admin-dashboard', views.admin_dashboard, name='admin-dashboard'),
    path('userList/', views.userList, name='userList'),
    path('deleteUser/<int:id>/', views.deleteUser, name='deleteUser'),
    path('editUser/<int:id>/', views.editUser, name='editUser'),

    ## Director ## 
    path('director-dashboard', views.director_index, name='director-dashboard'),

    ## Team Leader ##
    path('team-leader-dashboard', views.team_leader_index, name="team-leader-dashboard"),

    ## Expert ##
    path('', views.homepage, name='homepage'),

    ## የ6ወር ስኮርካርድ እቅድ ቅፅ ##
    path('Add_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ/', views.Add_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ, name='Add_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ'),
    path('View_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ/', views.View_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ, name='View_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ'),
    path('Print_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ/<int:form_id>', views.Print_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ, name='Print_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ'),

    ## የ6ወር የባህሪ መመዘኛ ቅፅ 1 ##
    path('Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1/', views.Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1, name='Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1'),
    path('View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1/', views.View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1, name='View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1'),
    path('Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1/<int:form_id>', views.Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1, name='Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1'),

    ## የ6ወር የባህሪ መመዘኛ ቅፅ 2 ##
    path('Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2/', views.Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2, name='Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2'),
    path('View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2/', views.View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2, name='View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2'),
    path('Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2/<int:form_id>', views.Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2, name='Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2'),

    ## የ6ወር የባህሪ መመዘኛ ቅፅ 3 ##
    path('Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3/', views.Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3, name='Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3'),
    path('View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3/', views.View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3, name='View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3'),
    path('Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3/<int:form_id>', views.Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3, name='Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3'),

    ## የድርጊት መርሃ ግብር ቅፅ
    path('Add_የድርጊት_መርሃ_ግብር_ቅፅ/', views.Add_የድርጊት_መርሃ_ግብር_ቅፅ, name='Add_የድርጊት_መርሃ_ግብር_ቅፅ'),
    path('View_የድርጊት_መርሃ_ግብር_ቅፅ/', views.View_የድርጊት_መርሃ_ግብር_ቅፅ, name='View_የድርጊት_መርሃ_ግብር_ቅፅ'),
    path('Print_የድርጊት_መርሃ_ግብር_ቅፅ/', views.Print_የድርጊት_መርሃ_ግብር_ቅፅ, name='Print_የድርጊት_መርሃ_ግብር_ቅፅ'),
]
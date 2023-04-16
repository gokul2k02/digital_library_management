from django.urls import path

from libraryapp import views

urlpatterns=[
    path('',views.login_fun,name='login'),
    path('log',views.readlog_fun),
    path('adminreg',views.adminreg_fun),
    path('adminread',views.adminread_fun),
    path('studentregone',views.stdregread_fun),
    path('studentreg',views.stdread_fun),
    path('addbk',views.addbk_fun,name='addbk'),
    path('readbook',views.readbook_fun),
    path('display',views.display_fun,name='dis'),
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out'),
    path('assign',views.assign_fun,name='assign'),
    path('assignread',views.assinred),
    path('sc',views.readassign_fun),
    path('display2',views.issuebk_fun,name='issuebk'),
    path('delete1/<int:id>',views.delete1_fun,name='del1'),
    path('vanish/<int:id>',views.update2_fun,name='up1'),
    path('stddisplay',views.call_fun,name='std_dis'),
    path('stdhome',views.stdhome_fun,name='std_home'),
    path('pro',views.profile_fun,name='pro'),
    path('prof',views.profupdate_fun,name='prof'),
    path('updatepro',views.updatepro_fun)

]
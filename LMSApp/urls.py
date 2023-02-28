from django.urls import path

from LMSApp import views

urlpatterns = [
    path('', views.home_fun, name='home'),
    path('adminreg', views.adminreg_fun, name='adminreg'),
    path('adminregread', views.adminregread_fun),
    path('studreg', views.studreg_fun, name='studreg'),
    path('studregread', views.studreread_fun, name='studregread'),
    path('readlog', views.readlog_fun),
    path('adminhome', views.adminhome_fun, name='adminhome'),
    path('resetpswd', views.resetpswd_fun, name='resetpswd'),
    path('addbook', views.addbook_fun, name='addbook'),
    path('readbook', views.readbook_fun, name='readbook'),
    path('displaybook', views.displaybook_fun, name='displaybook'),
    path('updatebook/<int:id>', views.update_book, name='updatebook'),
    path('deletebook/<int:id>', views.delete_book, name='deletebook'),
    path('issuebook', views.issuebook_fun, name='issuebook'),
    path('savebook', views.savebook_fun, name='savebook'),
    path('booksissued', views.booksissued_fun, name='booksissued'),
    path('updatebookissue/<int:id>', views.updatebookissue_fun, name='updatebookissue'),
    path('deletebookissue/<int:id>', views.deletebookissue_fun, name='deletebookissue'),
    path('admin_log_out', views.admin_log_out_fun, name='admin_log_out'),
    path('shome', views.shome_fun, name='shome'),
    path('sbooks', views.sbooks_fun, name='sbooks'),
    path('s_log_out', views.s_log_out_fun, name='s_log_out')
]

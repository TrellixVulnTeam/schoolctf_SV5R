from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from scorry import settings
from scorry_board import views

admin.autodiscover()

urlpatterns = [url(r'^$', views.index, name="scorry_index"),
#               url(r'^admin', redirect_to, {'url': '/admin/'}),
               url(r'^admin', include(admin.site.urls)),
               url(r'^summernote/', include('django_summernote.urls')),

               # login and registration urls
               url(r'^accounts/login/$', views.login_user, name="scorry_login"),
               url(r'^account/logout/$', views.logout_user, name="scorry_logout"),

               # news urls
               url(r'news/(\d{1,4})/$', views.detail_news, name="scorry_news"),
               url(r'scoreboard/', views.scoreboard, name="scoreboard"),

               # main urls
               url(r'tasks/$', views.tasks, name="scorry_tasks"),
               url(r'tasks/(\d{1,4})/$', views.task_detail, name="scorry_tasks_details"),
               url(r'tasks/solve/(\d{1,4})/$', views.task_solve, name="scorry_tasks_solve")
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = patterns('',
#(r'^one/$', redirect_to, {'url': '/another/'}),

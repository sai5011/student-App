from django.contrib import admin
from django.urls import path ,include

admin.site.site_header = "Student App Admin"
admin.site.site_title = "Student Admin Portal"
admin.site.index_title = "Welcome to Student App Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('student.urls'))
]

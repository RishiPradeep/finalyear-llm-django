from django.urls import path
from . import views

urlpatterns = [
    path("students",views.index,name="index"),
    path("faculty",views.facultyGet,name="getFaculty"),
    path("projects",views.projectsGet,name="getProjects"),
    path("papers",views.papersGet,name="getPapers"),
    path("feedback",views.feedbackGet,name="getFeedback")
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Faculty, Project, Papers, Feedback
from django.http import JsonResponse
# Create your views here.

def index(request):
    student_list = Student.objects.all()
    students_data = [
        {
            'StudentID': student.StudentID,
            'Department': student.Department,
            'Year': student.Year
        } for student in student_list
    ]
    return JsonResponse(students_data, safe=False)

def facultyGet(request):
    faculty_list = Faculty.objects.all()
    faculty_data = [
        {
            'FacultyID' : faculty.FacultyID,
            'Department' : faculty.Department
        } for faculty in faculty_list
    ]
    return JsonResponse(faculty_data, safe=False)

def projectsGet(request):
    project_list = Project.objects.all()
    project_data = [
        {
            'Name' : project.Name,
            'Description' : project.Description,
            'Deadline' : project.Deadline,
            'Faculty' : project.Faculty,
            'Students' : project.Students
        } for project in project_list
    ]
    return JsonResponse(project_data, safe=False)

def papersGet(request):
    papers_list = Papers.objects.all()
    papers_data = [
        {
            'Title' : papers.Title,
            'Description' : papers.Description,
            'SubmissionDate' : papers.SubmissionDate,
            'Authors' : papers.Authors,
            'Mentor' : papers.Mentor
        } for papers in papers_list
    ]
    return JsonResponse(papers_data, safe=False)

def feedbackGet(request):
    feedback_list = Feedback.objects.all()
    feedback_data = [
        {
            'Project' : feedback.Project,
            'Student' : feedback.Student,
            'Feedback' : feedback.Feedback,
            'Rating' : feedback.Rating
        } for feedback in feedback_list
    ]
    return JsonResponse(feedback_data, safe=False)


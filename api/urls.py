from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
# router.register('employees',views.EmployeeViewSet,basename='employee') #The Basename Has to be given only if we are using the viewsets.ViewSet otherwise for viewset.ModelViewSet we dont have to use it. 
router.register('employees',views.EmployeeViewSet) 
urlpatterns=[
    #function based view
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    #class based view
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()),
    
    #for using Viewsets
    path('',include(router.urls)),
    
    #for blogs
    path('blogs/',views.BlogsView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view()),
    
] 
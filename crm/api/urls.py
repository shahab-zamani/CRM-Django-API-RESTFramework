

from posixpath import basename
from django.urls import path,include
from .views import LeadViewset,UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register ('leads',LeadViewset,basename = 'leads')
router.register ('users',UserViewset,basename = 'users')

#Leads_List,leads_detail,LeadList,LeadDetails
urlpatterns = [

            path ('',include(router.urls)),

   #path('leads/', LeadList.as_view()),
   #path('leads/<int:id>/', LeadDetails.as_view()),

    #path('leads/', Leads_List),
   # path('leads/<int:pk>/', leads_detail),
]


from django.urls import path

from .views import MeetingDetailView, MeetingCreateView, UserList, UserDetail

urlpatterns = [
    path('', MeetingCreateView.as_view(), name='create_meeting'),
    # path('', MeetingAPIView.as_view(), name='welcome'),
    path('<int:pk>/', MeetingDetailView.as_view(), name='detail_meeting'),
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),

]
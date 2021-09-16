# from datetime import date, time
#
# import self as self
# from django.test import TestCase, Client
# from django.contrib.auth import get_user_model
# from django.urls import reverse
#
# from .models import Meeting, Room
#
# # Create your tests here.
# class MeetingTest(TestCase):
#
#     def setUp(self):
#         self.meeting = Meeting.objects.create(
#             title='Hello World',
#             date=date.today(),
#             start_time=time(9),
#             duration=1,
#             room=1
#         )
#
#     def test_string_representation(self):
#         meeting = Meeting(title='Hello World')
#         self.assertEqual(str(meeting), meeting.title)
#
#     def test_meeting_content(self):
#         self.assertEqual(f'{self.meeting.title}', 'Hello World')
#         self.assertEqual(f'{self.meeting.date}', '2021-09-16')
#         self.assertEqual(f'{self.meeting.start_time}', '09:00:00')
#         self.assertEqual(f'{self.meeting.duration}', '1')
#         self.assertEqual(f'{self.meeting.room}', '2')
#
#     def test_meeting_detail_view(self):
#         response = self.client.get('/meetings/1')
#         no_response = self.client.get('/meetings/10000')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'Hello World')
#         self.assertTemplateUsed(response, 'detail.html')

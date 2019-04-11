from django.urls import path
from . import views

urlpatterns = [
	path(
		'',
		views.UserListView.as_view(),
		name="user-list"),
	path(
		'create-user/',
		views.UserCreateView.as_view(),
		name="create-user"),
	path(
		'edit-user/<uuid:uuid>/',
		views.UserUpdateView.as_view(),
		name="update-user"),
	path(
		'delete-user/<uuid:uuid>/',
		views.UserDeleteView.as_view(),
		name="delete-user"),
	path(
		'user-details/<uuid:uuid>/',
		views.UserDetailView.as_view(),
		name="detail-user"),
]

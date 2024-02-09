from django.urls import path, include
#from chat import views as chat_views
from .views import chatPage
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path("chat/ ", chatPage, name="chat-page"),

	# login-section
	path("", LoginView.as_view(template_name="chats/LoginPage.html"), name="login-user"),
	path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]


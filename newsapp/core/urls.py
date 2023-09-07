from django.urls import path
from .views import Home, CreateNews, about, MyNews, MyNewsDetail, MyNewsUpdate, MyNewsDelete, Profile, search, single_post, Contact, Filter, category, CreateNewsComment, NewsDetails, update_profile, change_password
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', Home.as_view(), name = "home"),
    path('my-news/create-news', CreateNews.as_view(), name = "create_news"),
    path('about', about, name = "about"),
    path('my-news', MyNews.as_view(), name = "my_news"),
    path("my-news/details/<int:pk>", MyNewsDetail.as_view(), name="my_news_details"),
    path("my-news/update/<int:pk>", MyNewsUpdate.as_view(), name="my_news_update"),
    path("my-news/delete/<int:pk>", MyNewsDelete.as_view(), name="my_news_delete"),
    path('profile/', Profile.as_view(), name = "profile"),
    path('update-profile/', update_profile, name = "update_profile"),
    path('change-password/', change_password, name = "change_password"),
    path("search/", search, name="search"),
    path("single-post/", single_post, name="single_post"),
    path('contact/', Contact.as_view(), name = "contact"),
    path('filter/', Filter.as_view(), name = "filter"),
    path('category/', category, name = "category"),
    path('create-comment', CreateNewsComment.as_view(), name = "create_comment"),
    path("details/<int:pk>", NewsDetails.as_view(), name="news_details"),
    # path("parrword-reset", parrword_reset_request, name = "parrword_reset"),
    # path("eset/<uidb64>/<token>/", password_reset_confirm, name = "reset_confirm"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

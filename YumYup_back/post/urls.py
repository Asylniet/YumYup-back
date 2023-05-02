from django.urls import path
from .views import *

urlpatterns = [
    path("post_list/", post),
    path("saved_post/", saved_post),
    path("post_list/<int:post_id>/ratingComment_list/", rating_comment),
    path("post_list/<int:post_id>/calculateRating/", calculate_rating_by_post_id),
    path("saved_post/<int:saved_post_id>/", saved_post_detail),
    path("post_list/<int:post_id>/ratingComment_list/<int:rating_comment_id>/", rating_comment_detail),
    path("post_list/<int:post_id>/", post_detail)
]
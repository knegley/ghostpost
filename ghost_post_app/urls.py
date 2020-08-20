from django.urls import path
from ghost_post_app import views
urlpatterns = [path("", views.home_view, name="home"),
               path("add-post/", views.add_post_view, name="add_post"),
               path("boast-posts/", views.boast_view, name="boasts"),
               path("roast-posts", views.roast_view, name="roasts"),
               path("sorted/", views.sorted_view, name="sorted"),
               path("vote/<int:post_id>/<int:vote_value>",
                    views.up_vote_view, name="vote")
               ]

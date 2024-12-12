from django.urls import path
from .views import blog_list, blog_detail, blog_delete, blog_create, blog_update, vote_blog

urlpatterns = [
    path('', blog_list),
    path('create/', blog_create),  # Place "create/" before "<id>/"
    path('<id>/delete/', blog_delete),
    path('<id>/update/', blog_update),
    path('<id>/', blog_detail),  # Keep generic routes at the bottom
    path('<id>/vote/', vote_blog, name='vote_blog'),
]

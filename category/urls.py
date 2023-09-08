from django.urls import path


from django.conf import settings
from django.conf.urls.static import static

from category import views
from BookHub.feed import LatestEntriesFeed

urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.BookListView, name='books'),
    path('book/<int:pk>', views.BookDetailView, name='book-detail'),
    path('book/create/', views.BookCreate, name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate, name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete, name='book_delete'),

    path('student/<int:pk>/delete/', views.StudentDelete, name='student_delete'),
    path('student/create/', views.StudentCreate, name='student_create'),
    path('student<int:pk>/update/', views.StudentUpdate, name='student_update'),
    path('student/<int:pk>', views.StudentDetail, name='student_detail'),
    path('student/', views.StudentList, name='student_list'),
    path('student/book_list', views.student_BookListView, name='book_student'),
    path('book/<int:pk>/request_issue/', views.student_request_issue, name='request_issue'),

    path('feed/', LatestEntriesFeed(), name='feed'),
    path('return/<int:pk>', views.ret, name='ret'),


# url(r'^search_b/', views.search_book, name="search_b"),
# url(r'^search_s/', views.search_student, name="search_s")
]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),

# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

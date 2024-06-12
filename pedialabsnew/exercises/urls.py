from django.urls import re_path

from pedialabsnew.exercises.views import edit_lab, add_test_to_lab, \
    add_csv_to_lab, edit_test, delete_test, reorder_tests


urlpatterns = [
    re_path(r'^edit_lab/(?P<id>\d+)/$', edit_lab, {}, 'edit-lab'),
    re_path(r'^edit_lab/(?P<id>\d+)/add_test/$', add_test_to_lab, {},
            'add-test-to-lab'),
    re_path(r'^edit_lab/(?P<id>\d+)/add_csv/$', add_csv_to_lab, {},
            'add-csv-to-lab'),
    re_path(r'^edit_test/(?P<id>\d+)/$', edit_test, {}, 'edit-test'),
    re_path(r'^delete_test/(?P<id>\d+)/$', delete_test, {}, 'delete-test'),
    re_path(r'^reorder_tests/(?P<id>\d+)/$', reorder_tests, {},
            'reorder-tests'),
]

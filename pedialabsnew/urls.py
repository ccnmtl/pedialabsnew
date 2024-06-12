import django.views.static
import pedialabsnew.exercises.urls

from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.urls import path, re_path
from pedialabsnew.main.views import EditPageOverview, ViewPageOverview, \
    EditPage, ViewPage, ClearStateView, InstructorPage, InstructorLabReport, \
    ReportView, index
from django_cas_ng import views as cas_views

admin.autodiscover()

urlpatterns = [
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    path('cas/login', cas_views.LoginView.as_view(),
         name='cas_ng_login'),
    path('cas/logout', cas_views.LogoutView.as_view(),
         name='cas_ng_logout'),
    re_path(r'^registration/', include('registration.backends.default.urls')),
    re_path(r'^$', index),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^_clear/$', ClearStateView.as_view()),
    re_path(r'^_impersonate/', include('impersonate.urls')),
    re_path(r'^stats/$', TemplateView.as_view(template_name="stats.html")),
    re_path(r'smoketest/', include('smoketest.urls')),
    re_path(r'^uploads/(?P<path>.*)$', django.views.static.serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^pagetree/', include('pagetree.urls')),
    re_path(r'^quizblock/', include('quizblock.urls')),
    re_path(r'^exercises/', include(pedialabsnew.exercises.urls)),
    re_path(r'^instructor/$', InstructorPage.as_view()),
    re_path(r'^instructor/report/$', ReportView.as_view()),
    re_path(r'^instructor/(?P<uni>\w+)/lab/(?P<module_id>\d+)/$',
            InstructorLabReport.as_view()),

    # Overview. The order of these routes are important:
    re_path(r'^pages/public/edit/(?P<path>.*)$',
            EditPageOverview.as_view(), {}, 'edit-overview'),
    re_path(r'^pages/public/(?P<path>.*)$', ViewPageOverview.as_view()),
    # Labs. The order of these routes are important:
    re_path(r'^pages/labs/edit/(?P<path>.*)$', EditPage.as_view(), {},
            'edit-page'),
    re_path(r'^pages/labs/(?P<path>.*)$', ViewPage.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]

#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#                       INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

from django.conf.urls import url

from taskManager.views import *

app_name = "taskManager"

urlpatterns = [
    url(r'^$', index, name='index'),

    # File
    url(r'^download/(?P<file_id>\d+)/$',
        download, name='download'),
    url(r'^(?P<project_id>\d+)/upload/$',
        upload, name='upload'),
    url(r'^downloadprofilepic/(?P<user_id>\d+)/$',
        download_profile_pic, name='download_profile_pic'),

    # Authentication & Authorization
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^manage_groups/$', manage_groups,
        name='manage_groups'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^change_password/$', change_password,
        name='change_password'),
    url(r'^forgot_password/$', forgot_password,
        name='forgot_password'),
    url(r'^reset_password/$', reset_password,
        name='reset_password'),
    url(r'^profile/(?P<user_id>\d+)$',
        profile_by_id, name='profile_by_id'),
    url(r'^profile_view/(?P<user_id>\d+)$',
        profile_view, name='profile_view'),

    # Projects
    url(r'^project_create/$', project_create,
        name='project_create'),
    url(r'^(?P<project_id>\d+)/edit_project/$',
        project_edit, name='project_edit'),
    url(r'^manage_projects/$', manage_projects,
        name='manage_projects'),
    url(r'^(?P<project_id>\d+)/project_delete/$',
        project_delete, name='project_delete'),
    url(r'^(?P<project_id>\d+)/$',
        project_details, name='project_details'),
    url(r'^project_list/$', project_list,
        name='project_list'),

    # Tasks
    url(r'^(?P<project_id>\d+)/task_create/$',
        task_create, name='task_create'),
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/$',
        task_details, name='task_details'),
    url(r'^(?P<project_id>\d+)/task_edit/(?P<task_id>\d+)$',
        task_edit, name='task_edit'),
    url(r'^(?P<project_id>\d+)/task_delete/(?P<task_id>\d+)$',
        task_delete, name='task_delete'),
    url(r'^(?P<project_id>\d+)/task_complete/(?P<task_id>\d+)$',
        task_complete, name='task_complete'),
    url(r'^task_list/$', task_list, name='task_list'),
    url(r'^(?P<project_id>\d+)/manage_tasks/$',
        manage_tasks, name='manage_tasks'),


    # Notes
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/note_create/$',
        note_create, name='note_create'),
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/note_edit/(?P<note_id>\d+)$',
        note_edit, name='note_edit'),
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/note_delete/(?P<note_id>\d+)$',
        note_delete, name='note_delete'),

    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^search/$', search, name='search'),


    # Tutorials
    url(r'^tutorials/$', tutorials, name='tutorials'),
    url(r'^tutorials/(?P<vuln_id>[a-z\-]+)/$',
        show_tutorial, name='show_tutorial'),

    # Settings - DEBUG
    url(r'^settings/$', tm_settings, name='settings'),
]

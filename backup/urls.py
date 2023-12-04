from django.urls import path
from backup.views import restore_backup, list_backups, backup_database

urlpatterns = [
    path('list_backups/', list_backups, name='list_backups'),
    path('backup_database/', backup_database, name='backup_database'),
    path('restore/<str:filename>/', restore_backup, name='restore_backup'),


]
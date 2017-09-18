# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 23:06
from __future__ import unicode_literals

import NearBeach.private_media
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0009_remove_documents_document_uploaded_audit'),
    ]

    operations = [
        migrations.CreateModel(
            name='documents_folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents_folder_change_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'documents_folder',
            },
        ),
        migrations.CreateModel(
            name='folders',
            fields=[
                ('folder_id', models.AutoField(primary_key=True, serialize=False)),
                ('folder_description', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders_change_user', to=settings.AUTH_USER_MODEL)),
                ('parent_folder_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.folders')),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.project')),
                ('task_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.tasks')),
            ],
            options={
                'db_table': 'folder',
            },
        ),
        migrations.RemoveField(
            model_name='document_folders',
            name='change_user',
        ),
        migrations.RemoveField(
            model_name='document_folders',
            name='parent_folder_id',
        ),
        migrations.RemoveField(
            model_name='document_folders',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='document_folders',
            name='task_id',
        ),
        migrations.AlterField(
            model_name='documents',
            name='document',
            field=models.FileField(blank=True, null=True, storage=NearBeach.private_media.File_Storage(), upload_to=b''),
        ),
        migrations.DeleteModel(
            name='document_folders',
        ),
        migrations.AddField(
            model_name='documents_folder',
            name='document_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.documents'),
        ),
        migrations.AddField(
            model_name='documents_folder',
            name='folder_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.folders'),
        ),
    ]
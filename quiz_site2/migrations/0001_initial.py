# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('page_header', models.TextField(blank=True, null=True)),
                ('page_seq', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question_seq', models.IntegerField(default=100)),
                ('question_text', models.CharField(max_length=255)),
                ('question_type', models.CharField(max_length=255, default='SingleQuestion', choices=[('SingleQuestion', 'Single Question'), ('MultiChoiceQuestion', 'Multi-Choice Question'), ('TextQuestion', 'Text Question')])),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('response_text', models.CharField(max_length=255)),
                ('response_value', models.IntegerField()),
                ('response_seq', models.IntegerField(default=100)),
                ('question', models.ForeignKey(to='quiz_site2.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('section_text', models.CharField(max_length=255)),
                ('section_seq', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sub_page_header', models.TextField(blank=True, null=True)),
                ('sub_page_seq', models.IntegerField(default=100)),
                ('page', models.ForeignKey(to='quiz_site2.Page')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='sub_page',
            field=models.ForeignKey(to='quiz_site2.SubPage'),
        ),
        migrations.AddField(
            model_name='page',
            name='section',
            field=models.ForeignKey(to='quiz_site2.Section'),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('priority', models.PositiveIntegerField(choices=[(0, 'Unsent'), (10, 'Chat'), (20, 'Email'), (30, 'Text'), (40, 'Call')], help_text='Highest service to try')),
                ('status', models.PositiveIntegerField(choices=[(0, 'Unsent'), (10, 'Chat'), (20, 'Email'), (30, 'Text'), (40, 'Call')], default=0, help_text='Highest service tried')),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('responded', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

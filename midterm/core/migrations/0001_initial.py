# Generated by Django 3.0 on 2020-03-02 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField(default='', max_length=800)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('num_pages', models.IntegerField()),
                ('genre', models.IntegerField(choices=[(1, 'Fantasy'), (2, 'Classic'), (3, 'Poems')])),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField(default='', max_length=800)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('types', models.IntegerField(choices=[(1, 'Bullet'), (2, 'Food'), (3, 'Travel'), (4, 'Sport')])),
                ('publisher', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

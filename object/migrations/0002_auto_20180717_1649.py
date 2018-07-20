# Generated by Django 2.0.5 on 2018-07-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='kind',
        ),
        migrations.AddField(
            model_name='post',
            name='has_another_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='has_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='has_title',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='postchat',
            name='before',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat'),
        ),
        migrations.AlterField(
            model_name='postchatlikecount',
            name='post_chat',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat'),
        ),
        migrations.AlterField(
            model_name='postchatrestmessagelikecount',
            name='post_chat_rest_message',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChatRestMessageLike'),
        ),
        migrations.AlterField(
            model_name='postcommentlikecount',
            name='post_comment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostComment'),
        ),
        migrations.AlterField(
            model_name='postlikecount',
            name='post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post'),
        ),
        migrations.AddField(
            model_name='posttitle',
            name='post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post'),
        ),
        migrations.AddField(
            model_name='postdescription',
            name='post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post'),
        ),
    ]
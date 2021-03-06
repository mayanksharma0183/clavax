# Generated by Django 3.2.4 on 2021-06-11 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.basemodel')),
                ('token', models.CharField(max_length=200)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token_student', to='students.studentdetails')),
            ],
            bases=('students.basemodel',),
        ),
    ]

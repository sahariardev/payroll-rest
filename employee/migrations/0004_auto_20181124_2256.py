# Generated by Django 2.1.3 on 2018-11-24 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='n_id',
            field=models.CharField(default=11111, max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Package'),
        ),
        migrations.AddField(
            model_name='employee',
            name='pay_day',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number_secondary',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Type'),
        ),
    ]

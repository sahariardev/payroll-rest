# Generated by Django 2.1.3 on 2018-12-12 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComputationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_from', models.DateField()),
                ('effective_till_date', models.DateField()),
                ('rule', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_of_joining', models.DateField(auto_now=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=40)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(max_length=30)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=40)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('spouse_name', models.CharField(blank=True, max_length=30)),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Designation')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('salary', models.FloatField(null=True)),
                ('annual_leave', models.IntegerField()),
                ('sick_leave', models.IntegerField()),
                ('extra', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PayHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('description', models.TextField()),
                ('add_net_salary', models.BooleanField()),
                ('calculation_type', models.CharField(choices=[('Flat Rate', 'Flat Rate'), ('On Attendence', 'On Attendence'), ('On Production', 'On Production'), ('As Computed Value', 'As Computed Value'), ('As Custom Value', 'As Custom Value')], max_length=40)),
                ('add_or_deduct', models.CharField(choices=[('add', 'add'), ('deduct', 'deduct')], default='add', max_length=10)),
                ('under', models.CharField(choices=[('Direct Expense', 'Direct Expense'), ('Indirect Expense', 'Indirect Expense')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PayHeadType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductionAttendanceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Production', 'Production'), ('attendance/leave with pay', 'attendance/leave with pay'), ('attendance/leave without pay', 'attendance/leave without pay')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_from', models.DateField()),
                ('effective_till_date', models.DateField()),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryDetailItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=0)),
                ('value', models.FloatField()),
                ('rate', models.FloatField()),
                ('pay_head', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.PayHead')),
                ('salary_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.SalaryDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('symbol', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UnitRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_from', models.DateField()),
                ('effective_till_date' ,models.DateField()),
                ('first_unit',models.IntegerField()),
                ('value',models.FloatField()),
                ('second_unit',models.IntegerField())
            ],
        ),
        migrations.AddField(
            model_name='salarydetailitem',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Unit'),
        ),
        migrations.AddField(
            model_name='payhead',
            name='attendence_production_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.ProductionAttendanceType'),
        ),
        migrations.AddField(
            model_name='payhead',
            name='calculation_period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Unit'),
        ),
        migrations.AddField(
            model_name='payhead',
            name='pay_head_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.PayHeadType'),
        ),
        migrations.AddField(
            model_name='employee',
            name='peckage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Package'),
        ),
        migrations.AddField(
            model_name='computationinfo',
            name='pay_head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.PayHead'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='production_attendance_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.ProductionAttendanceType'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Unit'),
        ),
        migrations.AddField(
            model_name='salarydetail',
            name='name',
            field=models.CharField(max_length=30,null=True)
,
        ),
        migrations.AddField(
            model_name='payhead',
            name='rate',
            field=models.FloatField(null=True)
            ,
        ),
        migrations.AddField(
            model_name='payhead',
            name='rule',
            field=models.CharField(max_length=100, null=True)
            ,
        ),
    ]

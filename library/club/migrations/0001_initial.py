# Generated by Django 3.1 on 2020-08-11 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookID', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memberID', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gen', models.SmallIntegerField(verbose_name='generation')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ')], max_length=1)),
                ('year', models.SmallIntegerField(verbose_name='Niên khóa')),
                ('fb', models.TextField(verbose_name='tài khoản facebook')),
                ('section', models.CharField(choices=[('T', 'Truyền thông'), ('S', 'Sự kiện'), ('P', 'Phục vụ bạn đọc')], max_length=30)),
                ('role', models.CharField(choices=[('mem', 'Thành viên'), ('viceMod', 'Phó ban'), ('mod', 'Trưởng ban'), ('treasurer', 'Thủ quỹ'), ('viceSupermod', 'Phó Chủ nhiệm'), ('supermod', 'Chủ nhiệm')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('faculty', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ')], max_length=1)),
                ('status', models.CharField(choices=[('debt', 'Nợ'), ('free', 'Không nợ')], max_length=4)),
                ('note', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.UUIDField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(choices=[('BCN', 'BCN'), ('mem', 'trực viên')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='BookLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowingDate', models.DateField()),
                ('returningDate', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('free', 'Đã trả'), ('debt', 'Chưa trả')], max_length=4)),
                ('supervisor', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='club.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='club.student')),
            ],
            options={
                'ordering': ['borrowingDate'],
            },
        ),
    ]
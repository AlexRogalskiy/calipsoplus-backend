# Generated by Django 2.0.2 on 2018-07-06 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuacamoleConnection',
            fields=[
                ('connection_id', models.AutoField(primary_key=True, serialize=False)),
                ('connection_name', models.CharField(max_length=128)),
                ('protocol', models.CharField(max_length=32)),
                ('proxy_port', models.IntegerField(blank=True, null=True)),
                ('proxy_hostname', models.CharField(blank=True, max_length=512, null=True)),
                ('proxy_encryption_method', models.CharField(blank=True, max_length=4, null=True)),
                ('max_connections', models.IntegerField(blank=True, null=True)),
                ('max_connections_per_user', models.IntegerField(blank=True, null=True)),
                ('connection_weight', models.IntegerField(blank=True, null=True)),
                ('failover_only', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'guacamole_connection',
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionGroup',
            fields=[
                ('connection_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('connection_group_name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=14)),
                ('max_connections', models.IntegerField(blank=True, null=True)),
                ('max_connections_per_user', models.IntegerField(blank=True, null=True)),
                ('enable_session_affinity', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'guacamole_connection_group',
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=128)),
                ('parameter_value', models.CharField(max_length=4096)),
            ],
            options={
                'managed': False,
                'db_table': 'guacamole_connection_parameter',
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=10)),
            ],
            options={
                'managed': False,
                'db_table': 'guacamole_connection_permission',
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, unique=True)),
                ('password_hash', models.BinaryField()),
                ('password_salt', models.BinaryField(blank=True, null=True)),
                ('password_date', models.DateTimeField()),
                ('disabled', models.IntegerField()),
                ('expired', models.IntegerField()),
                ('access_window_start', models.TimeField(blank=True, null=True)),
                ('access_window_end', models.TimeField(blank=True, null=True)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('timezone', models.CharField(blank=True, max_length=64, null=True)),
                ('full_name', models.CharField(blank=True, max_length=256, null=True)),
                ('email_address', models.CharField(blank=True, max_length=256, null=True)),
                ('organization', models.CharField(blank=True, max_length=256, null=True)),
                ('organizational_role', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'guacamole_user',
            },
        ),
        migrations.CreateModel(
            name='CalipsoAvailableImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_name', models.CharField(max_length=255, unique=True)),
                ('docker_daemon', models.CharField(default='', max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('cpu', models.IntegerField()),
                ('memory', models.CharField(max_length=100)),
                ('hdd', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'calipso_images',
            },
        ),
        migrations.CreateModel(
            name='CalipsoContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calipso_user', models.CharField(max_length=255)),
                ('calipso_experiment', models.CharField(max_length=255)),
                ('container_id', models.CharField(max_length=255)),
                ('container_name', models.CharField(max_length=255)),
                ('container_status', models.CharField(max_length=25)),
                ('container_info', models.TextField()),
                ('container_logs', models.TextField()),
                ('guacamole_username', models.CharField(blank=True, max_length=255)),
                ('guacamole_password', models.CharField(blank=True, max_length=255)),
                ('vnc_password', models.CharField(blank=True, max_length=255)),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('host_port', models.CharField(blank=True, max_length=255)),
                ('public_name', models.CharField(default='default', max_length=255)),
            ],
            options={
                'db_table': 'calipso_containers',
            },
        ),
        migrations.CreateModel(
            name='CalipsoExperiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('serial_number', models.CharField(blank=True, max_length=50)),
                ('beam_line', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'calipso_experiments',
            },
        ),
        migrations.CreateModel(
            name='CalipsoFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=2083)),
            ],
            options={
                'db_table': 'calipso_facilities',
            },
        ),
        migrations.CreateModel(
            name='CalipsoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calipso_uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('experiments', models.ManyToManyField(to='apprest.CalipsoExperiment')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'calipso_users',
            },
        ),
        migrations.CreateModel(
            name='CalipsoUserQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_simultaneous', models.IntegerField(default=3)),
                ('cpu', models.IntegerField(default=4)),
                ('memory', models.CharField(default='8G', max_length=100)),
                ('hdd', models.CharField(default='20G', max_length=100)),
                ('calipso_user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apprest.CalipsoUser')),
            ],
            options={
                'db_table': 'calipso_quotas',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCalipsoAvailableImages',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('public_name', models.CharField(db_index=True, max_length=255)),
                ('docker_daemon', models.CharField(default='', max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('cpu', models.IntegerField()),
                ('memory', models.CharField(max_length=100)),
                ('hdd', models.CharField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical calipso available images',
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCalipsoContainer',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('calipso_user', models.CharField(max_length=255)),
                ('calipso_experiment', models.CharField(max_length=255)),
                ('container_id', models.CharField(max_length=255)),
                ('container_name', models.CharField(max_length=255)),
                ('container_status', models.CharField(max_length=25)),
                ('container_info', models.TextField()),
                ('container_logs', models.TextField()),
                ('guacamole_username', models.CharField(blank=True, max_length=255)),
                ('guacamole_password', models.CharField(blank=True, max_length=255)),
                ('vnc_password', models.CharField(blank=True, max_length=255)),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('host_port', models.CharField(blank=True, max_length=255)),
                ('public_name', models.CharField(default='default', max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical calipso container',
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCalipsoExperiment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('serial_number', models.CharField(blank=True, max_length=50)),
                ('beam_line', models.CharField(blank=True, max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical calipso experiment',
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCalipsoFacility',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=2083)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical calipso facility',
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCalipsoUser',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('calipso_uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical calipso user',
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCalipsoUserQuota',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('max_simultaneous', models.IntegerField(default=3)),
                ('cpu', models.IntegerField(default=4)),
                ('memory', models.CharField(default='8G', max_length=100)),
                ('hdd', models.CharField(default='20G', max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('calipso_user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='apprest.CalipsoUser')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical calipso user quota',
                'get_latest_by': 'history_date',
            },
        ),
    ]

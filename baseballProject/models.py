# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cranks(models.Model):
    day1 = models.DateField()
    ranks1 = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    win = models.CharField(max_length=100)
    lose = models.CharField(max_length=100)
    draw = models.CharField(max_length=100)
    winrate = models.CharField(max_length=100)
    diff = models.CharField(max_length=100)
    remine_games = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    runs_allowed = models.CharField(max_length=100)
    homerun = models.CharField(max_length=100)
    steal = models.CharField(max_length=100)
    hit = models.CharField(max_length=100)
    pitch = models.CharField(max_length=100)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = '_cranks'
        unique_together = (('day1', 'ranks1'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MPlayer(models.Model):
    player_id = models.CharField(unique=True, max_length=100)
    teams = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'm_player'


class MTeams(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    name_short = models.CharField(max_length=100)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'm_teams'


class Stats(models.Model):
    player_id = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    at_bat1 = models.CharField(max_length=100)
    at_bat2 = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    hit = models.CharField(max_length=100)
    double = models.CharField(max_length=100)
    triple = models.CharField(max_length=100)
    homerun = models.CharField(max_length=100)
    basehit = models.CharField(max_length=100)
    rbi = models.CharField(max_length=100)
    steal = models.CharField(max_length=100)
    steal_dead = models.CharField(max_length=100)
    sacrifice = models.CharField(max_length=100)
    sacrifice_fly = models.CharField(max_length=100)
    walks = models.CharField(max_length=100)
    hit_by_pitch = models.CharField(max_length=100)
    strikeout = models.CharField(max_length=100)
    double_out = models.CharField(max_length=100)
    hit_rate = models.CharField(max_length=100)
    on_base = models.CharField(max_length=100)
    slugging = models.CharField(max_length=100, blank=True, null=True)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField(blank=True, null=True)
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'stats'


class TChit(models.Model):
    day1 = models.DateField()
    rank1 = models.CharField(max_length=100)
    player_id = models.CharField(max_length=100)
    hit_rate = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    at_bat1 = models.CharField(max_length=100)
    at_bat2 = models.CharField(max_length=100)
    single_hit = models.CharField(max_length=100)
    double_hit = models.CharField(max_length=100)
    triple_hit = models.CharField(max_length=100)
    homerun = models.CharField(max_length=100)
    basehit = models.CharField(max_length=100)
    rbi = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    strikeout = models.CharField(max_length=100)
    walks = models.CharField(max_length=100)
    hit_by_pitch = models.CharField(max_length=100)
    sacrifice = models.CharField(max_length=100)
    sacrifice_fly = models.CharField(max_length=100)
    steal = models.CharField(max_length=100)
    steal_dead = models.CharField(max_length=100)
    double_out = models.CharField(max_length=100)
    on_base = models.CharField(max_length=100)
    slugging = models.CharField(max_length=100)
    ops = models.CharField(max_length=100)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_chit'


class TCranks(models.Model):
    day1 = models.DateField()
    ranks1 = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    win = models.CharField(max_length=100)
    lose = models.CharField(max_length=100)
    draw = models.CharField(max_length=100)
    winrate = models.CharField(max_length=100)
    diff = models.CharField(max_length=100)
    remine_games = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    runs_allowed = models.CharField(max_length=100)
    homerun = models.CharField(max_length=100)
    steal = models.CharField(max_length=100)
    hit = models.CharField(max_length=100)
    pitch = models.CharField(max_length=100)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_cranks'
        unique_together = (('day1', 'ranks1'),)


class TPranks(models.Model):
    day1 = models.DateField()
    ranks1 = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    win = models.CharField(max_length=100)
    lose = models.CharField(max_length=100)
    draw = models.CharField(max_length=100)
    winrate = models.CharField(max_length=100)
    diff = models.CharField(max_length=100)
    remine_games = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    runs_allowed = models.CharField(max_length=100)
    homerun = models.CharField(max_length=100)
    steal = models.CharField(max_length=100)
    hit = models.CharField(max_length=100)
    pitch = models.CharField(max_length=100)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_pranks'
        unique_together = (('day1', 'ranks1'),)

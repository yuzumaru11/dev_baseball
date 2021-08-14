from django.db import models

# マスタ系
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


# トラン系
class TCRanks(models.Model):
    day = models.DateField()
    rank = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    win = models.CharField(max_length=100)
    lose = models.CharField(max_length=100)
    draw = models.CharField(max_length=100)
    winrate = models.CharField(max_length=100)
    hit = models.CharField(max_length=100)
    pitch = models.CharField(max_length=100)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_cranks'
        unique_together = (('day', 'rank'),)


class TPRanks(models.Model):
    day = models.DateField()
    rank = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    win = models.CharField(max_length=100)
    lose = models.CharField(max_length=100)
    draw = models.CharField(max_length=100)
    winrate = models.CharField(max_length=100)
    hit = models.CharField(max_length=100)
    pitch = models.CharField(max_length=100)
    udate = models.DateTimeField()
    uuser = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    ruser = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_pranks'
        unique_together = (('day', 'rank'),)


class TChit(models.Model):
    day = models.DateField()
    rank = models.CharField(max_length=100)
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

class VCrankDay(models.Model):
    day = models.DateField()
    rank = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    win = models.CharField(max_length=100)
    lose = models.CharField(max_length=100)
    draw = models.CharField(max_length=100)
    winrate = models.CharField(max_length=100)
    hit = models.CharField(max_length=100)
    pitch = models.CharField(max_length=100)
    tname = models.CharField(max_length=100)
    tsname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'v_crank_day'

# Create your models here.

import datetime
from django.db import connection


def dictfetchall(cursor):
    # "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_vCrankDay():
    with connection.cursor() as cursor:
        sql = 'select * from v_crank_day where day1 = %s'
        today1 = datetime.date.today()
        cursor.execute(sql, (today1,))
        vCrankDay_data = dictfetchall(cursor)
        return vCrankDay_data


def get_vPrankDay():
    with connection.cursor() as cursor:
        sql = 'select * from v_prank_day where day1 = %s'
        today1 = datetime.date.today()
        cursor.execute(sql, (today1,))
        vPrankDay_data = dictfetchall(cursor)
        return vPrankDay_data


def get_vcStats():
    today1 = datetime.date.today()
    year1 = datetime.date.today().year
    # 規定打率以上の選手を取得
    sql = "select * from v_stats vs  inner join " \
          " (select teams , games*3.1 at_bat1_game from m_games mg where year1 = %s) mg on vs.teams = mg.teams " \
          " where vs.year1 = %s and vs.at_bat1 > at_bat1_game and vs.league = %s order by vs.hit_rate desc;"
    with connection.cursor() as cursor:
        cursor.execute(sql, (year1, year1,"central", ))
        vcStats = dictfetchall(cursor)

        for stat in vcStats:
            ops = int(stat['on_base'].replace('.', '')) + int(stat['slugging'].replace('.', ''))

            if ops > 1000:
              ops_tmp = '{:4,d}'.format(ops).replace(',', '.')
              ops = ops_tmp
            else:
                ops = "." + str(ops)

            stat['ops'] = ops
        return vcStats

def get_vpStats():
    today1 = datetime.date.today()
    year1 = datetime.date.today().year
    # 規定打率以上の選手を取得
    sql = "select * from v_stats vs  inner join " \
          " (select teams , games*3.1 at_bat1_game from m_games mg where year1 = %s) mg on vs.teams = mg.teams " \
          " where vs.year1 = %s and vs.at_bat1 > at_bat1_game and vs.league = %s order by vs.hit_rate desc;"
    with connection.cursor() as cursor:
        cursor.execute(sql, (year1, year1,"pacific", ))
        vcStats = dictfetchall(cursor)

        for stat in vcStats:
            ops = int(stat['on_base'].replace('.', '')) + int(stat['slugging'].replace('.', ''))

            if ops > 1000:
              ops_tmp = '{:4,d}'.format(ops).replace(',', '.')
              ops = ops_tmp
            else:
                ops = "." + str(ops)

            stat['ops'] = ops
        return vcStats


def get_vcPicthes():
    today1 = datetime.date.today()
    year1 = datetime.date.today().year
    # 規定投球以上の選手を取得
    sql = "select * from v_pstats vp inner join " \
          " (select teams , games all_games  from m_games mg where year1 = %s) mg on vp.teams = mg.teams " \
          " where vp.year1 = %s and cast(vp.pitch_innings as signed) > cast(mg.all_games as signed) and vp.league = %s order by vp.era asc;"
    with connection.cursor() as cursor:
        cursor.execute(sql, (year1, year1,"central", ))
        vpcStats = dictfetchall(cursor)

        return vpcStats


def get_vpPicthes():
    today1 = datetime.date.today()
    year1 = datetime.date.today().year
    # 規定投球以上の選手を取得
    sql = "select * from v_pstats vp inner join " \
          " (select teams , games all_games  from m_games mg where year1 = %s) mg on vp.teams = mg.teams " \
          " where vp.year1 = %s and cast(vp.pitch_innings as signed) > cast(mg.all_games as signed) and vp.league = %s order by vp.era asc;"
    with connection.cursor() as cursor:
        cursor.execute(sql, (year1, year1,"pacific", ))
        vppStats = dictfetchall(cursor)

        return vppStats


def get_team_bstats(team):
    year1 = datetime.date.today().year

    # 最新年の打撃成績(1打席以上)
    sql = "select * from v_stats vs where teams =%s and year1 =%s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (team, year1, ))
        team_bstats = dictfetchall(cursor)

        return team_bstats


def get_team_pstats(team):
    year1 = datetime.date.today().year

    # 最新年の投手成績(1打席以上)
    sql = "select * from v_pstats vp where teams =%s and year1 =%s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (team, year1,))
        team_pstats = dictfetchall(cursor)

        return team_pstats
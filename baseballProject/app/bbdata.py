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
        cursor.execute('select * from v_crank_day')
        vCrankDay_data = dictfetchall(cursor)
        return vCrankDay_data


def get_vPrankDay():
    with connection.cursor() as cursor:
        cursor.execute('select * from v_prank_day')
        vPrankDay_data = dictfetchall(cursor)
        return vPrankDay_data


def get_vPrankDay():
    with connection.cursor() as cursor:
        cursor.execute('select * from v_prank_day')
        vPrankDay_data = dictfetchall(cursor)
        return vPrankDay_data


def get_vStats():
    today1 = datetime.date.today()
    year1 = datetime.date.today().year
    sql = "select * from v_stats vs  inner join " \
          " (select teams , games*3.1 at_bat1_game from m_games mg where year1 = %s) mg on vs.teams = mg.teams " \
          " where vs.year1 = %s and vs.at_bat1 > at_bat1_game order by vs.hit_rate desc;"
    with connection.cursor() as cursor:
        cursor.execute(sql, (year1, year1, ))
        vStats = dictfetchall(cursor)

        for stat in vStats:
            ops = int(stat['on_base'].replace('.', '')) + int(stat['slugging'].replace('.', ''))

            if ops > 1000:
              ops_tmp = '{:4,d}'.format(ops).replace(',', '.')
              ops = ops_tmp
            else:
                ops = "." + str(ops)

            stat['ops'] = ops
        return vStats
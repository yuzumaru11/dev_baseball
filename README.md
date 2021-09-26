# dev_baseball
プロ野球選手のデータをスクレイピングしオリジナルのデータベースを作成する  
NPB公式サイトでは、計算されていない情報(.OPS等)を計算し一層野球を楽しめるような情報を  
見れるようにする  

### baseballProject
Djangoを利用したWebサービスを構築中  
  
  
### プログラム説明
> all_player_insert.py
> 
　⇒指定した期間の選手をDBへ登録する(ex.2000年～2021年の選手など)  
 
> ranks_insert.py
> 
　⇒本日の順位で更新

> update_m_games.py
>   
　⇒本日の試合数で「m_games]を更新

> active_bstats_update.py
>  
　⇒現役選手の打撃成績を更新

> active_pstats_update.py
>  
　⇒現役選手の投手成績を更新


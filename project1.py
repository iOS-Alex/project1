import statsapi

sched = statsapi.schedule(start_date='04/08/2025',end_date='04/09/2025',team=143,opponent=121)
team = statsapi.get('team', {'teamId':143})



print('The A\'s won %s games in 2024.' % sum(1 for x in statsapi.schedule(team=133,start_date='01/01/2025',end_date='12/31/2025') if x.get('winning_team','')=='Oakland Athletics'))
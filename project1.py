import statsapi

# get schedules for teams
sched = statsapi.schedule(start_date='04/11/2025',end_date='04/11/2025',team="",opponent="")

# get teams, how do i get a list of all teams and their ID's?
team = statsapi.get('team', {'teamId':112})
print(sched)

# where do I store my data once I pull it?

# why can't I see data for 2025?
#print('The A\'s won %s games in 2018.' % sum(1 for x in statsapi.schedule(team=133,start_date='01/01/2018',end_date='12/31/2018') if x.get('winning_team','')=='Oakland Athletics'))

# Dodgers ID 119
# Cubs ID 112
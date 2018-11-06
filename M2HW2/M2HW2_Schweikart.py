# Brain Schweikart
# M2HW2 - World Series Winners
# 11/01/18
# Read text file then allow the user to select a team
# After selecting a team dispaly the total wins

winner_list = []

try:
	f=open('WorldSeriesWinners.txt', 'r')
	
	for names in f.readlines():
		names = names.strip('\n')
		winner_list.append(names)
		f.close()
except:
		print('WorldSeriesWinners.txt file is not present.')
		exit(1)
	
def counts():
	num_of_wins = 0
	team_name = str(input('Enter the Teams\'s name:'))
	
	for name in winner_list:
		if(team_name == name):
			num_of_wins += 1
	print('The team ' + team_name +' has won ' + str(num_of_wins) + ' times in the period 1903 - 20009')
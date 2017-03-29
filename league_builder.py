import csv
import random

'''
LeagueBuilder, by Adam Cameron, March 2017

Take 18 youth soccer players and divide them into three more or less equal teams.

Comments explain immediately following line(s) of code.

'''


# Ensure script doesn't run upon importation.

if __name__ == "__main__":

	# Declare three empty lists corresponding to team titles.

	sharks = []
	dragons = []
	raptors = []

	# Declare two empty lists corresponding to experience/inexperience.

	experienced = []
	inexperienced = []

	# Open CSV file and instantiate csv.reader object.

	with open('soccer_players.csv') as csv_file:
		player_reader = csv.reader(csv_file, delimiter=',')
		
		# Skip headers
		next(player_reader, None)

		# Append experienced and inexperienced lists with data from CSV file.
		for line in player_reader:
			if line[2] == 'YES':
				experienced.append(line)
			else:
				inexperienced.append(line)

		# Allocate experienced team members to three empty team lists.
		# Length of 'experienced' list is divided by three, after which
		# the team list variables are reset to include list slices based on list length.

		members_per_team = len(experienced) // 3
		sharks = experienced[0: members_per_team] # E.g.: slice of 'experienced' from beginning to the length of the list divided by 3.
		raptors = experienced[members_per_team: 2 * members_per_team]
		dragons = experienced[2 * members_per_team:len(experienced)]

		# Allocate inexperienced team members to lists by declaring new lists and concatenating them with lists
		# already containing experienced players.

		final_drags = dragons + inexperienced[0:members_per_team]
		final_sharks = sharks + inexperienced[members_per_team:2 * members_per_team]
		final_rapts = raptors + inexperienced[2 * members_per_team:len(inexperienced)]

	# Function to join list items into strings
	# and concatenate them to an empty string.

	def joining(the_list):
		empty = ''
		for i in the_list:
			empty = (empty + ', '.join(i)) + '\n'
		return empty

	# Function opening and writing everything to output file.

	def make_file():
		with open('teams.txt', 'w') as f:
			f.write("Soccer Teams 2017 \n \n")
			f.write("Raptors: \n")
			f.write(joining(final_rapts))
			f.write('\n')
			f.write("Dragons: \n")
			f.write(joining(final_drags))
			f.write('\n')
			f.write("Sharks: \n")
			f.write(joining(final_sharks))

	# Text of form letter for formatting.

	a = """
	Dear {}, 

	I would like to warmly welcome you and your child to the beginning
	of our 2017 soccer season! We trust it will be an even bigger blast
	than the previous years. {} will be playing with the {} this year, and the first practice
	will be on Thursday, March 30th at 4:00 PM. 

	"""

	# Functions handling formatting and output of each team's form letter.


	def drag_letter_write(team_list):
		for i in team_list:
			b = a.format(i[3], i[0], 'Dragons')
			c = i[0].lower().replace(' ', '_')
			with open('%s.txt' % c, 'a') as letter_file:
				letter_file.write(b)

	def rapt_letter_write(team_list):
		for i in team_list:
			b = a.format(i[3], i[0], 'Raptors')
			c = i[0].lower().replace(' ', '_')
			with open('%s.txt' % c, 'a') as letter_file:
				letter_file.write(b)

	def shark_letter_write(team_list):
		for i in team_list:
			b = a.format(i[3], i[0], 'Sharks')
			c = i[0].lower().replace(' ', '_')
			with open('%s.txt' % c, 'a') as letter_file:
				letter_file.write(b)


make_file()
drag_letter_write(final_drags)
rapt_letter_write(final_rapts)
shark_letter_write(final_sharks)







# Reward the final step for walking forward
# Punish the final step for walking backwards
goodbad =   ((0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (1, 0, 0, 0,),
			 (-1, 0, 0, 0,),

			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, -1, 0,),


			 (0, 0, 1, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 1, 0, -1,),

			 (0, 0, -1, 0,),
			 (-1, 0, 0, 0,),
			 (0, -1, 0, 1,),
			 (0, 0, 0, 0,))

#prevent from moving leg on ground
#col 0 cant go to col 3 and viceversa. same is true for row 0 and 3.
norollerblade =   ((0, -1, 0, -1,),
			 (0, 0, 0, -1,),
			 (0, 0, 0, -1,),
			 (0, -1, 0, -1,),
			 (0, -1, 0, 0,), #4
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, -1, 0, 0,), #7
			 (0, -1, 0, 0,), #8
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,), #11
			 (0, -1, 0, -1,), #12
			 (0, 0, 0, -1,),
			 (0, 0, 0, 0,),
			 (0, -1, 0, -1,)) #15

# Prevent from going i to a falling state. (0,5,6,9,10,15)
imfalling = ((0, 0, 0, 0,), 
			 (-1, 0, -1, 0,),
			 (0, 0, -1, 0,),
			 (0, -1, 0, -1,),

			 (-1, 0, -1, 0,),
			 (0, -1, 0, 0,),
			 (0, -1, 0, -1,),
			 (-1, 0, 0, 0,),


			 (-1, 0, 0, 0,),
			 (0, -1, 0, -1,),
			 (0, -1, 0, 0,),
			 (-1, 0, -1, 0,),

			 (0, -1, 0, -1,),
			 (0, 0, -1, 0,),
			 (-1, 0, -1, 0,),
			 (0, 0, 0, 0,))


trans = ((1, 3, 4, 12),
		 (0, 2, 5, 13),
		 (3, 1, 6, 14),
		 (2, 0, 7, 15),
		 (5, 7, 0, 8),
		 (4, 6, 1, 9),
		 (7, 5, 2, 10),
		 (6, 4, 3, 11),
		 (9, 11, 12, 4),
		 (8, 10, 13, 5),
		 (11, 9, 14, 6),
		 (10, 8, 15, 7),
		 (13, 15, 8, 0),
		 (12, 14, 9, 1),
		 (15, 13, 10, 2),
		 (14, 12, 11, 3))

class Environment:
	def __init__(self, state=0):
		self.state= state
		self.trans = trans
		self.rew = [[imfalling[row][i]+goodbad[row][i]+norollerblade[row][i] for i in range(len(imfalling[row]))] for row in range(len(imfalling))]

	def go(self, a):
		r = self.rew[self.state][a]
		self.state = self.trans[self.state][a]
		return self.state, r

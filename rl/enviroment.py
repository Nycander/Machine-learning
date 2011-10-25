class Environment
	def __init__(self, state=0):
		self.state= state
		self.trans = #TODO
		self.rew = #TODO

	def go(self, a):
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


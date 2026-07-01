# Farms grass, carrots and wood, 4x4

while True:
	for i in range(get_world_size()):
		for w in range(get_world_size()):
			if can_harvest():
				harvest()
			if (i == 1):
				if can_harvest():
					harvest()
				
				if get_ground_type() == Grounds.Grassland:
					till()
				
				if get_ground_type() == Grounds.Soil:
					plant(Entities.Carrot)
				
			elif (i == 2):
				if can_harvest():
					harvest()
					
				if (w % 2 == 0):
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
					
			elif (i == 3):
				if (w % 2 != 0):
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
				
			move(East)
		move(North)

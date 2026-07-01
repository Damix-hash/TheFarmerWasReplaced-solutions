# Beginner loop, farms both grass and wood.

while True:
	for i in range(get_world_size()):
		for w in range(get_world_size()):
			
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			move(East)
		move(North)

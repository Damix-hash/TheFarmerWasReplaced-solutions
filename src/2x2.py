# Beginner loop, farms wood only (forgot theres cooldown for the grass harvest)

while True:
	for i in range(get_world_size()):
		for w in range(get_world_size()):
			
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			move(East)
		move(North)

# Pumpkin Dilemma

Carrot = Entities.Carrot
Tree = Entities.Tree
Grass = Grounds.Grassland
Soil = Grounds.Soil

def move_to(x, y):
	while True:
		if (get_pos_y() < y):
			move(North)
		
		elif (get_pos_y() > y):
			move(South)
			
		if (get_pos_x() < x):
			move(East)
			
		elif (get_pos_x() > x):
			move(West)
			
		if ((get_pos_y() == y) and (get_pos_x() == x)):
			break

move_to(0, 0)

while True:
	all_good = True

	for x in range(get_world_size()):
		for y in range(get_world_size()):
			
			if get_ground_type() == Grass:
				till()

			if get_ground_type() == Soil:

				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					all_good = False

				elif get_entity_type() == Entities.Pumpkin and can_harvest():
					pass
				else:
					all_good = False

				plant(Entities.Pumpkin)

			move(East)
		move(North)

	if all_good:
		harvest()

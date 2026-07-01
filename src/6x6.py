# 6x6
# unlocked variables (finally)

Carrot = Entities.Carrot
Tree = Entities.Tree
Grass = Grounds.Grassland
Soil = Grounds.Soil

while True:
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if can_harvest():
				harvest()
			
			if (y % 2 != 0 and x % 2 == 0):
				plant(Tree)

			elif (y % 2 == 0 and x % 2 != 0):
				if get_ground_type() == Grass:
					till()
				
				if get_ground_type() == Soil:
					plant(Carrot)
					
			if ((get_entity_type() == Carrot or get_entity_type() == Tree)):
				if get_water() < 0.5:
					use_item(Items.Water)
				
			move(East)
		move(North)

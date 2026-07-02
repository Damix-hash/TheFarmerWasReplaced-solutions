# sunflower dillema

from movement import move_to
from sort import insertion_sort

Carrot = Entities.Carrot
Tree = Entities.Tree
Pumpkin = Entities.Pumpkin
Sunflower = Entities.Sunflower
Grass = Grounds.Grassland
Soil = Grounds.Soil

while True:
	Last_Measure = []
	Solution = []
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			move_to(x, y)
	
			if get_ground_type() != Soil:
				till()
						
			if get_entity_type() != Sunflower:
				plant(Sunflower)
			elif get_entity_type() == Sunflower:
				Last_Measure.append({"measurement": measure(), "pos": (get_pos_x(), get_pos_y())})
				
	if Last_Measure:
		Solution = insertion_sort(Last_Measure)
		
		for i in Solution:
			x, y = i["pos"][0], i["pos"][1]
			
			move_to(x,y)
			if can_harvest():
				harvest()

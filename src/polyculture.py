# Polyculture
# move_to function implementation is at: https://github.com/Damix-hash/TheFarmerWasReplaced-solutions/blob/main/src/move_to.py
Carrot = Entities.Carrot
Tree = Entities.Tree
Pumpkin = Entities.Pumpkin
Grass = Grounds.Grassland
Soil = Grounds.Soil

from movement import move_to

def companion_data(comp):
	data = comp
	
	if data != None:
		return {
			"companion": data[0],
			"coordinates": data[1]
		}
	else:
		return None

while True:
	data = companion_data(get_companion())
			
	if data != None:
		move_to(data["coordinates"][0], data["coordinates"][1])
		if can_harvest():
			harvest()
		
		if (data["companion"] == Carrot or data["companion"] == Pumpkin):
			if get_ground_type() == Grass:
				till()
		else:
			if get_ground_type() == Soil:
				till()
	
		if (get_entity_type() != data["companion"]):
	
			plant(data["companion"])

		if (get_water() < 0.75 and num_items(Items.Water) > 100):
			use_item(Items.Water)
	else:
		move(East)


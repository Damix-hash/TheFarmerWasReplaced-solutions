def move_to(x=0, y=0):
	
	world_size = get_world_size()
	
	while True:
		if ((get_pos_y() == y) and (get_pos_x() == x)):
			break
			
		delta_x = (x - get_pos_x()) % world_size
		delta_y = (y - get_pos_y()) % world_size
		
		if delta_x != 0:
			if delta_x <= world_size // 2:
				move(East)
			else:
				move(West)
				
		if delta_y != 0:
			if delta_y <= world_size // 2:
				move(North)
			else:
				move(South)

if __name__ == "__main__":
	move_to(10, 1)

def move_to(y, x):
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

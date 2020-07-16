
cell = (i,j)
neighbours = [(cell[0]-1,cell[1]-1),(cell[0]-1,cell[1]),(cell[0]-1,cell[1]+1),(cell[0],cell[1]-1),(cell[0],cell[1]+1),\
			(cell[0]+1,cell[1]-1),(cell[0]+1,cell[1]),(cell[0]+1,cell[1]+1)]

for cell_x in neighbours:

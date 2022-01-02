import sys

# demo sudoku :
# 006840000201060007039000010000098300060000090007320000040000130700010804000035700

def showgrid(grid, solution):
	print()
	print('┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓')
	for row in range(9):
		if row%3:
			print('┠───┼───┼───╂───┼───┼───╂───┼───┼───┨')
		elif row%9:
			print('┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫')
		for col in range(9):
			if col%3:
				print('│', end='')
			else:
				print('┃', end='')
			n = grid[col][row]
			s = solution[col][row]
			print('' if n else '\x1b[1;36m', n if n else (s if s else '?'), end='\x1b[0m ')
		print('┃')
	print('┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛')

def copyarray(a):
	return [[c for c in b] for b in a]

def solve(grid, col, row):
	if row >= 9:
		showgrid(initial, grid)
		return
	nextcol = (col + 1) % 9
	nextrow = row + (col + 1) // 9
	if grid[col][row]:
		solve(copyarray(grid), nextcol, nextrow)
		return
	line = [n for n in [grid[i][row] for i in range(9)] if n]
	column = [n for n in [grid[col][i] for i in range(9)] if n]
	box = [n for n in [grid[i+(col//3)*3][j+(row//3)*3] for i in range(3) for j in range(3)] if n]
	alreadytaken = line + column + box
	for i in range(1, 10):
		if not i in alreadytaken:
			subgrid = copyarray(grid)
			subgrid[col][row] = i
			solve(subgrid, nextcol, nextrow)

if __name__ == '__main__':
	initial = [[int(sys.argv[1][j*9+i]) for j in range(9)] for i in range(9)]
	showgrid(initial, initial)
	solve(initial, 0, 0)
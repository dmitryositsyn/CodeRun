#  263. Yandex Cells

import sys
from functools import lru_cache


class SMN:
	def __init__(self, nr, nc):
		self.root = []
		self.rk = []
		self.d1, self.d2, self.d3 = {}, {}, {}
		fill_data(self, nr, nc)

def handle_vertical(table, dcells, cell_from, cell_to):
	lplus, rplus = (dcells[cell_from][0] - 1, dcells[cell_from][1] - 1), (dcells[cell_from][0] - 1, dcells[cell_to][1] + dcells[cell_to][3])
	for col_idx in range(dcells[cell_from][1], dcells[cell_to][1] + dcells[cell_to][3]):
		table[dcells[cell_from][0] - 1][col_idx] = " "
	if lplus[1] == 0:
		table[lplus[0]][lplus[1]] = "|"
	elif table[lplus[0]][lplus[1] - 1] == "-":
		table[lplus[0]][lplus[1]] = "+"
	else:
		table[lplus[0]][lplus[1]] = "|"
	if rplus[1] == len(table[0]) - 1:
		table[rplus[0]][rplus[1]] = "|"
	elif table[rplus[0]][rplus[1] + 1] == "-":
		table[rplus[0]][rplus[1]] = "+"
	else:
		table[rplus[0]][rplus[1]] = "|"
	print("Merged vertically-aligned cells")
	for i in range(len(table)):
		for j in range(len(table[0])):
			print(table[i][j], end="")
		sys.stdout.write("\n")

def handle_horizontal(table, dcells, cell_from, cell_to):
	uplus, bplus = (dcells[cell_from][0] - 1, dcells[cell_from][1] - 1), (dcells[cell_to][0] + dcells[cell_to][2], dcells[cell_from][1] - 1)
	for row_idx in range(dcells[cell_from][0], dcells[cell_to][0] + dcells[cell_to][2]):
		table[row_idx][dcells[cell_from][1] - 1] = " "
	if uplus[0] == 0:
		table[uplus[0]][uplus[1]] = "-"
	elif table[uplus[0] - 1][uplus[1]] == "|":
		table[uplus[0]][uplus[1]] = "+"
	else:
		table[uplus[0]][uplus[1]] = "-"
	if bplus[0] == len(table) - 1:
		table[bplus[0]][bplus[1]] = "-"
	elif table[bplus[0] + 1][bplus[1]] == "|":
		table[bplus[0]][bplus[1]] = "+"
	else:
		table[bplus[0]][bplus[1]] = "-"
	print("Merged horizontally-aligned cells")
	for i in range(len(table)):
		for j in range(len(table[0])):
			print(table[i][j], end="")
		sys.stdout.write("\n")

def merge(table, dcells, smn, first_cell_to_merge, second_cell_to_merge):
	if find(smn, first_cell_to_merge) == find(smn, second_cell_to_merge):
		print("Can not merge cell with itself")
		return
	p1, p2 = find(smn, first_cell_to_merge), find(smn, second_cell_to_merge)
	p1_c, p2_c = smn.d3[smn.d2[p1]], smn.d3[smn.d2[p2]]
	if p1_c[2][1] + 1 == p2_c[0][1] and p1_c[3][1] + 1 == p2_c[1][1] and p1_c[2][0] == p2_c[0][0] and p1_c[3][0] == p2_c[1][0]:
		handle_vertical(table,dcells,f"{p2_c[0][0]}{p2_c[0][1]}",f"{p2_c[1][0]}{p2_c[1][1]}")
		union(smn, p1, p2)
	elif p1_c[0][1] - 1 == p2_c[2][1] and p1_c[1][1] - 1 == p2_c[3][1] and p1_c[0][0] == p2_c[2][0] and p1_c[1][0] == p2_c[3][0]:
		handle_vertical(table,dcells,f"{p1_c[0][0]}{p1_c[0][1]}",f"{p1_c[1][0]}{p1_c[1][1]}")
		union(smn, p1, p2)
	elif convert_index(p1_c[1][0]) + 1 == convert_index(p2_c[0][0]) and convert_index(p1_c[3][0]) + 1 == convert_index(p2_c[2][0]) and p1_c[1][1] == p2_c[0][1] and p1_c[3][1] == p2_c[2][1]:
		handle_horizontal(table,dcells,f"{p2_c[0][0]}{p2_c[0][1]}",f"{p2_c[2][0]}{p2_c[2][1]}")
		union(smn, p1, p2)
	elif convert_index(p1_c[0][0]) - 1 == convert_index(p2_c[1][0]) and convert_index(p1_c[2][0]) - 1 == convert_index(p2_c[3][0]) and p1_c[0][1] == p2_c[1][1] and p1_c[2][1] == p2_c[3][1]:
		handle_horizontal(table,dcells,f"{p1_c[0][0]}{p1_c[0][1]}",f"{p1_c[2][0]}{p1_c[2][1]}")
		union(smn, p1, p2)
	else:
		sys.stdout.write("Can not merge unaligned cells\n")

def split(table, dcells, snm, cell_to_split):
	ans = 0
	rc = snm.d2[find(smn, cell_to_split)]
	ccells = snm.d3[rc]
	if ccells[0] == ccells[1] == ccells[2] == ccells[3]:
		sys.stdout.write("Can not split elementary cell\n")
	else:
		cc = ccells[0]
		cc2, cc3 = cc[0], convert_number(convert_index(ccells[3][0]) + 1)
		cc4 = (ccells[2][0], ccells[2][1] + 1)
		while cc != cc4:
			if cc[0] == cc3:
				cc = (cc2, cc[1] + 1)
			else:
				ans += 1
				cell_idx = f"{cc[0]}{cc[1]}"
				cell_attributes = dcells[cell_idx]
				for col_idx in range(cell_attributes[1], cell_attributes[1] + cell_attributes[3]):
					table[cell_attributes[0] - 1][col_idx] = "-"
				for row_idx in range(cell_attributes[0], cell_attributes[0] + cell_attributes[2]):
					table[row_idx][cell_attributes[1] - 1] = "|"
				table[cell_attributes[0] - 1][cell_attributes[1] - 1] = "+"
				table[cell_attributes[0] + cell_attributes[2]][cell_attributes[1] + cell_attributes[3]] = "+"
				seen_cell_idx = snm.d1[cell_idx]
				snm.root[seen_cell_idx] = seen_cell_idx
				snm.rk[seen_cell_idx] = 1
				default_col, default_row = dcells[cell_idx][4][0], dcells[cell_idx][4][1]
				tmp = (default_col, default_row)
				snm.d3[cell_idx] = [tmp, tmp, tmp, tmp]
				cc = (convert_number(convert_index(cc[0]) + 1), cc[1])
		print(f"Split onto {ans} cells")
		for i in range(len(table)):
			for j in range(len(table[0])):
				print(table[i][j], end="")
			sys.stdout.write("\n")

@lru_cache(maxsize=100000)
def convert_number(n):
	ans = ""
	while n > 0:
		ans = chr(65 + (n - 1) % 26) + ans
		n = (n - 1) // 26
	return ans

@lru_cache(maxsize=100000)
def convert_index(index):
	ans = 0
	for c in index:
		ans = ans * 26 + (ord(c) - 64)
	return ans

def find(smn, x):
	if isinstance(x, str):
		x = smn.d1[x]
	if x == smn.root[x]:
		return x
	smn.root[x] = find(smn, smn.root[x])
	return smn.root[x]

def union(smn, x, y):
	root_x = find(smn, x)
	root_y = find(smn, y)
	if root_x != root_y:
		if smn.rk[root_x] > smn.rk[root_y]:
			smn.root[root_y] = root_x
			change_outside(smn, root_x, root_y)
		elif smn.rk[root_x] < smn.rk[root_y]:
			smn.root[root_x] = root_y
			change_outside(smn, root_y, root_x)
		else:
			smn.root[root_y] = root_x
			smn.rk[root_x] += 1
			change_outside(smn, root_x, root_y)

def change_outside(smn, x, y):
	smn.d3[smn.d2[x]][3] = max(smn.d3[smn.d2[x]][3], smn.d3[smn.d2[y]][3], key=lambda x: (convert_index(x[0]), x[1]))
	smn.d3[smn.d2[x]][2] = min(smn.d3[smn.d2[x]][2], smn.d3[smn.d2[y]][2], key=lambda x: (convert_index(x[0]), -x[1]))
	smn.d3[smn.d2[x]][1] = min(smn.d3[smn.d2[x]][1], smn.d3[smn.d2[y]][1], key=lambda x: (-convert_index(x[0]), x[1]))
	smn.d3[smn.d2[x]][0] = min(smn.d3[smn.d2[x]][0], smn.d3[smn.d2[y]][0], key=lambda x: (convert_index(x[0]), x[1]))

def fill_data(smn, nr, nc, i=0):
	for row in range(1, nr + 1):
		for col in range(1, nc + 1):
			smn.rk.append(1)
			smn.root.append(i)
			cell = f"{convert_number(col)}{row}"
			smn.d1[cell] = i
			smn.d2[i] = cell
			tmp = (convert_number(col), row)
			smn.d3[cell] = [tmp, tmp, tmp, tmp]
			i += 1

mrow, mcol = tuple(map(int, input().split()))
table = [['' for i in range(mcol)] for j in range(mrow)]

for i in range(mrow):
	line = input()
	for j in range(mcol):
		table[i][j] = line[j]

row, hi = int(input()), tuple(map(int, input().split()))
col, wi = int(input()), tuple(map(int, input().split()))

dcells = {}
ci = cj = 1
for i in range(row):
	for j in range(col):
		ii = convert_number(j + 1)
		jj = i + 1
		dcells[f"{ii}{jj}"] = [ci, cj, hi[i], wi[j], (ii, jj)]
		cj += wi[j] + 1
	cj = 1
	ci += hi[i] + 1

smn = SMN(row, col)

for k, v in dcells.items():
	tli, tlj = v[0], v[1]
	bri, brj = v[0]+v[2]-1, v[1]+v[3]-1

	if table[tli][tlj - 1] == " ":
		union(smn, k, convert_number(convert_index(v[4][0]) - 1) + str(v[4][1]))
	if table[tli - 1][tlj] == " ":
		union(smn, k, v[4][0] + str(v[4][1] - 1))
	if table[bri][brj + 1] == " ":
		union(smn, k, convert_number(convert_index(v[4][0]) + 1) + str(v[4][1]))
	if table[bri + 1][brj] == " ":
		union(smn, k, v[4][0] + str(v[4][1] + 1))

for i in range(int(input())):
	q = sys.stdin.readline().split()
	if q[0] == "split":
		split(table, dcells, smn, q[1])
	if q[0] == "merge":
		merge(table, dcells, smn, q[1], q[2])
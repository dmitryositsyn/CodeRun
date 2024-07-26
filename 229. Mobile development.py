#  229. Мобилки

import heapq
from collections import Counter
import functools

def prepare_data():
	answer = 0
	heap_minimum = []
	heap_maximum = []
	skills = []
	num_participants = int(input())
	for prog, manager in zip(list(map(int, input().split())), list(map(int, input().split()))):
		skills.append([prog, manager])
		length = len(skills)-1
		if len(heap_minimum) < num_participants // 2:
			heapq.heappush(heap_minimum, KEY((manager-prog, length)))
		else:
			if manager-prog > heap_minimum[0].obj[0]:
				manager_id = heapq.heappop(heap_minimum).obj[1]
				heapq.heappush(heap_maximum, KEY((skills[manager_id][0]-skills[manager_id][1], manager_id)))
				heapq.heappush(heap_minimum, KEY((manager-prog, length)))
			else:
				heapq.heappush(heap_maximum, KEY((prog-manager, length)))
		answer = prog + answer
	return heap_minimum, heap_maximum, skills, answer

KEY = functools.cmp_to_key(lambda o1, o2: 1 if o1[0] > o2[0] else 0 if o1[0] == o2[0] else -1)
memo_min = Counter()
memo_max = Counter()

heap_minimum, heap_maximum, skills, answer = prepare_data()

managers_set = set()
for attributes in heap_minimum:
	attr_obj = attributes.obj
	answer = (skills[attr_obj[1]][1]-skills[attr_obj[1]][0]) + answer
	managers_set.add(attr_obj[1])

for i in range(int(input())):
	id, skill, score = map(int, input().split())
	if id-1 not in managers_set:
		dev_skill, manager_skill = skills[id-1]
		memo_max[(dev_skill - manager_skill, id-1)] += 1
		if skill-1 == 0:
			skills[id-1][0] += score
		else:
			skills[id-1][1] += score
		heapq.heappush(heap_minimum, KEY((skills[id-1][1] - skills[id-1][0], id-1)))
		while memo_min[heap_minimum[0].obj] > 0:
			memo_min[heap_minimum[0].obj] -= 1
			if memo_min[heap_minimum[0].obj] == 0:
				del memo_min[heap_minimum[0].obj]
			heapq.heappop(heap_minimum)
		nd, updated_id = heapq.heappop(heap_minimum).obj
		if updated_id in managers_set:
			managers_set.remove(updated_id)
			managers_set.add(id-1)
		if id-1 != updated_id:
			answer = answer - skills[updated_id][1] - skills[id-1][0] + skills[id-1][1] + skills[updated_id][0]
		else:
			answer += skills[updated_id][0] - dev_skill
		heapq.heappush(heap_maximum, KEY((-nd, updated_id)))
	else:
		dev_skill, manager_skill = skills[id-1]
		memo_min[(manager_skill - dev_skill, id-1)] += 1
		if skill-1 == 0:
			skills[id-1][0] += score
		else:
			skills[id-1][1] += score
		heapq.heappush(heap_maximum, KEY((skills[id-1][0] - skills[id-1][1], id-1)))
		while memo_max[heap_maximum[0].obj] > 0:
			memo_max[heap_maximum[0].obj] -= 1
			if memo_max[heap_maximum[0].obj] == 0:
				del memo_max[heap_maximum[0].obj]
			heapq.heappop(heap_maximum)
		nd, updated_id = heapq.heappop(heap_maximum).obj
		managers_set.remove(id-1)
		managers_set.add(updated_id)
		if id-1 != updated_id:
			answer = answer - skills[id-1][1] - skills[updated_id][0] + skills[updated_id][1] + skills[id-1][0]
		else:
			answer += skills[updated_id][1] - manager_skill
		heapq.heappush(heap_minimum, KEY((-nd, updated_id)))
	print(answer) 
#  234. MEW HTTP

import collections
import http.client


url = "127.0.0.1"
port = 7777


def process_three_equals(v_items, answers_minus_3, answer):
	second_and_third_values = collections.Counter(
		get_values([v_items[1], v_items[2]])
	)
	is_subset = True
	for key in second_and_third_values:
		if key not in answers_minus_3:
			is_subset = False

	if len(second_and_third_values) == 1:
		answer[v_items[1]] = answer[
			v_items[2]
		] = second_and_third_values.most_common()[0][0]
		del answers_minus_3[answer[v_items[1]]]

		first_value = get_values([v_items[0]])[0]
		answer[v_items[0]] = first_value
		del answers_minus_3[first_value]
		answer[v_items[3]] = answers_minus_3.most_common()[0][0]
	elif is_subset:
		third_and_fourth_values = collections.Counter(
			get_values([v_items[2], v_items[3]])
		)
		if len(third_and_fourth_values) == 1:
			answer[v_items[2]] = answer[
				v_items[3]
			] = third_and_fourth_values.most_common()[0][0]
			del second_and_third_values[answer[v_items[2]]]
			del answers_minus_3[answer[v_items[3]]]

			answer[v_items[1]] = second_and_third_values.most_common()[0][0]
			del answers_minus_3[answer[v_items[1]]]
			answer[v_items[0]] = answers_minus_3.most_common()[0][0]
		else:
			key_to_delete = None
			for key in third_and_fourth_values:
				if key in second_and_third_values:
					key_to_delete = key
			answer[v_items[2]] = key_to_delete
			del third_and_fourth_values[key_to_delete]
			del second_and_third_values[key_to_delete]

			answer[v_items[1]] = second_and_third_values.most_common()[0][0]
			answer[v_items[3]] = third_and_fourth_values.most_common()[0][0]
			del answers_minus_3[v_items[1]]
			del answers_minus_3[v_items[3]]

			answer[v_items[0]] = answers_minus_3.most_common()[0][0]
	else:
		key_to_delete = None
		for key in second_and_third_values:
			if key not in answers_minus_3:
				key_to_delete = key
		answer[v_items[2]] = key_to_delete
		del second_and_third_values[key_to_delete]
		second_value = second_and_third_values.most_common()[0][0]
		answer[v_items[1]] = second_value
		del answers_minus_3[second_value]

		first_value = get_values([v_items[0]])[0]
		answer[v_items[0]] = first_value
		del answers_minus_3[first_value]
		answer[v_items[3]] = answers_minus_3.most_common()[0][0]

	get_answer(answer, v_items)


def get_values(items):
	answer = []
	conn = http.client.HTTPConnection(url, port)
	headers = {"x-cat-variable": ", ".join(items)}
	conn.request("MEW", "/", headers=headers)
	res = conn.getresponse()
	for header, value in res.getheaders():
		if header.lower().startswith("x-cat-value"):
			answer.append(value)
	conn.close()
	return answer


def get_answer(answer, v_items):
	for variable in v_items:
		print(answer[variable])
	exit()


answer = {}
v_items = []
for _ in range(4):
	variable = input()
	v_items.append(variable)

if len(set(v_items)) != 4:
	variable_to_count = collections.Counter(v_items)
	most_common_variable, _ = variable_to_count.most_common(1)[0]
	most_common_value = get_values([most_common_variable])[0]
	answer[most_common_variable] = most_common_value
	for variable in v_items:
		if variable not in answer:
			print(get_values([variable])[0])
		else:
			print(answer[variable])
	exit()

answers_minus_3 = collections.Counter(
	get_values([v_items[0], v_items[1], v_items[3]])
)

if len(answers_minus_3) == 3:
	process_three_equals(v_items, answers_minus_3, answer)

answers_minus_2 = collections.Counter(
	get_values([v_items[0], v_items[2], v_items[3]])
)

if len(answers_minus_3) == 1:
	answer[v_items[0]] = answer[v_items[1]] = answer[v_items[3]] = list(
		answers_minus_3.keys()
	)[0]
	answer[v_items[2]] = get_values([v_items[2]])[0]
	get_answer(answer, v_items)
elif len(answers_minus_2) == 1:
	answer[v_items[0]] = answer[v_items[2]] = answer[v_items[3]] = list(
		answers_minus_2.keys()
	)[0]
	answer[v_items[1]] = get_values([v_items[1]])[0]
	get_answer(answer, v_items)
elif len(answers_minus_3) == 3 and len(answers_minus_2) == 3:
	key_to_delete = None
	for key in answers_minus_3:
		if key not in answers_minus_2:
			key_to_delete = key
	answer[v_items[1]] = key_to_delete
	del answers_minus_3[key_to_delete]

	key_to_delete = None
	for key in answers_minus_2:
		if key not in answers_minus_3:
			key_to_delete = key
	answer[v_items[2]] = key_to_delete
	del answers_minus_2[key_to_delete]

	first_answer = get_values([v_items[0]])[0]
	answer[v_items[0]] = first_answer
	for key in answers_minus_3:
		if key != v_items[0]:
			answer[v_items[3]] = key
	get_answer(answer, v_items)
elif len(answers_minus_3) == 2 and len(answers_minus_2) == 3:
	for key in answers_minus_2:
		if key not in answers_minus_3:
			answer[v_items[2]] = key
	del answers_minus_2[answer[v_items[2]]]

	first_answer = get_values([v_items[0]])[0]
	answer[v_items[0]] = first_answer
	answers_minus_2[first_answer] -= 1
	if answers_minus_2[first_answer] == 0:
		del answers_minus_2[first_answer]
	answers_minus_3[first_answer] -= 1
	if answers_minus_3[first_answer] == 0:
		del answers_minus_3[first_answer]

	answer[v_items[3]] = list(answers_minus_2.keys())[0]
	answers_minus_2[answer[v_items[3]]] -= 1
	if answers_minus_2[answer[v_items[3]]] == 0:
		del answers_minus_2[answer[v_items[3]]]
	answers_minus_3[answer[v_items[3]]] -= 1
	if answers_minus_3[answer[v_items[3]]] == 0:
		del answers_minus_3[answer[v_items[3]]]

	answer[v_items[1]] = list(answers_minus_3.keys())[0]
	get_answer(answer, v_items)
elif len(answers_minus_3) == 3 and len(answers_minus_2) == 2:
	for key in answers_minus_3:
		if key not in answers_minus_2:
			answer[v_items[1]] = key
	del answers_minus_3[answer[v_items[1]]]

	first_answer = get_values([v_items[0]])[0]
	answer[v_items[0]] = first_answer
	answers_minus_2[first_answer] -= 1
	if answers_minus_2[first_answer] == 0:
		del answers_minus_2[first_answer]
	answers_minus_3[first_answer] -= 1
	if answers_minus_3[first_answer] == 0:
		del answers_minus_3[first_answer]

	answer[v_items[3]] = list(answers_minus_3.keys())[0]
	answers_minus_2[answer[v_items[3]]] -= 1
	if answers_minus_2[answer[v_items[3]]] == 0:
		del answers_minus_2[answer[v_items[3]]]
	answers_minus_3[answer[v_items[3]]] -= 1
	if answers_minus_3[answer[v_items[3]]] == 0:
		del answers_minus_3[answer[v_items[3]]]

	answer[v_items[2]] = list(answers_minus_2.keys())[0]
	get_answer(answer, v_items)
elif (
	len(answers_minus_3) == 2
	and len(answers_minus_2) == 2
	and answers_minus_2 != answers_minus_3
):
	if set(answers_minus_2.keys()) != set(answers_minus_3.keys()):
		for key in answers_minus_3:
			if key not in answers_minus_2:
				answer[v_items[1]] = key
		del answers_minus_3[v_items[1]]

		for key in answers_minus_2:
			if key not in answers_minus_3:
				answer[v_items[2]] = key
		del answers_minus_2[v_items[2]]
	else:
		second_value, _ = answers_minus_3.most_common()[0]
		answer[v_items[1]] = second_value
		answers_minus_3[second_value] -= 1

		third_value, _ = answers_minus_2.most_common()[0]
		answer[v_items[2]] = third_value
		answers_minus_2[third_value] -= 1

	first_answer = get_values([v_items[0]])[0]
	answer[v_items[0]] = first_answer
	answers_minus_3[answer[v_items[0]]] -= 1

	keys_to_delete = []
	for key in answers_minus_3:
		if answers_minus_3[key] == 0:
			keys_to_delete.append(key)
	for key in keys_to_delete:
		del answers_minus_3[key]

	answer[v_items[3]] = list(answers_minus_3.keys())[0]
	get_answer(answer, v_items)
elif answers_minus_2 == answers_minus_3:
	intersects_twice, intersects_once = answers_minus_3.most_common()
	intersects_twice = intersects_twice[0]
	intersects_once = intersects_once[0]

	first_three_answers = collections.Counter(
		get_values([v_items[0], v_items[1], v_items[2]])
	)
	if first_three_answers[intersects_twice] == 3:
		answer[v_items[0]] = intersects_twice
		answer[v_items[1]] = intersects_twice
		answer[v_items[2]] = intersects_twice
		answer[v_items[3]] = intersects_once
	elif (
		first_three_answers[intersects_twice] == 2
		and first_three_answers[intersects_once] == 1
	):
		answer[v_items[0]] = intersects_once
		answer[v_items[1]] = intersects_twice
		answer[v_items[2]] = intersects_twice
		answer[v_items[3]] = intersects_twice
	elif (
		first_three_answers[intersects_twice] == 1
		and first_three_answers[intersects_once] == 2
	):
		answer[v_items[0]] = intersects_twice
		answer[v_items[1]] = intersects_once
		answer[v_items[2]] = intersects_once
		answer[v_items[3]] = intersects_twice

	get_answer(answer, v_items)
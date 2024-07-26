#  239. Сервис подписки

import sys
import json


DOT_SYMBOL = "."
SHIFT = 2
SEPARATORS = (",", ":")
FIELDS = ("price", "stock_count", "partner_content.title", "partner_content.description")


class Tools:
	@staticmethod
	def get_answer_chunk(s, offer):
		ans = dict(id=offer["id"])
		for f in s["t"]:
			Tools.insert(f, ans, offer)
		for f in s["s"]:
			Tools.insert(f, ans, offer)
		return ans


	@staticmethod
	def update(field, offer, req):
		if DOT_SYMBOL in field:
			f = field.split(DOT_SYMBOL)
			p, n = f[0], f[1:]
			if p in req:
				if p not in offer:
					offer[p] = dict()
				trigger = Tools.update(DOT_SYMBOL.join(n), offer[p], req[p])
				if trigger:
					return [p] + [f"{p}.{t}" for t in trigger]
		elif field in req:
			if field not in offer or offer[field] != req[field]:
				offer[field] = req[field]
				return [field]


	@staticmethod
	def insert(field, data, offer):
		if DOT_SYMBOL in field:
			f = field.split(DOT_SYMBOL)
			p, n = f[0], f[1:]
			if p in offer:
				if p not in data:
					data[p] = dict()
				Tools.insert(DOT_SYMBOL.join(n), data[p], offer[p])
		elif field in offer:
			data[field] = offer[field]


n, m = map(int, sys.stdin.readline().rstrip("\n").strip().split())

input_data = []
for i in range(n):
	line = sys.stdin.readline().rstrip("\n").split(" ")
	t_num, s_num = int(line[0]), int(line[1])
	chunk = {"t": line[SHIFT : t_num + SHIFT], "s": line[t_num + SHIFT : t_num + s_num + SHIFT]}
	input_data.append(chunk)


offers, ans = [], []
for ii in range(m):
	req = json.loads(sys.stdin.readline().rstrip("\n").strip())
	ro = req["offer"]
	offer = []
	for obj in offers:
		if obj["id"] == ro["id"]:
			offer.append(obj)
	if offer:
		offer = offer[0]
	else:
		offer = dict(id=ro["id"])
		offers.append(offer)

	subscribers_candidates = list(enumerate(input_data))
	subscribers_for_req = []

	for f in FIELDS:
		triggers = Tools.update(f, offer, ro)
		if triggers:
			subscribers_for_trigger = [
				(i, s)
				for i, s in subscribers_candidates
				if any(obj in triggers for obj in s["t"])
			]
			subscribers_for_req += subscribers_for_trigger
			for s in subscribers_for_trigger:
				subscribers_candidates.remove(s)

	subscribers_for_req.sort(key=lambda x: x[0])

	for _, s in subscribers_for_req:
		ans.append(json.dumps(dict(trace_id=req["trace_id"], offer=Tools.get_answer_chunk(s, offer)), separators=SEPARATORS))


sys.stdout.write("\n".join(ans))

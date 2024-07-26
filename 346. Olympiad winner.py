#  346. Победитель олимпиады

import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict

def downloads_subs(name, part):
	url_with_params = (
		"http://127.0.0.1:7777/view/submissions?"
		+ urllib.parse.urlencode({"contest": name, "login": part})
	)
	with urllib.request.urlopen(url_with_params) as response:
		root = ET.fromstring(response.read())

	submissions = defaultdict(set)
	submissions["attempts"] = defaultdict(list)
	for s in root.iter("submission"):
		if s.attrib["verdict"] != "CE":
			submissions["attempts"][s.attrib["problem"]].append((int(s.attrib["timestamp"]), s.attrib["verdict"]))
			if s.attrib["verdict"] == "OK":
				submissions["solved"].add(s.attrib["problem"])

	return submissions

contest = input()
with urllib.request.urlopen(
	"http://127.0.0.1:7777/view/participants?"
	+ urllib.parse.urlencode({"contest": contest})
) as response:
	root = ET.fromstring(response.read())

solved = defaultdict(list)
participants = {}
maximum = 0
for p in root.iter("participant"):
	sumbmissions = downloads_subs(contest, p.attrib["login"])
	num = len(sumbmissions["solved"])
	if num > maximum:
		maximum = max(num, maximum)
	solved[num].append(p.attrib["login"])
	participants[p.attrib["login"]] = sumbmissions

minimum = 999999999999999999999
if len(solved[maximum]) != 1:
	mapping = defaultdict(list)
	for p in solved[maximum]:
		statistics = participants[p]
		total = 0
		for solv in statistics["solved"]:
			sub = list(sorted(statistics["attempts"][solv]))
			for t, v in sub:
				if v == "OK":
					total += int(t)
					break
				else:
					total += 20
		minimum = min(minimum, total)
		mapping[total].append(p)

	print(len(mapping[minimum]))
	for p in sorted(mapping[minimum]):
		print(p)
else:
	print(1)
	print(solved[maximum][0])
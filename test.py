def test_index(liste, index):
	for i in index:
		if not liste[i]:
			return 0
	return 1

print test_index([0, 1, 0, 0, 0, 1, 0], [1, 5])


coucou = 1 if "lol" else "coucou"
print coucou
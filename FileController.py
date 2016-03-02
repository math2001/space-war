import pickle
import os

class FileController:
	def __init__(self):
		pass

	def save(self, mode, *path):
		path = os.path.join(path)
		if os.isfile(path):
			with open(path, mode) as f:
				return pickle.Unpickler(f).load()
		else:
			return False

	def load(self, *path):
		path = os.path.join(path)
		if os.isfile(path):
			print "coucou"

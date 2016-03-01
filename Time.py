import time

class Time:
	def __init__(self):
		self.start_time = time.time()

	def get_time(self, rounding=0):
		t = time.time() - self.start_time
		if rounding == 0:
			t = int(t)
		else:
			t = round(t, rounding)
		return t

	def reset_time(self):
		self.start_time = time.time()
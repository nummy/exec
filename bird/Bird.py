class Bird(object):
	def __init__(self, n, x0, y0, dx, dy, mass, r):
		self.name = n
		self.x0 = x0
		self.y0 = y0
		self.dx = dx
		self.dy = dy
		self.mass = mass
		self.radius = r

	def move(self):
		self.x0 = self.x0 + self.dx
		self.y0 = self.y0 + self.dy

	def decelerate(self):
		self.dx = self.dx*1.0/2

	def stop(self):
		self.dx = 0.0
		self.dy = 0.0

	def fly_away(self):
		if self.x0-self.radius<0 or self.y0-self.radius<0 or self.x0+self.radius>1000 or self.y0+self.radius>1000:
			return True
		else:
			return False

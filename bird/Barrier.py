class Barrier(object):
	def __init__(self, n, xc,yc, r0, s):
		self.name = n
		self.xc = xc
		self.yc = yc
		self.radius = r0
		self.strength = s

	def strike(self, strength):
		# strike with the bird
		self.strength = self.strength - strength
		if self.strength < 0:
			self.strength = 0.0



		
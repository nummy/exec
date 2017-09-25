import json
import sys
import os.path
import math
from Bird import *
from Pig import *
from Barrier import *


def read_file():
	fp = None
	filename = input("Enter the name of the data file => ")
	print(filename)
	try:
		fp = open(filename.strip(),'r')
	except IOError as e:
		print("Error input.")
		sys.exit(1)
	data = fp.read().strip()
	d = json.loads(data)
	return d

def init(data):
	pigs = [Pig(elem["name"], elem["xc"], elem["yc"], elem["radius"]) for elem in data.get("pigs",[])]
	birds = [Bird(elem["name"], elem["x0"], elem["y0"], 
					elem["dx"], elem["dy"],elem["mass"],
					elem["radius"]) for elem in data.get("birds", [])]
	barriers = [Barrier(elem["name"], elem["xc"], 
				elem["yc"], elem["radius"], 
				elem["strength"]) for elem in data.get("barriers", [])]
	return birds, pigs, barriers

def is_collide(bird, obstacle):
	x0 = bird.x0
	y0 = bird.y0
	xc = obstacle.xc
	yc = obstacle.yc
	radius_bird = bird.radius
	radius_obstacle = obstacle.radius
	distance = math.sqrt((x0-xc)**2+(y0-yc)**2)
	if distance <= radius_bird + radius_obstacle:
		return True
	else:
		return False

def show_info(birds, pigs, barriers):
	print("\nThere are %d birds:" % len(birds))
	for bird in birds:
		print("    %s: (%.1f,%.1f)" % (bird.name, bird.x0, bird.y0))
	print("\nThere are %d pigs:" % len(pigs))
	for pig in pigs:
		print("    %s: (%.1f,%.1f)" % (pig.name, pig.xc, pig.yc))
	print("\nThere are %d barriers:" % len(barriers))
	for barrier in barriers:
		print("    %s: (%.1f,%.1f)" % (barrier.name, barrier.xc, barrier.yc))


def main():
	data = read_file()
	birds, pigs, barriers = init(data)
	show_info(birds, pigs, barriers)
	birds.reverse()
	pigs.reverse()
	barriers.reverse()
	count = 0
	# the number of pigs is zero
	if len(pigs) == 0:
		print("Time 0: All pigs are popped. The birds win!")
		sys.exit()
	while True:
		# the number of birds is zero
		if len(birds) == 0:
			break
		bird = birds.pop()
		# print start position
		print("Time %d: %s starts at (%.1f,%.1f)" % (count,bird.name, bird.x0, bird.y0))
		win = False
		while True:
			bird.move()
			count += 1
			speed_lte6 = False
			copy_pigs = pigs[:]
			for pig in copy_pigs:
				if is_collide(bird, pig):
					print("Time %d: %s at (%.1f,%.1f) pops %s" % (count,bird.name, bird.x0, bird.y0,pig.name))
					pigs.remove(pig)
					bird.decelerate()
					speed = (bird.dx**2+bird.dy**2)**0.5
					print("Time %d: %s at (%.1f,%.1f) has (dx, dy) = (%.1f,%.1f)" % (count, bird.name, bird.x0, bird.y0, bird.dx, bird.dy))
					if speed <= 6:
						speed_lte6 = True
						print("Time %d: %s at (%.1f,%.1f) with speed %.1f stops" % (count, bird.name, bird.x0, bird.y0, speed))
						break
			# exit loop when speed <= 6, stop the bird
			if speed_lte6:
				break
			# exit when no pig left
			if len(pigs) == 0:
				print("Time %d: All pigs are popped. The birds win!" % count)
				win = True
				break
			collision = False
			copy_barriers = barriers[:]
			for barrier in copy_barriers:
				if is_collide(bird, barrier):
					strength = (bird.dx**2+bird.dy**2)*bird.mass
					barrier.strike(strength)
					bird.stop()
					print("Time %d: %s at (%.1f,%.1f) hits %s, Strength %.1f" % (count, bird.name, bird.x0, bird.y0, barrier.name, barrier.strength))
					if barrier.strength <= 0:
						print("Time %d: %s crumbles" % (count, barrier.name))
						barriers.remove(barrier)
					print("Time %d: %s at (%.1f,%.1f) has (dx, dy) = (%.1f,%.1f)" % (count, bird.name, bird.x0, bird.y0, bird.dx, bird.dy))
					print("Time %d: %s at (%.1f,%.1f) with speed 0.0 stops" % (count, bird.name, bird.x0, bird.y0))
					collision = True
					break
			if collision:
				break
			if bird.fly_away():
				print("Time %d: %s at (%.1f,%.1f) has left the game" % (count, bird.name, bird.x0, bird.y0))
				break
		if win:
			sys.exit()
	if len(pigs) == 0:
		print("Time %d: No more birds. The pigs win!" % (count))
	else:
		print("Time %d: No more birds. The pigs win!" % count)
		print("Remaining pigs:")
		pigs.reverse()
		for pig in pigs:
			print(pig.name)


if __name__ == "__main__":
	main()

class Car(object):
	def __init__(self, seats, people):
		self.seats = seats
		self.people = people

	@property
	def available_seats(self):
		return self.seats - self.people

	@property
	def full(self):
		return self.seats == self.people

	def move_to(self, car):
		people_moved = min(car.available_seats, self.people)
		car.people += people_moved
		self.people -= people_moved

	def __repr__(self):
		return f'{self.people}/{self.seats}'


def find_available_car_index(cars, available_car_index, min_car_index):
	while available_car_index > min_car_index and cars[available_car_index].full:
		available_car_index -= 1
	return available_car_index if not cars[available_car_index].full and available_car_index > min_car_index else None

def solution(P, S):
	cars = [Car(s, p) for p, s in zip(P, S)]
	cars = sorted(cars, key=lambda car: car.seats)

	available_car_index = len(cars)-1
	emptied = 0

	for car_index, car in enumerate(cars):
		if available_car_index is None: break

		while car.people:
			available_car_index = find_available_car_index(cars, available_car_index, car_index)
			if available_car_index is None: break

			available_car = cars[available_car_index]
			car.move_to(available_car)

			if not car.people:
				emptied += 1


	return len(cars) - emptied

print(solution([3,1],[4,1]))
print(solution([1,4,1],[1,5,1]))
print(solution([4,4,2,4],[5,5,2,5]))
print(solution([2,3,4,2],[2,5,7,2]))
print(solution([1,2,3,4,5,1,2,3,5,5] * 10000, [2,5,5,7,5]*20000))
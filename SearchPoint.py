from random import randint

class SearchPoint():
	'''Класс искомой точки'''
	def __init__(self, w, h):
		'''инициализация случайных координат искомой точки'''
		self.__x = randint(0, w)
		self.__y = randint(0, h)
	def where_is_point(self, x, y):
		'''Описывает положение искомой точки относительно текущей.
		Возможные варианты: "R", "RU", "RD", "L", "LU", "LD", "U", "D" , ""
		'''
		pos_x = pos_y = ''
		if x > self.__x:
			pos_x = 'L'
		elif x < self.__x:
			pos_x = 'R'
		if y > self.__y:
			pos_y = 'D'
		elif y < self.__y:
			pos_y = 'U'
		return pos_x+pos_y
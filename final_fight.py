from random import randint


class Ship:
    def __init__(self, length, tp=1, x=0, y=0):
        self._length = length
        self._tp = tp  # Тип: 1 - горизонтальный, 2 - вертикальный
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * length  # Массив, который может обозначать состояние клеток
        self.update_position()

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y
        self.update_position()

    def get_start_coords(self):
        return self._x, self._y

    def update_position(self):
        if self._tp == 1:  # Горизонтальный
            self.current_position = {'x0': self._x, 'y0': self._y, 'x1': self._x + self._length - 1, 'y1': self._y}
        else:  # Вертикальный
            self.current_position = {'x0': self._x, 'y0': self._y, 'x1': self._x, 'y1': self._y + self._length - 1}

    def move(self, go):
        if self._is_move:
            if self._tp == 1:  # Горизонтальная ориентация
                if 0 <= self._x + go <= 9:
                    self._x += go
            else:  # Вертикальная ориентация
                if 0 <= self._y + go <= 9:
                    self._y += go
            self.update_position()

    def is_collide(self, ship):
        if self._tp == 1 and ship._tp == 1:  # Горизонтальный - Горизонтальный
            if self.current_position['y0'] == ship.current_position['y0']:
                if (self.current_position['x0'] <= ship.current_position['x1'] and
                        self.current_position['x1'] >= ship.current_position['x0']):
                    return True
        elif self._tp == 1 and ship._tp == 2:  # Горизонтальный - Вертикальный
            if (self.current_position['x0'] <= ship.current_position['x0'] <= self.current_position['x1'] + 1) and \
                    (ship.current_position['y0'] <= self.current_position['y0'] <= ship.current_position['y1'] + 1):
                return True
        elif self._tp == 2 and ship._tp == 1:  # Вертикальный - Горизонтальный
            if (ship.current_position['x0'] <= self.current_position['x0'] <= ship.current_position['x1'] + 1) and \
                    (self.current_position['y0'] <= ship.current_position['y0'] <= self.current_position['y1'] + 1):
                return True
        elif self._tp == 2 and ship._tp == 2:  # Вертикальный - Вертикальный
            if self.current_position['x0'] == ship.current_position['x0']:
                if (self.current_position['y0'] <= ship.current_position['y1'] + 1 and
                        self.current_position['y1'] >= ship.current_position['y0']):
                    return True
        return False

    def is_out_pole(self, size):
        if self._tp == 1:
            return not (0 <= self._x < size and 0 <= self._x + self._length - 1 < size)
        else:
            return not (0 <= self._y < size and 0 <= self._y + self._length - 1 < size)

    def __getitem__(self, indx):
        return self._cells[indx]

    def __setitem__(self, indx, value):
        self._cells[indx] = value
        if value == 2:
            self._is_move = False


class GamePole:
    def __init__(self, size=10):
        self.size = size
        self._ships = []
        self._map = [[0 for _ in range(size)] for _ in range(size)]
        self.ship_numbers = {4: 1, 3: 2, 2: 3, 1: 4}  # Количество кораблей разных размеров

    def generate_ships(self):
        for length, count in sorted(self.ship_numbers.items(), reverse=True):
            for _ in range(count):
                while True:
                    x, y = randint(0, self.size - 1), randint(0, self.size - 1)
                    tp = randint(1, 2)  # Случайный выбор горизонтальный или вертикальный
                    ship = Ship(length, tp, x, y)
                    if not self.is_collide(ship):
                        self._ships.append(ship)
                        self.place_ship_on_map(ship)
                        break

    def is_collide(self, ship):
        for existing_ship in self._ships:
            if ship.is_collide(existing_ship):
                return True
        return False

    def place_ship_on_map(self, ship):
        for i in range(ship._length):
            if ship._tp == 1:  # Горизонтальный
                self._map[ship._y][ship._x + i] = 1
            else:  # Вертикальный
                self._map[ship._y + i][ship._x] = 1

    def move_ships(self):
        for ship in self._ships:
            potential_step = randint(-1, 1)
            if not ship.is_out_pole(self.size):
                checker = [s for s in self._ships if s != ship]
                collisions = [s.is_collide(ship) for s in checker]
                if not any(collisions):
                    self._ships.remove(ship)
                    ship.move(potential_step)
                    self._ships.append(ship)
                    self.place_ship_on_map(ship)

    def print_map(self):
        for row in self._map:
            print(" ".join(str(cell) for cell in row))
        print("\n")


if __name__ == "__main__":
    game = GamePole()
    game.generate_ships()
    game.print_map()

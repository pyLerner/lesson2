# Переменные объекта "Транспортное средство"
vehicle_type: str = 'bus'
in_fleet: bool = True           # True, если эксплуатируется, False - выведен из эксплуатации
passenger_capacity: int = 80     # Пассажировместимость
outer_turning_radius: float = 11.5

print('vehicle_type', type(vehicle_type))
print('in_fleet', type(in_fleet))
print('passenger_capacity', type(passenger_capacity))
print('outer_turning_radius', type(outer_turning_radius))

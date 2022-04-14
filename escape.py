import math

planet_radius = input('Ingrese el radio del planeta en kilómetros:')
gravitational_constant = input('Ingrese la constante gravitacional:')

planet_radius_num = int(planet_radius)
gravitational_constant_num = float(gravitational_constant)

escape_velocity = math.sqrt(2 * (planet_radius_num * 1000) * gravitational_constant_num)

print(f'La velocidad de escape es: {escape_velocity:.1f}[m/s]')
# Reference solution for exercise 05.
from conversions import average, bar_to_psi, celsius_to_kelvin, l_s_to_m3_h

pressures_bar = [7.1, 7.4, 7.6, 7.2]
temperature_c = 83.5
flow_l_s = 41.5

average_bar = average(pressures_bar)
print("Average pressure (bar):", average_bar)
print("Average pressure (psi):", round(bar_to_psi(average_bar), 2))
print("Temperature (K):", celsius_to_kelvin(temperature_c))
print("Flow (m3/h):", l_s_to_m3_h(flow_l_s))

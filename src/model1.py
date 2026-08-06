import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
matplotlib.use("TkAgg")   # run matplotlib with linux

# Input - Output variables
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Fuzzification
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['warm'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['hot'] = fuzz.trimf(temperature.universe, [30, 40, 40])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Fuzzy rules
rule1 = ctrl.Rule(temperature['cold'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['warm'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], fan_speed['high'])

# Xay dung he thong
fan_ctrl = ctrl.ControlSystem(rules=[rule1, rule2, rule3])
fan = ctrl.ControlSystemSimulation(fan_ctrl)

# Nhap Crisp input
fan.input['temperature'] = int(input('Nhap nhiet do: '))

# Suy luan
fan.compute()

# Crisp output
print(f"Fan speed = {fan.output['fan_speed']}")


# Hien thi do thi
temperature.view()
fan_speed.view(sim = fan)

plt.show()
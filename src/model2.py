import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
mpl.use('TkAgg')

# I/O var
T = ctrl.Antecedent(np.arange(300, 600, 1), 'temperature')
P = ctrl.Antecedent(np.arange(500, 1000, 1), 'pressure')
angle = ctrl.Consequent(np.arange(-90, 90, 1), 'angle')

# Fuzzification
T['normal'] = fuzz.trimf(T.universe, [300, 300, 450])
T['hot'] = fuzz.trimf(T.universe, [300, 450, 600])
T['super hot'] = fuzz.trimf(T.universe, [450, 600, 600])

P['low'] = fuzz.trimf(P.universe, [500, 500, 750])
P['normal'] = fuzz.trimf(P.universe, [500, 750, 1000])
P['high'] = fuzz.trimf(P.universe, [750, 1000, 1000])

angle['-ve large'] = fuzz.trimf(angle.universe, [-90, -90, -45])
angle['-ve small'] = fuzz.trimf(angle.universe, [-90, -45, 0])
angle['zero'] = fuzz.trimf(angle.universe, [-45, 0, 45])
angle['+ve small'] = fuzz.trimf(angle.universe, [0, 45, 90])
angle['+ve large'] = fuzz.trimf(angle.universe, [45, 45, 90])

# Fuzzy rules
rule1 = ctrl.Rule(T['normal'] & P['low'], angle['+ve large'])
rule2 = ctrl.Rule(T['normal'] & P['normal'], angle['zero'])
rule3 = ctrl.Rule(T['normal'] & P['high'], angle['-ve large'])
rule4 = ctrl.Rule(T['hot'] & P['low'], angle['+ve large'])
rule5 = ctrl.Rule(T['hot'] & P['normal'], angle['zero'])
rule6 = ctrl.Rule(T['hot'] & P['high'], angle['-ve small'])
rule7 = ctrl.Rule(T['super hot'] & P['low'], angle['+ve small'])
rule8 = ctrl.Rule(T['super hot'] & P['normal'], angle['-ve large'])
rule9 = ctrl.Rule(T['super hot'] & P['high'], angle['-ve small'])

# Build
rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]
turbine_ctrl = ctrl.ControlSystem(rules=rules)
turbine = ctrl.ControlSystemSimulation(turbine_ctrl)

# Crisp input
turbine.input['temperature'] = float(input('Nhap nhiet do: '))
turbine.input['pressure'] = float(input('Nhap ap xuat: '))

turbine.compute() # Suy luan

# Crisp output
print(f"=> Goc quay tua bin: {turbine.output['angle']:.2f}")

T.view()
P.view()
angle.view(sim=turbine)
plt.show()
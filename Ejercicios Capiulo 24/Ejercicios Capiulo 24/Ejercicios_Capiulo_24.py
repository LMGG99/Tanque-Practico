"""41"""
colores = input('Introduce tu color favorito:\n')
tupla_colores = ('morado', 'rosa', 'negro', 'blanco')

if colores in tupla_colores[0]:
	print('El color morado está admitido')
elif colores in tupla_colores[1]:
	print('El color rosa está admitido')
elif colores in tupla_colores[2]:
	print('El color negro está admitido')
elif colores in tupla_colores[3]:
	print('El color blanco está admitido')
else:
	print('Color no admitido')

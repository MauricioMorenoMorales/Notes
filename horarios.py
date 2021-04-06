#? horarios de referencia = {
# 	'california': 11%,  -> 11
# 	'mexico': 13%,      -> 13 <|
# 	'guatemala': 13%,   -> 12|
# 	'colombia': 14%,    -> 13|
# 	'peru': 14%,        -> 13|
# 	'venezuela': 15%,   -> 14|
# 	'bolivia': 15%,     -> 14|
# 	'chile': 16%,       -> 14|
# 	'madrid': 20%,      -> 20
# }

def main():
	pais_seleccionado = input("¿En qué país te encuentras?: ")
	input_hora_seleccionada = input(f'Que hora de {pais_seleccionado} te gustaria evaluar (formato HH:MM): ')
	hora_seleccionada = int(input_hora_seleccionada.split(':')[0])
	minuto_seleccionado = input_hora_seleccionada.split(':')[1]
	horario_de_verano = True
	if(int(minuto_seleccionado) > 59 or int(minuto_seleccionado) < 0):
		return print("Los minutos introducidos no pueden ser mayores a 60")
	if(hora_seleccionada > 24 or hora_seleccionada < 0):
		return print('La introducida no puede ser mayor a 24')
	if(pais_seleccionado.lower() == "chile"):
		if(horario_de_verano):
			hora_california = hora_seleccionada - 3 if hora_seleccionada - 3 >= 0 else hora_seleccionada + 21
			hora_mexico = hora_seleccionada -1 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 23
			hora_guatemala = hora_seleccionada -2 if hora_seleccionada - 2 >= 0 else hora_seleccionada + 22
			hora_colombia = hora_seleccionada - 1 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 23
			hora_peru = hora_seleccionada - 1 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 23
			hora_venezuela = hora_seleccionada
			hora_bolivia = hora_seleccionada
			hora_madrid = hora_seleccionada + 6 if hora_seleccionada + 6 < 24 else hora_seleccionada  - 18
		else:
			hora_california = hora_seleccionada - 5 if hora_seleccionada - 5 >= 0 else hora_seleccionada + 19
			hora_mexico = hora_seleccionada -3 if hora_seleccionada - 3 >= 0 else hora_seleccionada + 21
			hora_guatemala = hora_seleccionada -3 if hora_seleccionada - 3 >= 0 else hora_seleccionada + 21
			hora_colombia = hora_seleccionada - 2 if hora_seleccionada - 2 >= 0 else hora_seleccionada + 22
			hora_peru = hora_seleccionada - 2 if hora_seleccionada - 2 >= 0 else hora_seleccionada + 22
			hora_venezuela = hora_seleccionada - 1 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 23
			hora_bolivia = hora_seleccionada - 1 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 23
			hora_madrid = hora_seleccionada + 4 if hora_seleccionada + 4 < 24 else hora_seleccionada  - 20
		print(f"""
	hora de chile:      {hora_seleccionada}:{minuto_seleccionado}
	hora de madrid:     {hora_madrid}:{minuto_seleccionado}
	hora de california: {hora_california}:{minuto_seleccionado}
	hora de mexico:     {hora_mexico}:{minuto_seleccionado}
	hora de guatemala:  {hora_guatemala}:{minuto_seleccionado}
	hora de colombia:   {hora_colombia}:{minuto_seleccionado}
	hora de peru:       {hora_peru}:{minuto_seleccionado}
	hora de venezuela:  {hora_venezuela}:{minuto_seleccionado}
	hora de bolivia:    {hora_bolivia}:{minuto_seleccionado}
			""")
	if(pais_seleccionado.lower() == "mexico" or pais_seleccionado.lower() == "méxico"):
		if(horario_de_verano):
			hora_california = hora_seleccionada - 2 if hora_seleccionada - 2 >= 0 else hora_seleccionada + 22
			hora_chile = hora_seleccionada + 1 if hora_seleccionada + 1 < 24 else hora_seleccionada - 23
			hora_guatemala = hora_seleccionada - 1 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 23
			hora_colombia = hora_seleccionada
			hora_peru = hora_seleccionada
			hora_venezuela = hora_seleccionada + 1 if hora_seleccionada + 1 < 24 else hora_seleccionada - 23
			hora_bolivia = hora_seleccionada + 1 if hora_seleccionada + 1 < 24 else hora_seleccionada - 23
			hora_madrid = hora_seleccionada + 7 if hora_seleccionada + 7 < 24 else hora_seleccionada  - 17
		else:
			hora_california = hora_seleccionada - 2 if hora_seleccionada - 2 >= 0 else hora_seleccionada + 22
			hora_chile = hora_seleccionada + 3 if hora_seleccionada + 3 < 24 else hora_seleccionada - 21
			hora_guatemala = hora_seleccionada
			hora_colombia = hora_seleccionada + 1 if hora_seleccionada + 1 < 24 else hora_seleccionada - 23
			hora_peru = hora_seleccionada + 1 if hora_seleccionada + 1 < 24 else hora_seleccionada - 23
			hora_venezuela = hora_seleccionada + 2 if hora_seleccionada + 2 < 24 else hora_seleccionada - 22
			hora_bolivia = hora_seleccionada + 2 if hora_seleccionada + 2 < 24 else hora_seleccionada - 22
			hora_madrid = hora_seleccionada + 7 if hora_seleccionada + 7 < 24 else hora_seleccionada  - 17
		print(f"""
	hora de california: {hora_california}:{minuto_seleccionado}
	hora de mexico:     {hora_seleccionada}:{minuto_seleccionado}
	hora de guatemala:  {hora_guatemala}:{minuto_seleccionado}
	hora de colombia:   {hora_colombia}:{minuto_seleccionado}
	hora de peru:       {hora_peru}:{minuto_seleccionado}
	hora de venezuela:  {hora_venezuela}:{minuto_seleccionado}
	hora de bolivia:    {hora_bolivia}:{minuto_seleccionado}
	hora de chile:      {hora_chile}:{minuto_seleccionado}
	hora de madrid:     {hora_madrid}:{minuto_seleccionado}
			""")
main()
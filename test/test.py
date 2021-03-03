#? horarios de referencia = {
# 	'chile': 16,
# 	'california': 11,
# 	'mexico': 13,
# 	'guatemala': 13,
# 	'colombia': 14,
# 	'peru': 14,
# 	'venezuela': 15,
# 	'bolivia': 15,
# 	'madrid': 20,
# }

def main():
	pais_seleccionado = input("¿En qué país te encuentras?: ")
	input_hora_seleccionada = input(f'Que hora de {pais_seleccionado} te gustaria evaluar (formato HH:MM): ')
	hora_seleccionada = int(input_hora_seleccionada.split(':')[0])
	minuto_seleccionado = int(input_hora_seleccionada.split(':')[1]) or '00'
	# if(minuto_seleccionado == False): minuto_seleccionado = '00'
	if(hora_seleccionada > 24): return print('La introducida no puede ser mayor a 24')
	if(pais_seleccionado.lower() == "chile"):
		hora_california = hora_seleccionada - 5 if hora_seleccionada - 5 >= 0 else hora_seleccionada + 19
		hora_mexico = hora_seleccionada -3 if hora_seleccionada - 3 >= 0 else hora_seleccionada + 21
		hora_guatemala = hora_seleccionada -3 if hora_seleccionada - 3 >= 0 else hora_seleccionada + 21
		hora_colombia = hora_seleccionada - 2 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 22
		hora_peru = hora_seleccionada - 2 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 22
		hora_venezuela = hora_seleccionada - 1 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 23
		hora_bolivia = hora_seleccionada - 1 if hora_seleccionada - 1 >= 0 else hora_seleccionada + 23
		hora_madrid = hora_seleccionada + 4 if hora_seleccionada + 4 <= 24 else hora_seleccionada  - 20
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
main()
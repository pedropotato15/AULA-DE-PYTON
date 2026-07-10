meses = 2
dias = 3
lista_semana = ["segunda-feira", "terça-feira", 'quarta-feira', "quinta-feira", "sexta_feira", "sábado", "domingo"]
contador_meses = 0
contador_semana = 0

for i in range(meses):
    contador_dias = 0
    contador_meses += 1
    print(f"\n------- Mes {contador_meses} -------\n")
    for i in range(dias):
        contador_dias += 1
        print(f"dia {contador_dias} - {lista_semana[contador_semana]}")
        if contador_semana < 6:
            contador_semana += 1
        else:
            contador_semana = 0   
             
       

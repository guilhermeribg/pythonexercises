segundosconver=input("Por favor, entre com o número de segundos que deseja converter: ")
totalseg=int(segundosconver)

dias=totalseg//86400
segrest=totalseg%86400
horas=segrest//3600
segrest2=segrest%3600
minutos=segrest2//60
segundos=segrest2%60

print(dias,"dias, ",horas,"horas, ",minutos,"minutos e ",segundos,"segundos.")
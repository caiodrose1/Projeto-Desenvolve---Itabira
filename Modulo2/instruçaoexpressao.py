#Q1

valor_hora = 20.0
horas_trabalhadas = 40

salario_bruto = valor_hora * horas_trabalhadas
inss = salario_bruto * 0.10
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (inss + sindicato)

print(f"Salário semanal bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (10%): R$ {inss:.2f}")
print(f"Desconto sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário semanal líquido: R$ {salario_liquido:.2f}")

#Q2

valor_hora = 20.0
horas_trabalhadas = 40

salario_bruto = valor_hora * horas_trabalhadas

salario_liquido = salario_bruto - (salario_bruto * 0.10 + salario_bruto * 0.05)

print(f"Salário semanal bruto: R$ {salario_bruto:.2f}")
print(f"Salário semanal líquido: R$ {salario_liquido:.2f}")


#Q3

valor_brl = 100.00
taxa_brl_por_cny = 0.69

valor_cny = valor_brl / taxa_brl_por_cny

print(f"Valor em BRL: R$ {valor_brl:.2f}")
print(f"Valor equivalente em CNY: ¥ {valor_cny:.2f}")

#Q4

distancia_km = 42.195
tempo_horas = 3

distancia_metros = distancia_km * 1000
tempo_segundos = tempo_horas * 3600

v_media = distancia_metros / tempo_segundos

print(f"Distância em metros: {distancia_metros:.1f} m")
print(f"Tempo em segundos: {tempo_segundos} s")
print(f"Velocidade média necessária: {v_media:.2f} m/s")
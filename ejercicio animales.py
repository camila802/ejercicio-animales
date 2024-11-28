def leche_por_semana(vacas, k_metros_por_vaca, litros_por_dia):
    """
    Calcula la producción de leche por semana en la granja.
    
    vacas: número de vacas
    k_metros_por_vaca: metros cuadrados requeridos por vaca
    litros_por_dia: litros de leche que produce una vaca por día
    """
    leche_total_dia = vacas * litros_por_dia
    leche_total_semana = leche_total_dia * 7  # 7 días en una semana
    return leche_total_semana

def huevos_por_mes(aves, gallinas_porcentaje=1/3):
    """
    Calcula la producción de huevos en un mes.
    
    aves: número total de aves
    gallinas_porcentaje: proporción de gallinas respecto al total de aves
    """
    gallinas = aves * gallinas_porcentaje  # 1/3 de las aves son gallinas
    mitad_gallinas = gallinas / 2  # mitad de las gallinas
    huevos_cada_3_dias = (mitad_gallinas * (30 / 3))  # días divididos por 3
    huevos_cada_5_dias = (mitad_gallinas * (30 / 5))  # días divididos por 5
    huevos_totales = huevos_cada_3_dias + huevos_cada_5_dias
    return int(huevos_totales)

# Ejemplo de uso:
# Datos para el subproblema 1
vacas = 10
k_metros_por_vaca = 20
litros_por_dia = 10

# Datos para el subproblema 2
aves = 90  # Total de aves en la granja

# Resultados
leche_semanal = leche_por_semana(vacas, k_metros_por_vaca, litros_por_dia)
huevos_mensuales = huevos_por_mes(aves)

print(f"Producción de leche semanal: {leche_semanal} litros")
print(f"Producción de huevos mensual: {huevos_mensuales} huevos")

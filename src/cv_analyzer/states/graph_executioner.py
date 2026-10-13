"""
Description:   Write a brief description of the script's purpose here.
Author:        David Jiménez Cooper - SpiderCoop
Date:          2026-10-12
"""

import time


def execute_graph(grafo, estado_inicial):
    print("🚀 Iniciando el análisis de alineación...")
    tiempo_inicio_total = time.perf_counter()
    tiempo_paso_anterior = tiempo_inicio_total

    estado_final = estado_inicial.copy()

    # .stream() emite un evento cada vez que un nodo termina su ejecución
    for evento in grafo.stream(estado_inicial):
        # 'evento' es un diccionario: {"nombre_del_nodo": {llaves_actualizadas}}
        for nombre_nodo, actualizaciones in evento.items():
            tiempo_actual = time.perf_counter()
            duracion_nodo = tiempo_actual - tiempo_paso_anterior

            print(f"✅ Nodo completado: [{nombre_nodo}]")
            print(f"⏱️  Tiempo tomado: {duracion_nodo:.2f} segundos")
            print(f"📊 Variables actualizadas: {list(actualizaciones.keys())}")
            print("-" * 40)

            # Actualizamos nuestras referencias
            tiempo_paso_anterior = tiempo_actual
            estado_final.update(actualizaciones)

    tiempo_total = time.perf_counter() - tiempo_inicio_total
    print(f"🎉 Proceso total finalizado en {tiempo_total:.2f} segundos.")

    return estado_final

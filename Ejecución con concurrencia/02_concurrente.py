import asyncio
import time

async def entrenar_en_gimnasio(usuario, maquina, series, retraso_inicial=0):
    if retraso_inicial > 0:
        await asyncio.sleep(retraso_inicial)  # Espera a que el primer usuario libere la máquina

    for serie in range(1, series + 1):
        print(f"[{usuario}] Entrenando en {maquina} (Serie {serie}/{series})...")
        await asyncio.sleep(1.0)  # Tiempo haciendo las repeticiones en la máquina

        if serie < series:
            print(f"[{usuario}] Tiempo muerto (descanso): deja libre {maquina} y usa la caminadora...")
            await asyncio.sleep(1.5)  # Mientras usa la caminadora, el otro usuario usa la máquina
        else:
            print(f"[{usuario}] Terminó todas sus series en {maquina} y la deja libre.")

async def main():
    print("GIMNASIO CONCURRENTE: ALTERNANDO MÁQUINA Y CAMINADORA EN TIEMPOS MUERTOS \n")
    inicio = time.perf_counter()

    # Ambos usuarios entrenan concurrentemente aprovechando el tiempo muerto entre series
    await asyncio.gather(
        entrenar_en_gimnasio("Yo (Usuario 1)", "Press de Banca", series=3, retraso_inicial=0),
        entrenar_en_gimnasio("Compañero (Usuario 2)", "Press de Banca", series=3, retraso_inicial=1.0)
    )

    fin = time.perf_counter()
    print(f"\nTiempo total de entrenamiento concurrente: {fin - inicio:.2f} segundos.")

if __name__ == "__main__":
    asyncio.run(main())

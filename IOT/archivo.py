import datetime

ubicacion = "mi_archivo.txt"

def interaccion(source, data_content):
    
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    # Formato del registro: [TIMESTAMP] [TIPO] [CHAT_ID] -> DATOS
    log_entry = f"[{timestamp}] [{source}] -> {data_content}\n"
    
    try:
        # Abre el archivo en modo 'a' (append) para añadir al final
        with open(ubicacion, 'a', encoding='utf-8') as f:
            f.write(log_entry)
            
    except Exception as e:
        # para un sistema mas robusto
        print(f"ERROR escribiendo el archivo txt: {e}")

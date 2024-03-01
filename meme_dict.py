import
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD" : "una cara riendo",
            "MELO" : "algo que esta bien",
            "PARCERO" : "amigo",
            }
            
palabra = input("¿Que palabar no entiendes")

if palabra in meme_dict:
    print(palabra+ ":" , meme_dict[palabra] )
else:
    print("no tengo el significado de esa palabra, pero te muestro otra:")
    clave = random.choice(meme_dict.keys() )
    print(clave+ ":", meme_dict[clave] )

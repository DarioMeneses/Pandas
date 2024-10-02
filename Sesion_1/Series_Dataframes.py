#Vamos a importar la biblioteca de pandas

import pandas as pd
psg_players = pd.Series(
    ["Navas", "Mbappe", "Neymar", "Messi"],
    #index=[1,7,10,30]
)
print(psg_players)
psg_dict = {1: "Navas", 7: "Mbappe", 10: "Neymar", 30: "Messi"}
psg_players_dict = pd.Series(psg_dict)
print(psg_players_dict)

# Diccionario con datos de jugadores
dict = {"Jugador": ["Navas", "Mbappe", "Neymar", "Messi"],
        "Altura": [183.0, 170.0, 170.0, 165.0],
        "Goles": [2, 200, 150, 200] }   


df = pd.DataFrame(dict, index=[1,7,10,30])
print(df)
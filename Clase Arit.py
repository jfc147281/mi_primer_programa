
apetece_helado_input = input("Te apatece un helado? (Si/No)").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Ingrese Si o No, al ingresar otro valor se tomara como no")
    apetece_helado = False


tiene_dinero_input = input("Tienes dinero para un helado (Si/No").upper()
esta_el_senor_helados_input = input("Esta el señor (Si/No)").upper()
esta_tu_tia_input = input("estas con tu tia (Si/No").upper()



apetece_helado = apetece_helado_input == "SI"
tiene_dinero = tiene_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puede_permitirselo = (tiene_dinero or esta_tu_tia) == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("comete un helado")
else:
    print("no comas")
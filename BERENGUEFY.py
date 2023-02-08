print("*Benvinguts a BERENGUIFY 2.0!")
print("----------MENU----------")
print("1.-Afegir una canco")
print("2.-Registrar un usuari")
print("3.-Veure cancons disponibles")
print("4.-Veure usuaris del sistema")
print("5.-Sortir del programa")
print("Tria una opcio de les anteriors:")
opcio=int(input()) #Elegir una opcio
if opcio == 1:
    print("------AFEGIR CANCO 1-------")
    nomCanco1=input("Introdueix canco: ")
    nomAutor1=input("Escriu autor canco: ")
    import re 
    url1=input("Introdueix URL de la canco:") #Introduir URL i comprovar si és el format correcte
    x = re.search("^https://.", url1) 
    if not (x):
     print("L'adreca no es correcta. Torna a intentar.")
     url1=input("Introdueix URL de la canco:")
     x = re.search("^https://.", url1)
     if not (x):
         print("L'adreca no es correcta.")
         quit()
    anyLlancament1=input("Escriu any llancament: ") #Escriure any de llançament i comprovar si el format és correcte.
    x = re.search("[0-9][0-9][0-9][0-9]", anyLlancament1) 
    if not (x):
     print("La data no es correcta. Torna a intentar.")
     anyLlancament1=input("Escriu any llancament: ")
     x = re.search("[0-9][0-9][0-9][0-9]", anyLlancament1) 
     if not (x):
         print("La data no es correcta.")
         quit() #Codi per sortir del programa si no és correcte la entrada.
    estilMusica1=input("Introdueix estil de musica: ")
    print("------AFEGIR CANCO 2-------")
    nomCanco2=input("Introdueix canco: ")
    nomAutor2=input("Escriu autor canco: ")
    import re 
    url2=input("Introdueix URL de la canco:")
    x = re.search("^https://.", url2) 
    if not (x):
     print("L'adreca no es correcta. Torna a intentar.")
     url2=input("Introdueix URL de la canco:")
     x = re.search("^https://.", url2) 
     if not (x):
         print("L'adreca no es correcta.")
         quit()
    anyLlancament2=input("Escriu any llancament: ")
    x = re.search("[0-9][0-9][0-9][0-9]", anyLlancament2) 
    if not (x):
     print("La data no es correcta. Torna a intentar.")
     anyLlancament2=input("Escriu any llancament: ")
     x = re.search("[0-9][0-9][0-9][0-9]", anyLlancament2) 
     if not (x):
         print("La data no es correcta.")
         quit()
    estilMusica2=input("Introdueix estil de musica: ")
elif opcio == 2:
      print("------REGISTRAR USUARI 1-------")
      nomComplet1=input("Introdueix el teu nom complet: ")
      import re 
      dataNaixement1=input("Introdueix la teva data de naixement: ") #Introduir data naixement en cormat dd/MM/aaaa i comprovar si esta escrit correctament amb el format.
      x = re.search("[0-9]{2}/[0-9]{2}/[0-9]{4}", dataNaixement1) 
      if not (x):
         print("La data no esta en un format correcte. Torna a intentar.")
         dataNaixement1=input("Introdueix la teva data de naixement: ")
         x = re.search("[0-9]{2}/[0-9]{2}/[0-9]{4}", dataNaixement1) 
         if not (x):
              print("La data no esta en un format correcte.")
              quit() #Sortir del programa
      correuElectronic1=input("Introdueix el teu correu electronic: ") #Comprovar si el correu electrònic està correctament escrit.
      x = re.search("[@]", correuElectronic1) 
      if not (x):
         print("No es un correu electronic. Torna a intentar.")
         correuElectronic1=input("Introdueix el teu correu electronic: ")
         x = re.search("[@]", correuElectronic1) 
         if not (x):
             print("No es un correu electronic.")
             quit()
      ciutat1=input("Introdueix la ciutat on vius: ")
      print("------REGISTRAR USUARI 2-------")
      nomComplet2=input("Introdueix el teu nom complet: ")
      dataNaixement2=input("Introdueix la teva data de naixement: ")
      x = re.search("[0-9]{2}/[0-9]{2}/[0-9]{4}", dataNaixement2) 
      if not (x):
         print("La data no esta en un format correcte. Torna a intentar.")
         dataNaixement2=input("Introdueix la teva data de naixement: ")
         x = re.search("[0-9]{2}/[0-9]{2}/[0-9]{4}", dataNaixement2) 
         if not (x):
             print("La data no esta en un format correcte.")
             quit( )
      correuElectronic2=input("Introdueix el teu correu electronic: ")
      x = re.search("\W", correuElectronic2) 
      if not (x):
         print("No es un correu electronic. Torna a intentar.")
         correuElectronic2=input("Introdueix el teu correu electronic: ")
      x = re.search("\W", correuElectronic2)
      if not (x):
         print("No es un correu electronic.")
         quit()
      ciutat2=input("Introdueix la ciutat on vius: ")
elif opcio == 3: #Esta opció no funciona en aquesta versió del codi ja que només podem registrar una opció, i per fer aquesta opció necessitam altre més
      print("------REGISTRE CANCO 1-------")
      print("Nom: "+nomCanco1)
      print("Autor: "+nomAutor1)
      print("URL de la canço: "+url1)
      print("Any llencament: "+anyLlancament1)
      print("Estil de musica: "+estilMusica1)
      print("------REGISTRE CANCO 2-------")
      print("Nom: "+nomCanco2)
      print("Autor: "+nomAutor2)
      print("URL de la canço: "+url2)
      print("Any llencament: "+anyLlencament2)
      print("Estil de musica: "+estilMusica2)
elif opcio == 4:  #Esta opció no funciona en aquesta versió del codi ja que només podem registrar una opció, i per fer aquesta opció necessitam altre més
      print("------REGISTRE USUARI 1-------")
      print("Usuari: "+nomComplet1)
      print("Data naixement: "+dataNaixement1)
      print("Correu electronic: "+correuElectronic1)
      print("Ciutat: "+ciutat1)
      print("------REGISTRE USUARI 2-------")
      print("Usuari: "+nomComplet2)
      print("Data naixement: "+dataNaixement2)
      print("Correu electronic: "+correuElectronic2)
      print("Ciutat: "+ciutat2)
elif opcio == 5:
      print("------SORTIR DEL PROGRAMA-------")
      print("Introdueix qualsevol lletra per sortir del programa")
      input()
archivo='mrtrix3.txt'


with open(archivo) as archivo:
 for linea in archivo:
  if 'abstract' in linea:   
   print(linea)



#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!
szam = int(input(' adjá számot: '))
szam1 = int(input('még 1-et teso: '))
if szam < szam1:
  print(szam,'<- ez a kisebb')

if szam > szam1:
  print(szam1, '-< ez a nagyobb a kettő közül.')
  
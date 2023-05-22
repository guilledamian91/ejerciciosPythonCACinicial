codigo="HGorLa*c?isarsq!"
palabraSecreta=""
for i in range(len(codigo)):
 if codigo[i] == "*":
  break
 if i%2 ==1:
  palabraSecreta = palabraSecreta + codigo[i] 
print(palabraSecreta)
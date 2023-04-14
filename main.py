def inverter(texto):
    return texto[::-1]

print(inverter("ODITREVNI OTXET"))

str = "ODITREVNI OTXET"
str_inversa = "" 
for i in range(len(str)-1, -1, -1): 
    str_inversa += str[i]
print(str_inversa)
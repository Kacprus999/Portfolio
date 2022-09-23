print("tekst1 :")
text1 = input()

print("tekst2 :")
text2 = input()

a = text1[0:2]
b = text2[0:2]

text1 = text1[2:len(text1)]
text1 = b + text1

text2 = text2[2:len(text2)]
text2 = a + text2


print("tekst1 : " + text1)
print("tekst2 : " + text2)


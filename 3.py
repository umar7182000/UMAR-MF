a = input()
if ( a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U' ):
  print("Vowel")
elif( a >= 'a' and a <= 'z' or a >= 'A' and a <= 'Z'):
  print("Consonant")
else:
  print("invalid")

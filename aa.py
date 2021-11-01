#1 Vanaf 30 terugtellen tot de raketlancering. Print elke tel en print de lancering.
#2 Print de uren van de dag. Voor de ochtend voeg je 'AM' toe. Voor de middag voeg je 'PM' toe
#3 Print alle even getallen tussen 20 en 50
#4 Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot aan de opgegeven dag.
#5 Herhaal een input() tot het resultaat daarvan gelijk is aan 'quit' Print het aantal iteraties per iteratie.
#6 Tel de cijfers vanaf 50 totdat hun gezamelijke som groter is dan 1000, print elk cijfer en de totale som per iteratie.

#1
# import time

# for i in range(30,0,-1):
#     time.sleep(1)
#     print(i)

#2
# for i in range(1,25,1):
#     am = 'AM'
#     pm = 'PM'
#     if i <12 :
#         print('{} {}'. format(i, am))
#     else:
#         print('{} {}'. format(i, pm))


#3
# for e in range(11,25,1):
#     print(e*2)

#4
# d = input("welke dag ")

# test_list = ['ma', 'di', 'wo', 'do', 'vr', 'za', 'zo']
  
# N = d

# temp = test_list. index(N)
# res = test_list[:temp]

# print(str(res))

  
#5
# inpt = input("chars: ")

# for karakter in inpt:
# 	print(karakter)

# begin = 50
# oth = []

#6
# for i in range(0,1001):
#     print(i)
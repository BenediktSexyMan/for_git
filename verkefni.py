#Forritun Git Verkefni
val = input("Hvað viltu gera?\n1: tvær tölur?\n2: Nöfn?\n3: Hástafir og Lágstafir?\n4: Hætta?\n")
while val != "4":
    if val == "1":
        num1 = int(input("Gefðu mér tvær heiltölur!\n"))
        num2 = int(input())
        print("Tölurnar lagðar saman eru:", num1 + num2, "\nTölurnar margfaldaðar saman eru:", num1 * num2)

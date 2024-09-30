import random

print("Välkommen till MMA! Följ anvisningarna för att spela!")

# Be spelarna ange sina namn
PlayerA = input("Spelare A, ange namn: ")
PlayerB = input("Spelare B, ange namn: ")

# Satsning
print("\nVem vill du satsa på?")
print(f"1: {PlayerA}")
print(f"2: {PlayerB}")

bet_player = input("Ange nummer på den spelare du vill satsa på: ")
bet_amount = int(input("Hur mycket vill du satsa? "))

hp_a = 100
hp_b = 100

# Första ronden
while hp_a > 0 and hp_b > 0:
    # Spelare A tappar slumpmässigt mellan 1 och 10 HP
    damage_to_a = random.randint(1, 10)
    hp_a -= damage_to_a
    print(f"{PlayerA} tappade {damage_to_a} HP och har nu: {hp_a}")

    if hp_a <= 50:
        break  # Om Spelare A har mindre än eller lika med 50 HP, avsluta ronden

    # Spelare B tappar slumpmässigt mellan 1 och 10 HP
    damage_to_b = random.randint(1, 10)
    hp_b -= damage_to_b
    print(f"{PlayerB} tappade {damage_to_b} HP och har nu: {hp_b}")

    if hp_b <= 50:
        break  # Om Spelare B har mindre än eller lika med 50 HP, avsluta ronden

# Fråga om de vill köra runda 2
print("Nästa runda börjar snart!")
svar_a = input(f"Är {PlayerA} redo för runda 2? (ja/nej): ")
svar_b = input(f"Är {PlayerB} redo för runda 2? (ja/nej): ")

if svar_a.lower() == "ja" and svar_b.lower() == "ja":
    while hp_a > 0 and hp_b > 0:
        # Spelare A tappar slumpmässigt mellan 1 och 10 HP
        damage_to_a = random.randint(1, 10)
        hp_a -= damage_to_a
        print(f"{PlayerA} tappade {damage_to_a} HP och har nu: {hp_a}")

        if hp_a <= 0:
            break  # Om Spelare A tappar all HP, avsluta

        # Spelare B tappar slumpmässigt mellan 1 och 10 HP
        damage_to_b = random.randint(1, 10)
        hp_b -= damage_to_b
        print(f"{PlayerB} tappade {damage_to_b} HP och har nu: {hp_b}")

        if hp_b <= 0:
            break  # Om Spelare B tappar all HP, avsluta

# Avgör vinnaren
winner = ""
if hp_a > 0:
    winner = PlayerA
    print(f"{PlayerA} är vinnaren!")
elif hp_b > 0:
    winner = PlayerB
    print(f"{PlayerB} är vinnaren!")
else:
    print("Det blev oavgjort!")

# Kontrollera satsningen
if winner == PlayerA and bet_player == "1":
    print(f"Grattis! Du satsade {2*bet_amount} på {PlayerA} och vann!")
elif winner == PlayerB and bet_player == "2":
    print(f"Grattis! Du satsade {2*bet_amount} på {PlayerB} och vann!")
else:
    print("Tyvärr, du förlorade din satsning.")

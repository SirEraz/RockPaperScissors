import math
import random
import time

playerHand = 0
cpuHand = 0

spacer = str("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

while True:
    print("Rock… Paper… Scissors…")
    print("1 - Rock \n2 - Paper\n3 - Scissors")
    print("Enter 1-3 to decide, or anything else to exit the game.")

    menu = int(input(" DECIDE: "))

    if menu == 1:
        playerHand = 1
        cpuHand = random.randint(1,3)
        if cpuHand == playerHand:
            print("________                      ._.")
            print("\______ \____________ __  _  _| |")
            print(" |    |  \_  __ \__  \\ \/ \/ / |")
            print(" |    `   \  | \// __ \\     / \|")
            print("/_______  /__|  (____  /\/\_/  __")
            print("        \/           \/        \/")
                  
            print("\nIt's a draw! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
        if cpuHand == 2:
            print("YOU: Rock")
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(2)
            print("\n...\n")
            print("CPU: Paper")
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(2)
            print("\n")
            print("You Lost! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
        if cpuHand == 3:
            print("YOU: Rock")
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(2)
            print("\n...\n")
            print("CPU: Scissors")
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(2)
            print("\n")
            print("You Win! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
    elif menu == 2:
        playerHand = 2
        cpuHand = random.randint(1,3)
        if cpuHand == playerHand:
            print("________                      ._.")
            print("\______ \____________ __  _  _| |")
            print(" |    |  \_  __ \__  \\ \/ \/ / |")
            print(" |    `   \  | \// __ \\     / \|")
            print("/_______  /__|  (____  /\/\_/  __")
            print("        \/           \/        \/")
            print("\nIt's a draw! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
        elif cpuHand == 1:
            print("YOU: Paper")
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(2)
            print("\n...\n")
            print("CPU: Rock")
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(2)
            print("\n")
            print("You Win! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
        elif cpuHand == 3:
            print("YOU: Paper")
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(2)
            print("\n...\n")
            print("CPU: Scissors")
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(2)
            print("\n")
            print("You Lost! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
    elif menu == 3:
        playerHand = 3
        cpuHand = random.randint(1,3)
        if cpuHand == playerHand:
            print("________                      ._.")
            print("\______ \____________ __  _  _| |")
            print(" |    |  \_  __ \__  \\ \/ \/ / |")
            print(" |    `   \  | \// __ \\     / \|")
            print("/_______  /__|  (____  /\/\_/  __")
            print("        \/           \/        \/")
            print("\nIt's a draw! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
        if cpuHand == 1:
            print("YOU: Scissors")
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(2)
            print("\n...\n")
            print("CPU: Rock")
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(2)
            print("\n")
            print("You Lost! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
        if cpuHand == 2:
            print("YOU: Scissors")
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(2)
            print("\n...\n")
            print("CPU: Paper")
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(2)
            print("\n")
            print("You Win! Press enter to play again.")
            enter = str(input(""))
            print(spacer)
    else:
        exit()



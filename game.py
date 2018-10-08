import sys
import rpg


def check_death(characters):
    # return true if every character in the list is dead
    for char in characters:
        if char.hp != 0:
            return False
    return True


# print python version & welcome message
print sys.version
print "-" * 20 + "\n\n\n"
print "Welcome to Endless Battles!"

# Game setup
player = rpg.Character("Link", 100)
foes = [rpg.Character("Undead Knight", 50), rpg.Character("Medusa", 35)]


# Game main loop
print "\n\n Battle has started!"
while not check_death(foes):
    index = 0
    while index < len(foes):
        print "{0}. {1} \t [{2} HP]".format(index+1, foes[index].name, foes[index].hp)
        index = index + 1
    choice = input("Attack enemy: ")
    foes[choice-1].get_hit(23)
    print "\n\n"
print "\n Victory Fare ~~~~"

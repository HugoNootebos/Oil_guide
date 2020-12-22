import numpy as np

class Player:
    def __init__(self, name, food = 0, wood = 0, steel = 0, nuclear = 0, oil = 0, troops = 0):
        self.name = name
        self.food = food
        self.wood = wood
        self.steel = steel
        self.nuclear = nuclear
        self.oil = oil
        self.troops = troops

print()
print("WELCOME TO THE OIL GUIDE APP")
print("insert [help] to view commands\n")
players = []
player_num = int(input("How many players? "))
for i in range(player_num):
    players += [Player(input("Player " + str(i + 1) + "'s name? "))]
print()
turn = 0
turn_num = 1
event_card = 0
default_player = Player("Mouse")


class Continent:
    def __init__(self, name, size, card_bonus = 1):
        self.name = name
        self.size = size
        self.card_bonus = card_bonus

continents = list()
continents.append(Continent("North-America", size = 9))
continents.append(Continent("South-America", size = 4, card_bonus = 0))
continents.append(Continent("Europe", size = 8))
continents.append(Continent("Africa", size = 6))
continents.append(Continent("Asia", size = 11, card_bonus = 2))
continents.append(Continent("Oceania", size = 4, card_bonus = 0))


class Country:
    def __init__(self, name, nuked_by = Player("none"), continent = Continent(name = "none", size = 43), food = 0, wood = 0, steel = 0, nuclear = 0, oil = 0, troops = 0, owner = default_player, radioactive = 0, developed = 0):
        self.name ="blank country"
        self.food = food
        self.wood = wood
        self.steel = steel
        self.nuclear = nuclear
        self.oil = oil
        self.troops = troops
        self.owner = owner
        self.radioactive = radioactive
        self.developed = developed
        self.nuked_by = nuked_by
        self.continent = continent

countries = [i for i in range(42)]
countries[0] = Country("Redneck", continent = continents[0], troops = 3)
countries[1] = Country("Madagaskar", continent = continents[3], food = 1, troops = 1, wood = 2)
countries[2] = Country ("Zuid-Afrika", continent = continents[3], food = 1, troops = 2)
countries[3] = Country("Belgisch Congo", continent = continents[3], troops = 3, steel = 1)
countries[4] = Country("Somalië", continent = continents[3], troops = 3, wood = 1)
countries[5] = Country("Nigeria", continent = continents[3], troops = 3, wood = 1)
countries[6] = Country("Sahara", continent = continents[3], troops = 2, oil = 1, nuclear = 1)
countries[7] = Country("IJsland", continent = continents[2], troops = 1, wood = 2, oil = 1)
countries[8] = Country("Viking", continent = continents[2], food = 2, wood = 1, oil = 1)
countries[9] = Country("Sovjet-Rusland", continent = continents[2], troops = 3, wood = 1, oil = 1)
countries[10] = Country("Belarus", continent = continents[2], food = 4, wood = 1)
countries[11] = Country("Nazi-Duitsland", continent = continents[2], food = 1, troops = 1, steel = 2)
countries[12] = Country("Romeinse Rijk", continent = continents[2], food = 4)
countries[13] = Country("Spanje", continent = continents[2], food = 2, troops = 1)
countries[14] = Country("Londen", continent = continents[2], food = 2, wood = 1)
countries[15] = Country("Siberië", continent = continents[4], food = 1, steel = 1, oil = 1)
countries[16] = Country("Kazachstan", continent = continents[4], food = 1, troops = 1, oil = 1, nuclear = 1)
countries[17] = Country("China", continent = continents[4], food = 8)
countries[18] = Country("Mongolië", continent = continents[4], food = 1, troops = 1, steel = 1)
countries[19] = Country("Noord-Korea", continent = continents[4], troops = 2)
countries[20] = Country("Maleisië", continent = continents[4], food = 1, wood = 2)
countries[21] = Country("Sri Lanka", continent = continents[4], food = 1, troops = 1, wood = 2)
countries[22] = Country("India", continent = continents[4], food = 1, troops = 1, wood = 1)
countries[23] = Country("Ottomaanse Rijk", continent = continents[4], food = 2, troops = 1, oil = 1)
countries[24] = Country("Arabië", continent = continents[4], oil = 5)
countries[25] = Country("Japan", continent = continents[4], food = 1, wood = 1, steel = 1)
countries[26] = Country("Nederlands-Indië", continent = continents[5], food = 1, wood = 2, steel = 1)
countries[27] = Country("Outback", continent = continents[5], food = 1, steel = 3, nuclear = 1)
countries[28] = Country("Gold Coast", continent = continents[5], food = 1, troops = 1, steel = 2)
countries[29] = Country("Filipijnen", continent = continents[5], food = 1, troops = 1, wood = 1, steel = 1)
countries[30] = Country("Argentinië", continent = continents[1], food = 1, steel = 2)
countries[31] = Country("Venezuela", continent = continents[1], troops = 1, steel = 3, nuclear = 1)
countries[32] = Country("Brazilië", continent = continents[1], steel = 1, wood = 3)
countries[33] = Country("Peru", continent = continents[1], steel = 3, food = 1, troops = 1)
countries[34] = Country("Alaska", continent = continents[0], food = 1, troops = 1, steel = 1, oil = 1)
countries[35] = Country("New York", continent = continents[0], food = 4)
countries[36] = Country("Los Angeles", continent = continents[0], food = 2, troops = 1, wood = 1)
countries[37] = Country("Canada", continent = continents[0], wood = 2, oil = 1, nuclear = 1)
countries[38] = Country("Mexico", continent = continents[0], food = 1, troops = 1, wood = 1)
countries[39] = Country("Groenland", continent = continents[0], food = 2, oil = 1)
countries[40] = Country("Cuba", continent = continents[0], food = 2, troops = 1, wood = 1)
countries[41] = Country("Pearl Harbor", continent = continents[0], troops = 2)

country_names = []
for i in range(len(countries)):
    country_names += [countries[i].name]


def guess_country(inp):
    out = Country("none")
    matches = []
    for i in range(len(country_names)):
        if np.char.lower(inp) == np.char.lower(country_names[i][:len(inp)]):
            matches += [countries[i]]
    if len(matches) == 1:
        out = matches[0]
    elif len(matches) > 1:
        for i in range(len(matches)):
            if input(matches[i].name + "?: ") in ["j", "J", "ja", "Ja", "y", "Y", "yes", "Yes"]:
                out = matches[i]
                break
    return out

def show_stats(turn):
    players[turn].food = 0
    players[turn].wood = 0
    players[turn].steel = 0
    players[turn].oil = 0
    players[turn].nuclear = 0
    players[turn].troops = 0
    for i in range(len(countries)):
        if countries[i].owner == players[turn] and countries[i].radioactive == 0:
            n = 1
            if countries[i].developed == 2:
                n = 2
            elif countries[i].developed == 1:
                n = 0
            players[turn].food += n*countries[i].food
            players[turn].wood += n*countries[i].wood
            players[turn].steel += n*countries[i].steel
            players[turn].oil += n*countries[i].oil
            players[turn].nuclear += n*countries[i].nuclear
            players[turn].troops += countries[i].troops
    print(players[turn].name, "'s resources per round:")
    print(" food:    " + str(players[turn].food))
    print(" wood:    " + str(players[turn].wood))
    print(" steel:   " + str(players[turn].steel))
    print(" oil:     " + str(players[turn].oil))
    print(" uranium: " + str(players[turn].nuclear))
    print(" troops:  " + str(3 + int(players[turn].troops/3)))

def nuke():
    nuked_country = guess_country(input("Which country is nuked? "))
    for i in range(len(countries)):
        if countries[i] == nuked_country:
            countries[i].radioactive += 3
            countries[i].nuked_by = players[turn]
            print(" " + countries[i].name + "'s radioactivity is now 3")
            break

def check_for_continents(turn):
    lst = []  #list of each of owner's country's continent affiliation
    continent_lst = []
    for i in range(len(countries)):
        if countries[i].owner == players[turn]:
            lst += [countries[i].continent]
    for i in range(len(continents)):
        if continents[i].size == lst.count(continents[i]):
            continent_lst += [continents[i]]
    return continent_lst

show_stats(turn)

running = True
delayed_develop = False

while running:
    inp = input()
    if inp == "":
        turn = (turn + 1) % player_num
        turn_num += 1
        event_card += 1
        print(players[turn].name + " starts TURN " + str(turn_num) + ")")
        if event_card == player_num + 1:
            print(" Draw an event card")
            event_card = 0
        players_continents = check_for_continents(turn)
        if players_continents != []:
            card_bonus = 0
            continent_names = ""
            for i in range(len(players_continents)):
                card_bonus += players_continents[i].card_bonus
                continent_names += players_continents[i].name
                if i != len(players_continents) - 1:
                    continent_names += " and "
            print(" " + players[turn].name + " gets " + str(card_bonus) + " cards for controlling " + continent_names)
        for i in range(len(countries)):
            if countries[i].developed == 1 and countries[i].owner == players[turn]:
                if countries[i].continent in players_continents:
                    countries[i].developed = 2
                    print(" " + countries[i].name + " is now developed (instant production)")
                else:
                    delayed_develop = True
                    delayed_develop_country = countries[i]
                    print(" " + countries[i].name + " is now developed (no production)")
            if countries[i].radioactive > 0 and countries[i].nuked_by == players[turn]:
                countries[i].radioactive -= 1
                print(" " + countries[i].name + "'s radioactivity is now " + str(countries[i].radioactive))
        show_stats(turn)
        if delayed_develop:
            delayed_develop_country.developed = 2
            delayed_develop = False
    elif inp == "nuke":
        nuke()
    elif inp == "develop" or inp == "build":
        country = guess_country(input("Which country is being developed? "))
        print(" " + players[turn].name + " starts developing " + country.name)
        country.developed = 1
    elif inp == "lose" or inp == "lost":
        country_lost = guess_country(input("Which country was lost? "))
        print(" " + players[turn].name + " lost " + country_lost.name)
        country_lost.owner = default_player
    elif inp == "countries":
        for i in range(len(countries)):
            if countries[i].owner == players[turn]:
                print(" " + countries[i].name)
        print()
    elif inp == "elimination":
        eliminated_player = input("Who has been eliminated? ")
        for i in range(player_num):
            if eliminated_player.lower() == players[i].name.lower():
                players.remove(players[i])
                player_num -= 1
                print(" " + eliminated_player + " was eliminated\n")
                if player_num == 1:
                    print(players[0].name + " WINS!")
                    running = False
                break
    elif inp == "show":
        show_stats(turn)
    elif inp == "q":
        running = False
    elif inp == "help":
        print("commands:")
        print(" [] to end turn")
        print(" [country name] to conquer a country")
        print(" [lose] to lose a country")
        print(" [countries]")
        print(" [develop]")
        print(" [nuke]")
        print(" [show]")
        print(" [elimination] to remove another player")
        print(" [q] to quit\n")
    else:
        country = guess_country(inp)
        if country in countries and country.owner != players[turn]:
            country.owner = players[turn]
            print(" " + players[turn].name + " takes " + country.name + "\n")
        elif country in countries:
            print(" " + players[turn].name + " already owns " + country.name)
        else:
            print(" This is not a country")

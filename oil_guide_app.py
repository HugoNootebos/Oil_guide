import numpy as np
from random import randint

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
        self.name = name
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

if player_num == 3:
    starting_countries = [countries[8], countries[41], countries[21]]
for i in range(player_num):
    players += [Player(input("Player " + str(i + 1) + "'s name? "))]
print()

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
    country_num = 0
    players[turn].food = 0
    players[turn].wood = 0
    players[turn].steel = 0
    players[turn].oil = 0
    players[turn].nuclear = 0
    players[turn].troops = 0
    for i in range(len(countries)):
        if countries[i].owner == players[turn] and countries[i].radioactive == 0:
            n = 1
            country_num += 1
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
    print(" countries: " + str(country_num))
    cont_lst = check_for_continents(turn)
    cont_str = ""
    if len(cont_lst) != 0:
        for i in range(len(cont_lst)):
            cont_str += cont_lst[i].name + ", "
        print(" continents: " + cont_str[0:-2])
    print(" " + players[turn].name + "'s resources per round:")
    print("  food:    " + str(players[turn].food))
    print("  wood:    " + str(players[turn].wood))
    print("  steel:   " + str(players[turn].steel))
    print("  oil:     " + str(players[turn].oil))
    print("  uranium: " + str(players[turn].nuclear))
    print("  troops:  " + str(3 + int(players[turn].troops/3)))

def nuke():
    nuked_country = guess_country(input("Which country is nuked? "))
    nuked_country.radioactive += 3
    nuked_country.nuked_by = players[turn]
    print(" " + nuked_country.name + "'s radioactivity is now " + str(nuked_country.radioactive))

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
develop_country = countries[0]

while running:
    inp = input()
    try:
        if inp == "":
            turn = (turn + 1) % player_num
            turn_num += 1
            event_card += 1
            print(players[turn].name + " starts TURN " + str(turn_num))
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
            develop_country = guess_country(input("Which country is being developed? "))
            print(" " + players[turn].name + " starts developing " + develop_country.name)
            develop_country.developed = 1
        elif inp == "undevelop":
            undevelop_country = guess_country(input("Which country is being undeveloped? "))
            if undevelop_country.owner == players[turn]:
                print(" " + undevelop_country.name + " is now undeveloped ")
                undevelop_country.developed = 0
        elif inp == "lose" or inp == "lost":
            country_lost = guess_country(input("Which country was lost? "))
            print(" " + players[turn].name + " lost " + country_lost.name)
            country_lost.owner = default_player
        elif inp == "lose many":
            print(" insert [exit] to exit loop")
            while True:
                country_lost_guess = input("Which country was lost? ")
                if country_lost_guess in ["q", "exit", "quit"]:
                    break
                country_lost = guess_country(country_lost_guess)
                print(" " + players[turn].name + " lost " + country_lost.name)
                country_lost.owner = default_player
        elif inp == "reset":
            for i in range(len(countries)):
                if countries[i].owner == players[turn]:
                    countries[i].owner = default_player
            print(players[turn].name + "'s countries have been reset")
        elif inp in ["undo", "l"]:
            country.owner = default_player
            print(" " + players[turn].name + " lost " + country.name)
        elif inp == "countries":
            for i in range(len(countries)):
                if countries[i].owner == players[turn]:
                    print(" " + countries[i].name + "+"*countries[i].developed)
            print()
        elif inp == "produce":
            for i in range(len(countries)):
                if countries[i].owner == players[turn]:
                    print(" " + countries[i].name + ": food: " + str(countries[i].food) + ", wood: " + str(countries[i].wood) + ", steel: " + str(countries[i].steel) + ", uranium: " + str(countries[i].nuclear) + ", oil: " + str(countries[i].oil) + ", helmets: " + str(countries[i].troops) + ", developed: " + str(countries[i].developed in [1,2] + " (" + countries[i].developed + ")"))
        elif inp in ["elimination", "eliminate", "eliminated"]:
            eliminated_player = input(" Who has been eliminated? ")
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
        elif inp == "shop":
            print(" Anytime")
            print("  bridge: 10 wood")
            print("  rails:  2  wood + 1 steel")
            print("  nuke:   5  uranium")
            print(" Reinforcement Phase")
            print("  boat:   15 wood")
            print("  plane:  10 steel")
            print("  tank:   20 steel")
            print("  fort:   10/15/20 wood")
        elif inp == "cards" or inp == "card":
            print(" troops:  x  1")
            print(" food:    x 2.5")
            print(" wood:    x  3")
            print(" steel:   x  2")
            print(" oil:     x  2")
            print(" uranium: x 1.5")
        elif inp in ["event card", "event timer"]:
            print(str(player_num - event_card + 1) + " more turns until an event card is drawn")
        elif inp == "show development":
            for i in range(len(countries)):
                print(countries[i].name + ": " + countries[i].developed)
        elif inp == "q":
            running = False
        elif inp == "help":
            print("commands:")
            print(" [] to end turn")
            print(" [country name] to conquer a country")
            print(" [lose] to lose a country")
            print(" [lose many] to lose multiple countries")
            print(" [gain many] to gain multiple countries")
            print(" [reset] to lose all countries")
            print(" [undo] to lose a country that was just obtained")
            print(" [countries] to see current player's countries")
            print(" [produce] to see what each country produces")
            print(" [show] to see current player's resource production")
            print(" [develop] to start developing a country (x2 production)")
            print(" [undevelop] to undevelop a country")
            print(" [nuke] to indicate a country has been nuked")
            print(" [cards] to see card conversion factors")
            print(" [event card] to see turns until new event card is drawn")
            print(" [shop] to see shop")
            print(" [eliminate] to remove a player")
            print(" [show development]")
            print(" [q] to quit") 
        else:
            country = guess_country(inp)
            if country in countries and country.owner != players[turn]:
                country.owner = players[turn]
                print(" " + players[turn].name + " takes " + country.name)
            elif country.name == "none":
                print(" this is not a country or command. Insert [help] for commands")
            else:
                print(" " + players[turn].name + " already owns " + country.name)
    except:
        pass


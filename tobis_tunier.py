from glob import glob
import random
from statistics import mode
import sys
def ko(dataarray, name):
    #winnerlist = []
    playeramount = int(dataarray.pop(0))
    playerlist = dataarray
    if playeramount % 2 == 1:
        print("Deine Spielerzahl ist leider ungerade somit geht das KO System nicht auf")
        ask = input("Es wird nun ein Spieler zufällig disqualifiziert\n Falls du das nicht willst schreibe (n) \nIn dem Fall wenn du n eingibst musst du entweder vor dem Neustart deine Spieleranzahl in eine gerade Zahl umwandeln oder das Liga System verwenden.")
        if ask == "n" or ask == "N":
            sys.exit(0)
        else:
            rdmn = random.randint(0,playeramount-1)
            playerlist.pop(rdmn)
            playeramount = playeramount - 1

    loop = True
    print(playerlist[0])
    while loop:
        try:
            tournament_schedule = int(input("Welchen Tunierplan möchtest du benutzen durchnumerriert nach der Ordnung der Textdatei(1), zufällig (2), manuell (3)"))
        except ValueError:
            print("Dein Input leider keine ganze Zahl")
        if tournament_schedule == 1:
            loop = False
            round1plan = {}
            playeramount_half = int(playeramount / 2)
            for i in range (1, playeramount_half + 1):
                print(i)
                if i ==1:
                    round1plan["group{0}".format(i)] = 0, 1
                else:
                    x = i-1
                    x = x *2
                    round1plan["group{0}".format(i)] = x, x+1
            print(round1plan)

            print("Der Turierplan wird nach der Ordnung der Textdatei erstellt")
        elif tournament_schedule == 2:
            loop = False
            round1plan = {}
            playeramount_half = int(playeramount / 2)
            check = []
            player_order = []
            for i in range (0,playeramount-1):
                check.append(i)
            print(check)
            while len(check) != 0:
                random_number = random.randint(0,playeramount-1)
                try:
                    check.remove(random_number)
                except:
                    continue
                player_order.append(random_number)
            print(player_order)
            for i in range (0,playeramount_half):
                x = i-1
                x = x *2
                round1plan["group{0}".format(i+1)] = player_order[x], player_order[x+1]
            print("Der Turnierplan wurde zufällig erstellt")
            print(round1plan)

        elif tournament_schedule == 3:
            loop = False
            round1plan = {}
            playeramount_half = int(playeramount / 2)
            check = []
            print(playeramount_half)
            for i in range (0, playeramount_half):
                checker = True
                while checker:
                    checker = False
                    i_plus = i+1
                    try:
                        player1 = int(input("Erster Spieler der Gruppe" + str(i_plus) + "\n:"))
                    except ValueError:
                        print("Deine Eingabe ist leider keine Ganze Zahl vom Typ (Integer)")
                        checker = True
                        continue
                    try:
                        player2 = int(input("Zweiter Spieler der Gruppe" + str(i_plus) + "\n:"))
                    except ValueError:
                        print("Deine Eingabe ist leider keine Ganze Zahl vom Typ (Integer)")
                        checker = True
                        continue
                    for x in check:
                        print("Check wird durchgeführt")
                        if x == player1:
                            print("Du hast leider Spieler", player1, " schon zugewiesen\nBitte wähle einen anderen Spieler für den ersten Spieler der Gruppe" + str(i_plus))
                            checker = True
                            continue
                        if x == player2:
                            print("Du hast leider Spieler", player2, " schon zugewiesen\nBitte wähle einen anderen Spieler für den ersten Spieler der Gruppe" + str(i_plus))
                            checker = True
                            continue
                check.append(player1)
                check.append(player2)
                round1plan["group{0}".format(i+1)] = player1 - 1, player2 - 1
                print(check)
            print(round1plan)

        else:
            print("Bitte gebe einen zahl zwischen 1 und 3 ein")
    for _ in range(1):
        round3plan = {}
        round3list = []
        playeramount_loop = playeramount_half
        print(playeramount_loop)
        round2plan = round1plan
        print(round2plan)
        while playeramount_loop / 2 >= 1 or playeramount_loop == 1:
            if playeramount_loop == 1:
                print("Finale Runde")
                print(round2plan)
                players = round2plan["group"+str(1)]
                playerone = players[0]
                playertwo = players[1]
                playerone_power = int(playerlist[playerone])
                playertwo_power = int(playerlist[playertwo])
                random_number = random.randint(1, playerone_power + playertwo_power)
                print(random_number)
                if 0 <= random_number <= playerone_power:
                    print("Spieler " + str(playerone) + " hat gewonnen mit einer Power von " + str(playerone_power))
                    #winnerlist.append(playerone)
                else:
                    print("Spieler " + str(playertwo) + " hat gewonnen mit einer Power von " + str(playertwo_power))
                    #winnerlist.append(playertwo)
                break
            for i in range(1, playeramount_loop + 1):
                players = round2plan["group"+str(i)]
                print(players)
                playerone = players[0]
                playertwo = players[1]
                playerone_power = int(playerlist[playerone])
                playertwo_power = int(playerlist[playertwo])
                random_number = random.randint(1, playerone_power + playertwo_power)
                if 0 <= random_number <= playerone_power:
                    print("Spieler 1 hat gewonnen")
                    round3list.append(playerone)
                else:
                    print("Spieler 2 hat gewonnen")
                    round3list.append(playertwo)
                print(playerone)
                print(playerone_power)
                print(playertwo)
                print(playertwo_power)
            print("liste",round3list)
            xy = int(playeramount_loop / 2)
            #xy = xy + 1
            for x in range (1,xy + 1):
                if x == 1:
                    round3plan["group{0}".format(x)] = round3list[0], round3list[1]
                else:
                    y = x - 1
                    y = y * 2
                    round3plan["group{0}".format(x)] = round3list[y], round3list[y+1]
            round3list = []
            print(round3plan)
            round2plan = round3plan
            round3plan = {}
            playeramount_loop = int(playeramount_loop / 2)
            print(playeramount_loop)
    #winner_end = mode(winnerlist)
    #winner = playerlist[int(winner_end)]
    #print(winner_end)
    #print(name)
    #print("Spieler" + str(winner_end) + "hat im Durschnitt am häufigsten gewonnen mit einer Stärke von " , winner , "\n")
    #print(playerlist)
    
def liga(dataarray,name):
    winnerlist = []
    playeramount = int(dataarray.pop(0))
    for _ in range(1):
        print("\n" + "Starte Liga mit der Datei " + name)
        playerlist = dataarray
        print(playeramount)
        print(playerlist)
        wins = playeramount * [0]
        print(wins)
        print(wins)
        for i in range (0,playeramount-1):
            print("\n")
            print("spieler" + str(i))
            print(playerlist[i])
            print("\n")
            powerplayeri = int(playerlist[i])
            for x in range (i+1,playeramount):
                print("spieler" + str(x))
                print(playerlist[x])
                powerplayerx = int(playerlist[x])
                random_number = random.randint(0, powerplayeri + powerplayerx)
                print("Zufallszahl"+ str(random_number))
                if 0 <= random_number <= powerplayeri:
                    print("Spieler" + str(i) + "hat gewonnen")
                    win = wins[i]
                    win = win + 1
                    wins[i] = win
                else:
                    print("Spieler" + str(x) + "hat gewonnen")
                    win = wins[x]
                    win = win + 1
                    wins[x] = win
        print("Die Ergebnisse stehen fest ", wins)
        max = wins[0]
        print("Länge siege", len(wins))
        print("Array wins ",wins)
        for i in range(0,len(wins)):
            if(wins[i] > max):
                max = wins[i]
        print("Die größte Anzahl an Siegen ist ", max)
        #testen ob es mehrere Gewinner gibt
        winner_arr_power = []
        winner_arr_index = []
        for i in range(0,len(wins)):
            if wins[i] == max:
                winner_arr_index.append(i)
        for i in winner_arr_index:
            winner_arr_power.append(playerlist[i])
        print(winner_arr_index)
        print(winner_arr_power)
        length_winner_power = len(winner_arr_power)
        if length_winner_power > 1:
            print("Es gibt mehrere Gewinner und zwar ", length_winner_power)
            ask = str(input("Was möchtest du machen? Soll es mehrere Gewinner geben dann skipe mit (skip)\nOder möchtest du ein KO zwischen den Spielern mit den meisten siegen (ko)\n:"))
            if ask == "skip":
                for i in range(0,length_winner_power):
                    print("Spieler" + str(winner_arr_index[i]) + " hat gewonnen mit einer Angriffstärke von " + str(winner_arr_power[i]))
            elif ask == "ko":
                print("Das KO System wird aufgerufen......")
                if length_winner_power % 2 == 1:
                    print("Die Anzahl an Spielern ist ungrade wir müssen leider einen disqualifizieren")
                    print("Dies wird zufällig entschieden")
                    rdmn = random.randint(0, length_winner_power - 1)
                    winner_arr_power.pop(rdmn)
                param = "Finale"
                players = len(winner_arr_power)
                for i in range (0, len(winner_arr_index)):
                    print("Spieler" + str(winner_arr_index[i]) + " wird als Spieler" + str(i) + " antreten.")

                winner_arr_power.insert(0,players)
                ko(winner_arr_power, param)
            else:
                print("Ungültige Eingabe gebe bitte (skip) oder (ko) ein")


        else:
            index = wins.index(max)
            print("Der Index ist", index)
            winner = playerlist[index]
            print("Spieler" + str(index) + " hat gewonnen mit einer Angriffstärke von " + winner)
            #winnerlist.append(str(index))
    #winner_end = mode(winnerlist)
    #winner = playerlist[int(winner_end)]
    #print(winner_end)
   # print(name)
  #  print("Spieler" + str(winner_end) + "hat im Durschnitt am häufigsten gewonnen mit einer Stärke von " , winner , "\n")
   # print(playerlist)

def read_from_file(filename):
    file1 = open(filename, "r").read().split('\n')
    filearray = []

    for i in file1:
        filearray.append(i)
    return filearray


def ko5(dataarray, name, skip):
    winnerlist = []
    playeramount = int(dataarray.pop(0))
    playerlist = dataarray
    if playeramount % 2 == 1:
        print("Deine Spielerzahl ist leider ungerade somit geht das KO System nicht auf")
        ask = input("Es wird nun ein Spieler zufällig disqualifiziert\n Falls du das nicht willst schreibe (n) \nIn dem Fall wenn du n eingibst musst du entweder vor dem Neustart deine Spieleranzahl in eine gerade Zahl umwandeln oder das Liga System verwenden.")
        if ask == "n" or ask == "N":
            sys.exit(0)
        else:
            rdmn = random.randint(0,playeramount-1)
            playerlist.pop(rdmn)
            playeramount = playeramount - 1
    loop = True
    print(playerlist[0])
    while loop:
        if skip == False:
            try:
                tournament_schedule = int(input("Welchen Tunierplan möchtest du benutzen durchnumerriert nach der Ordnung der Textdatei(1), zufällig (2), manueller Plan (3)"))
            except ValueError:
                print("Dein Input leider keine ganze Zahl")
        else:
            tournament_schedule = 1
        if tournament_schedule == 1:
            loop = False
            round1plan = {}
            playeramount_half = int(playeramount / 2)
            for i in range (1, playeramount_half + 1):
                print(i)
                if i ==1:
                    round1plan["group{0}".format(i)] = 0, 1
                else:
                    x = i-1
                    x = x *2
                    round1plan["group{0}".format(i)] = x, x+1
            print(round1plan)

            print("Der Turierplan wird nach der Ordnung der Textdatei erstellt")
        elif tournament_schedule == 2:
            loop = False
            round1plan = {}
            playeramount_half = int(playeramount / 2)
            check = []
            player_order = []
            for i in range (0,playeramount-1):
                check.append(i)
            print(check)
            while len(check) != 0:
                random_number = random.randint(0,playeramount-1)
                try:
                    check.remove(random_number)
                except:
                    continue
                player_order.append(random_number)
            print(player_order)
            for i in range (0,playeramount_half):
                x = i-1
                x = x *2
                round1plan["group{0}".format(i+1)] = player_order[x], player_order[x+1]
            print("Der Turnierplan wurde zufällig erstellt")
            print(round1plan)


        elif tournament_schedule == 3:
            loop = False
            round1plan = {}
            playeramount_half = int(playeramount / 2)
            check = []
            print(playeramount_half)
            for i in range (0, playeramount_half):
                checker = True
                while checker:
                    checker = False
                    i_plus = i+1
                    try:
                        player1 = int(input("Erster Spieler der Gruppe" + str(i_plus) + "\n:"))
                    except ValueError:
                        print("Deine Eingabe ist leider keine Ganze Zahl vom Typ (Integer)")
                        checker = True
                        continue
                    try:
                        player2 = int(input("Zweiter Spieler der Gruppe" + str(i_plus) + "\n:"))
                    except ValueError:
                        print("Deine Eingabe ist leider keine Ganze Zahl vom Typ (Integer)")
                        checker = True
                        continue
                    for x in check:
                        print("Check wird durchgeführt")
                        if x == player1:
                            print("Du hast leider Spieler", player1, " schon zugewiesen\nBitte wähle einen anderen Spieler für den ersten Spieler der Gruppe" + str(i_plus))
                            checker = True
                            continue
                        if x == player2:
                            print("Du hast leider Spieler", player2, " schon zugewiesen\nBitte wähle einen anderen Spieler für den ersten Spieler der Gruppe" + str(i_plus))
                            checker = True
                            continue
                check.append(player1)
                check.append(player2)
                round1plan["group{0}".format(i+1)] = player1 - 1, player2 - 1
                print(check)
            print(round1plan)

        else:
            print("Bitte gebe einen zahl zwischen 1 und 3 ein")
    for _ in range(1):
        round3plan = {}
        round3list = []
        playeramount_loop = playeramount_half
        round2plan = round1plan
        print("first plan",round2plan)
        print(round2plan)
        while playeramount_loop / 2 >= 1 or playeramount_loop == 1:
            if playeramount_loop == 1:
                print("Finale Runde")
                players = round2plan["group"+str(1)]
                print(players)
                playerone = players[0]
                playertwo = players[1]
                playerone_power = int(playerlist[playerone])
                playertwo_power = int(playerlist[playertwo])
                playerone_wins = 0
                playertwo_wins = 0
                for _ in range(0,5):
                    random_number = random.randint(1, playerone_power + playertwo_power)
                    if 0 <= random_number <= playerone_power:
                        print("Spieler 1 hat gewonnen")
                        playerone_wins = playerone_wins + 1
                    else:
                        print("Spieler 2 hat gewonnen")
                        playertwo_wins = playertwo_wins + 1

                print(playerone_wins, "Spieler 1 Siege")
                print(playertwo_wins, "Spieler 2 Siege")
                if playerone_wins > playertwo_wins:
                    print("Spieler " + str(playerone) + " hat gewonnen mit einer Power von " + str(playerone_power))
                    round3list.append(playerone)
                else:
                    print("Spieler " + str(playertwo) + " hat gewonnen mit einer Power von " + str(playertwo_power))
                    round3list.append(playertwo)
                break
            for i in range(1, playeramount_loop + 1):
                players = round2plan["group"+str(i)]
                print(players)
                playerone = players[0]
                playertwo = players[1]
                playerone_power = int(playerlist[playerone])
                playertwo_power = int(playerlist[playertwo])
                checkw = True
                while checkw:
                    playerone_wins = 0
                    playertwo_wins = 0
                    for _ in range(0,4):
                        checkw = False
                        random_number = random.randint(1, playerone_power + playertwo_power)
                        if 0 <= random_number <= playerone_power:
                            print("Spieler 1 hat gewonnen")
                            playerone_wins = playerone_wins + 1
                            winnerlist.append(playerone)
                        else:
                            print("Spieler 2 hat gewonnen")
                            playertwo_wins = playertwo_wins + 1
                            winnerlist.append(playertwo)
                    if playerone_wins == playertwo_wins:
                        print("Es wird nochmal gekämpft gleichstand")
                        checkw = True
                if playerone_wins > playertwo_wins:
                    print("Spieler 1 hat die meisten Runden gewonnen : " + str(playerone_wins) + "Runden")
                    round3list.append(playerone)
                else:
                    print("Spieler 2 hat die meisten Runden gewonnen : " + str(playertwo_wins) + "Runden")
                    round3list.append(playertwo)
                print(playerone)
                print(playerone_power)
                print(playertwo)
                print(playertwo_power)
            print(round3list)
            xy = int(playeramount_loop / 2)
            for x in range (1,xy + 1):
                if x == 1:
                    round3plan["group{0}".format(x)] = round3list[0], round3list[1]
                else:
                    y = x - 1
                    y = y * 2
                    round3plan["group{0}".format(x)] = round3list[y], round3list[y+1]
            print(round3plan)
            round2plan = round3plan
            round3list = []
            round3plan = {}
            playeramount_loop = int(playeramount_loop / 2)
            print(playeramount_loop)
    #winner_end = mode(winnerlist)
   # winner = playerlist[int(winner_end)]
   # print(winner_end)
  #  print(name)
   # print("Spieler" + str(winner_end) + "hat im Durschnitt am häufigsten gewonnen mit einer Stärke von " , winner , "\n")
  #  print(playerlist)
    
if __name__ == '__main__':
    dirlist = glob('*.txt')
    amount_txt = len(dirlist)
    print(amount_txt, "Textdateien wurden erfolgreich eingelesen.")

    datadic = {}
    for i in range (0,amount_txt):
        datadic["file{0}".format(i)] = read_from_file(dirlist[i-1])

    print(datadic)
    print("\n")
    loop = True
    loop2 = False
    skip = False
    while loop == True:
        try:
            ask_config = str(input("Tobi möchtest du eine von uns geprüpfte Konfiguration benutzen? (y) (n)\n:"))
        except ValueError:
            print("Deine Eingabe war leider kein String bitte gebe entweder ein (y) oder (n) ein")
            continue
        if ask_config == "y" or ask_config == "Y":
            try:
                ask_which_config = str(input("Durch Simulationen haben wir diese 2 Konfigurationen für dich gefunden entweder das Liga System (l) oder best of five KO-System (ko5) mit der Ordnung nach der txt Datei. Bitte wähle jetzt deine Konfiguration\n:"))
            except ValueError:
                print("Deine Eingabe war leider kein String bitte gebe entweder ein (l) oder (ko5) ein")
                continue
            if ask_which_config == "l" or ask_which_config == "L":
                print("Die Liga Konfiguration wird geladen.")
                loop = False
                loop2 = False
                for i in range (0,amount_txt):
                    name = "file" + str(i)
                    res = datadic[name]
                    print(type(res))
                    liga(res,name)
            elif ask_which_config == "ko5" or ask_which_config == "KO5":
                print("Die KOx5 Konfiguration wird geladen.")
                skip = True
                loop = False
                loop2 = False
                for i in range (0,amount_txt):
                    name = "file" + str(i)
                    res = datadic[name]
                    ko5(res,name,skip)
            else:
                print("ungültige Eingabe du musst entweder (l) für das liga system oder (ko5) für das best of five K.O-System eingeben.")
                continue
        elif ask_config == "n" or ask_config == "N":
            print("Du hast dich für die manuelle Konfiguration entschieden.")
            loop = False
            loop2 = True
        else:
            print("Keine gültige Eingabe bitte gebe ein (y) für ja oder ein (n) für nein ein")
            continue
    
    while loop2:
        try:
            which_league = str(input("Welches System möchtest du benutzen Liga(l), K.O(ko), K.Ox5(ko5)\n:"))
        except ValueError:
            print("Deine Eingabe war leider kein String bitte gebe entweder ein (l), (ko) oder (ko5) ein")
            continue


        if which_league == "l":
            for i in range (0,amount_txt):
                loop2 = False
                name = "file" + str(i)
                res = datadic[name]
                print(type(res))
                liga(res,name)
        elif which_league == "ko":
            for i in range (0,amount_txt):
                loop2 = False
                name = "file" + str(i)
                res = datadic[name]
                ko(res,name)
        elif which_league == "ko5":
            for i in range (0,amount_txt):
                loop2 = False
                name = "file" + str(i)
                res = datadic[name]
                ko5(res,name,skip)


        else:
            print("Dieses Ligasystem gibt es nicht in unserem System.\nBitte achten sie auch auf eine korrekte Schreibweise ihr Input war : "+ which_league)









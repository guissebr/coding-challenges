import random

weapons = ["Rock", "Paper", "Scissors"]
player_score = 0
cpu_score = 0

while player_score < 3 and cpu_score < 3:
    for i in range(0,3):
        print "%s %s" % (i+1, weapons[i])
    player = (input("Make your selection:")) -1
    cpu = random.randint(0,2)
    print "Player: %s vs. Computer: %s\n" % (weapons[player], weapons[cpu])
    if player != cpu:
        if (player - cpu + 3) % 3 < (cpu - player + 3) % 3:
            player_score += 1
            print "Player wins %d game(s)!\nScore is Player: %d Computer: %d\n" % (player_score, player_score, cpu_score)
        else:
            cpu_score += 1
            print "Computer wins %d game(s)!\nScore is Player: %d Computer: %d\n" % (cpu_score, player_score, cpu_score)
    else: print "Tie!\nScore is Player: %d Computer: %d" % player_score, cpu_score
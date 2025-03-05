import time
import threading

highscore = "0"
count = 0
stop = False
prevScore = ""


def stopGame():
    global stop
    global count
    stop = True
    with open("hiScore.txt", "w") as f:
        f.write(highscore)
    if count > int(prevScore):
        print()
        print(f"you scored {count}")
        print("yey!! you beat your previous record!!")
        print("\nGame ended!!")
    else:
        print(f"you scored {count}")
    return


with open("hiScore.txt") as s:
    highscore = s.read()
    prevScore = highscore


print(
    "GAME RULES : \n1)keep pressing 0 till the timer ends\nBeat your high score\nWin your game\n"
)
print(f"YOUR HIGHSCORE IS : {highscore}\n")
print("start the game!!\n")

timer = threading.Timer(5, stopGame)
timer.start()

while not stop:
    press = input()
    count += 1
    highscore = str(count)

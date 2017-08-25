import webbrowser
import time

number = 0
print("This program started on", time.ctime())
while(number<3):
    time.sleep(15)
    webbrowser.open("https://www.youtube.com/watch?v=GRWMkUUlNuc")
    #webbrowser.open("https://www.youtube.com/watch?v=Awadrec-tHk")
    number = number + 1


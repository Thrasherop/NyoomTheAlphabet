import pyautogui as py
from time import sleep


def main():

    print("You have 5 seconds to tab over")
    sleep(5)

    py.typewrite("abcdefghijklmnopqrstuvwxyz")
    print("Complete")




if __name__ == "__main__":
    main()


import sys
from time import sleep

def main():
    num = int(sys.argv[1])
    for i in range(num):
        print(str(i) + " " + str(i * i * i))
        sleep(1)

if __name__ == "__main__""":
    main()

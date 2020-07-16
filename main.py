from printer import *
from builder import build


def start():
    print_title()
    delay_print("\n\n\tHello, welcome to the spigot plugin builder. Select an option: \n\n", 0.03)
    delay_print("\t\t1. Build a plugin\n\n", 0.03)
    delay_print("\t\t2. Edit plugin configuration settings\n\n", 0.03)
    delay_print("\t\t3. Create custom plugin using blank settings\n\n", 0.03)
	
    answer = input("")
    if int(answer) == 1:
        build()


if __name__ == "__main__":
    start()
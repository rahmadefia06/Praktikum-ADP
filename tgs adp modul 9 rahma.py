import os
import time
from termcolor import cprint, colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_rabbit_logo():
    logo = r"""
      (\/)    
     (•ㅅ•)   
     /   づ   
    KELINCI   
"""
    cprint(logo, 'white', 'on_cyan', attrs=['bold'])

def loading_animation():
    loading_text = ">>> Memuat aplikasi kelinci"
    for i in range(8):
        dots = "." * (i % 4)
        print(colored(loading_text + dots + "   ", 'blue'), end="\r")
        time.sleep(1)
    print(colored("^-^ Aplikasi siap digunakan! ^-^", 'green', attrs=['bold']))

def main():
    clear_screen()
    cprint("="*50, 'yellow')
    cprint("       >>> SELAMAT DATANG DI BUNNY APP <<<        ", 'red', attrs=['bold'])
    cprint("="*50, 'yellow')
    show_rabbit_logo()
    loading_animation()

if __name__ == "__main__":
    main()
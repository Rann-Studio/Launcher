import requests
import filecmp
import time
import sys
import os
import inspect


class Launcher:
    def __init__(self):
        self.print_loading('Checking version')
        self.check_update()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def print_clear(self, message):
        self.clear()
        print(message)
    
        
    def print_loading(self, message, dots=3, loop=2):
        self.clear()
        for i in range(loop):
            for j in range(0, dots + 1):
                print(f"{message}{'.' * j}\033[K", end="\r")
                time.sleep(0.3)

            for j in range(dots - 1, 0, -1):
                print(f"{message}{'.' * j}\033[K", end="\r")
                time.sleep(0.3)


    def check_update(self):
        try:
            latest_version = requests.get('https://raw.githubusercontent.com/Rann-Studio/Launcher/main/Launcher.py', timeout=10).text.replace('\r', '')
            with open("temp.txt", "w", encoding="utf-8") as file:
                file.write(latest_version)

            are_files_equal = filecmp.cmp('Launcher.py', "temp.txt")
            os.remove("temp.txt")

            if are_files_equal:
                self.main_program()
            else:
                self.print_loading('New version is available. Updating')
                with open('Launcher.py', 'w', encoding="utf-8") as file:
                    file.write(latest_version)

                self.print_loading('Update complete, restarting')
                self.restart_program()

        except requests.exceptions.ConnectTimeout:
            self.print_loading('Connection timeout. Attempting to reconnect')
            self.check_update()

        except requests.exceptions.ConnectionError:
            raise SystemExit('No internet connection.')

        except Exception as err:
            raise SystemExit(err)
        

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)
    
    
    def exit_program(self):
        self.print_clear('Thanks for using this program.')
        sys.exit()


    def show_banner(self):
        banner = inspect.cleandoc("""
        ███╗   ██╗███████╗██╗   ██╗████████╗██████╗  ██████╗ ███╗   ██╗
        ████╗  ██║██╔════╝██║   ██║╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
        ██╔██╗ ██║█████╗  ██║   ██║   ██║   ██████╔╝██║   ██║██╔██╗ ██║
        ██║╚██╗██║██╔══╝  ██║   ██║   ██║   ██╔══██╗██║   ██║██║╚██╗██║
        ██║ ╚████║███████╗╚██████╔╝   ██║   ██║  ██║╚██████╔╝██║ ╚████║
        ╚═╝  ╚═══╝╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
        Author : Rann
        """)
        print(banner + '\n')


    def show_menu(self):
        menu = inspect.cleandoc("""
        0. Exit Program
        1. Option 1
        2. Option 2
        3. Option 3
        4. Option 4
        5. Option 5
        """)
        print(menu)
        

    def main_program(self):
        self.clear()
        self.show_banner()
        self.show_menu()
        
        user_input = input("\nSelect an option: ")

        if user_input == "0":
            self.exit_program()
            
        else:
            print('Incorrect option.', end="\r")
            time.sleep(3)
            self.main_program()

if __name__ == '__main__':
    App = Launcher()

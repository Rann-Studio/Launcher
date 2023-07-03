import requests
import filecmp
import time
import sys
import os
import inspect


class Launcher:
    def __init__(self):
        self.print_clear('Checking version...')
        self.check_update()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def print_clear(self, message):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(message)
        time.sleep(3)


    def check_update(self):
        try:
            latest_version = requests.get('https://raw.githubusercontent.com/Rann-Studio/Launcher/main/Launcher.py', timeout=10).text.replace('\r', '')
            with open("temp.txt", "w") as file:
                file.write(latest_version)

            are_files_equal = filecmp.cmp('Launcher.py', "temp.txt")
            os.remove("temp.txt")

            if are_files_equal:
                self.main_program()
            else:
                self.print_clear('New version is available. Updating...')
                with open('Launcher.py', 'w') as file:
                    file.write(latest_version)

                self.print_clear('Update complete, restarting...')
                self.restart_program()

        except requests.exceptions.ConnectTimeout:
            self.print_clear('Connection timeout. Attempting to reconnect...')
            self.check_update()

        except requests.exceptions.ConnectionError:
            raise SystemExit('No internet connection.')

        except Exception as err:
            raise SystemExit(err)
        

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)


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
        print(banner + '\n\n')


    def show_menu(self):
        print("=== MENU ===")
        print("1. Pilihan 1")
        print("2. Pilihan 2")
        print("3. Pilihan 3")
        print("4. Keluar")
        

    def main_program(self):
        self.clear()
        self.show_banner()
        self.show_menu()


if __name__ == '__main__':
    Launcher()

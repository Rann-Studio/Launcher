import requests
import time
import sys
import os
import filecmp


class Launcher:
    def __init__(self):
        self.print_clear('Checking version...')
        self.check_update()

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
                self.print_clear('Already on the latest version.')
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


if __name__ == '__main__':
    Launcher()

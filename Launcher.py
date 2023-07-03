import requests
import time
import sys
import os

class Launcher:

    def __init__(self) -> None:
        """
        Constructor method. It is automatically called when creating a new instance of the class.
        """
        self.check_update()


    def print_clear(self, message) -> None:
        """
        Clear the console, print a message, and sleep for 3 seconds.

        Args:
            message (str): The message to be printed.

        Returns:
            None
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(message)
        time.sleep(3)


    def get_latest_version(self, perform_update=False) -> str:
        """
        Get the latest version from a URL.

        Args:
            perform_update (bool, optional): Whether to perform the update or not. Defaults to False.

        Returns:
            latest_version (str): The latest version file data.
        """
        try:
            latest_version = requests.get('https://raw.githubusercontent.com/Rann-Studio/Launcher/main/Launcher.py', timeout=10).text.replace('\n\n', '')
            if not perform_update:
                return latest_version
            else:
                self.print_clear('Writing new file ...')
                with open('Launcher.py', 'w') as file:
                    file.write(latest_version)
                    file.close()

                self.print_clear('Update complete, restarting ...')
                self.restart_program()

        except requests.exceptions.ConnectTimeout:
            self.print_clear('Connection timeout. Attempting to reconnect ...')
            self.get_latest_version()

        except requests.exceptions.ConnectionError as err:
            raise SystemExit('No internet connection.')
        
        except Exception as err:
            raise SystemExit(err)
        

    def check_update(self) -> None:
        """
        Check for the latest version and perform an update if necessary.

        Args:
            None

        Returns:
            None
        """
        self.print_clear('Checking for the latest version...')
        latest_version = self.get_latest_version()
        
        try:
            now_version =  open('Launcher.py', 'r').read()
            if now_version == latest_version:
                self.print_clear('Already on the latest version.')
            else:
                self.print_clear('New version is available. Updating ...')
                self.get_latest_version(perform_update=True)
                
        except Exception as err:
            raise SystemExit(err)
        
    
    def restart_program(self) -> None:
        """
        Restart the Python program.

        Args:
            None

        Returns:
            None
        """
        python = sys.executable
        os.execl(python, python, *sys.argv)

        
Launcher()

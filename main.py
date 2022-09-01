import os

from service import Service
from rich.console import Console

class Main(Service):
    def __init__(self):
        self.console = Console()

    def start(self):
        try:
            while True:
                ip = self.console.input(
                    "[bold white]"
                    "Enter ip address: "
                )
                print()

                Service(ip).get_info()
        except KeyboardInterrupt:
            exit("Bye!")
        except Exception as error:
            exit(error)

if __name__ == "__main__":
    Main().start()

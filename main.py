import os

from service import Service
from rich.console import Console

class Main(Service):
    def __init__(self):
        self.console = Console()
        self.clear()

    def start(self):
        try:
            while True:
                ip = self.console.input(
                    "[bold white]Enter ip address: "
                )
                print()

                Service(ip).get_info()
        except KeyboardInterrupt:
            exit("Bye!")
        except Exception as error:
            self.console.print(
                "[bold white]Error:[/] "
                f"[bold red]{error}[/]"
            )
            exit()

    @staticmethod
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

if __name__ == "__main__":
    Main().start()

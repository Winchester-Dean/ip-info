import json
import requests

from rich.console import Console

class Service:
    """Service: https://ipapi.co"""
    def __init__(self, ip: str):
        self.ip = ip
        self.console = Console()

    def get_info(self):
        try:
            request = requests.get(
                "https://ipapi.co/{}/json".format(
                    self.ip
                )
            ).json()

            ip = request["ip"]
            version = request["version"]
            city = request["city"]
            country = request["country_name"]
            country_code = request["country_code"]
            calling_code = request["country_calling_code"]
            languages = request["languages"]
            time_zone = request["timezone"]
            currency = request["currency"]
            currency_name = request["currency_name"]
            organization = request["org"]

            green = "[bold green]"
            close = "[/]"

            text = (
                "[bold white]"
                f"{green}Ip{close}: {ip}\n"
                f"{green}Ip version{close}: {version}\n"
                f"{green}Country{close}: {country}\n"
                f"{green}Country code{close}: "
                f"{country_code}\n"
                f"{green}City{close}: {city}\n"
                f"{green}Country calling code{close}: "
                f"{calling_code}\n"
                f"{green}Languages{close}: {languages}\n"
                f"{green}Time zone{close}: {time_zone}\n"
                f"{green}Currency{close}: {currency}\n"
                f"{green}Currency name{close}: "
                f"{currency_name}\n"
                f"{green}Organization{close}: "
                f"{organization}\n"
                "[/]"
            )

            self.console.print(text)
        except Exception as error:
            self.console.print(
                "[bold white]Error:[/] "
                f"[bold red]{error}[/]"
            )
            exit()


import platform
import socket
import psutil
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
def get_cpu_model():
    try:
        with open("/proc/cpuinfo", "r") as file:
            for line in file:
                if line.startswith("model name"):
                    return line.split(":", 1)[1].strip()
    except OSError:
        pass

    return platform.processor() or "Inconnu"

def get_system_info():
    console.print(
        Panel.fit(
            "[bold cyan]SYSTEM INFO[/bold cyan]\n"
            "[white]Rapport détaillé de la machine[/white]",
            border_style="cyan"
        )
    )

    table = Table(title="Informations générales", border_style="cyan")
    table.add_column("Élément", style="cyan")
    table.add_column("Valeur", style="white")

    table.add_row("Système", platform.system())
    table.add_row("Version", platform.version())
    table.add_row("Architecture", platform.machine())
    table.add_row("Nom de la machine", platform.node())
    table.add_row("Utilisateur", os.getlogin())

    console.print(table)

    cpu = Table(title="Processeur", border_style="green")
    cpu.add_column("Élément", style="green")
    cpu.add_column("Valeur")

    cpu.add_row("Processeur", get_cpu_model())
    cpu.add_row("Cœurs physiques", str(psutil.cpu_count(logical=False)))
    cpu.add_row("Cœurs logiques", str(psutil.cpu_count(logical=True)))
    cpu.add_row("Utilisation CPU", f"{psutil.cpu_percent(interval=1)} %")

    console.print(cpu)

    ram = psutil.virtual_memory()

    memory = Table(title="Mémoire RAM", border_style="yellow")
    memory.add_column("Élément", style="yellow")
    memory.add_column("Valeur")

    memory.add_row("RAM totale", f"{ram.total / (1024**3):.2f} Go")
    memory.add_row("RAM utilisée", f"{ram.used / (1024**3):.2f} Go")
    memory.add_row("RAM disponible", f"{ram.available / (1024**3):.2f} Go")
    memory.add_row("Utilisation", f"{ram.percent} %")

    console.print(memory)

    partition = "/" if platform.system() != "Windows" else os.environ.get("SystemDrive", "C:") + "\\"
    disk = psutil.disk_usage(partition)

    storage = Table(title="Stockage", border_style="magenta")
    storage.add_column("Élément", style="magenta")
    storage.add_column("Valeur")

    storage.add_row("Espace total", f"{disk.total / (1024**3):.2f} Go")
    storage.add_row("Espace utilisé", f"{disk.used / (1024**3):.2f} Go")
    storage.add_row("Espace libre", f"{disk.free / (1024**3):.2f} Go")

    console.print(storage)

    network = Table(title="Réseau", border_style="blue")
    network.add_column("Élément", style="blue")
    network.add_column("Valeur")

    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = "Indisponible"

    network.add_row("Nom d'hôte", hostname)
    network.add_row("Adresse IP", ip)

    console.print(network)

    console.print(
        Panel(
            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            title="Date et heure",
            border_style="white"
        )
    )


if __name__ == "__main__":
    get_system_info()

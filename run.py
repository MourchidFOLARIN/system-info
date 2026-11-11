
import platform
import socket
import psutil
import os
from datetime import datetime


def get_system_info():
    print("=" * 55)
    print("          INFORMATIONS SUR LA MACHINE")
    print("=" * 55)

    # Informations générales
    print("\n[1] SYSTEME")
    print("Système :", platform.system())
    print("Version :", platform.version())
    print("Architecture :", platform.machine())
    print("Nom de la machine :", platform.node())
    print("Nom de l'utilisateur :", os.getlogin())

    # Informations processeur
    print("\n[2] PROCESSEUR")
    print("Processeur :", platform.processor())
    print("Cœurs physiques :", psutil.cpu_count(logical=False))
    print("Cœurs logiques :", psutil.cpu_count(logical=True))
    print("Utilisation CPU :", psutil.cpu_percent(interval=1), "%")

    # Mémoire RAM
    print("\n[3] MEMOIRE RAM")
    ram = psutil.virtual_memory()
    print("RAM totale :", round(ram.total / (1024**3), 2), "Go")
    print("RAM utilisée :", round(ram.used / (1024**3), 2), "Go")
    print("RAM disponible :", round(ram.available / (1024**3), 2), "Go")
    print("Utilisation :", ram.percent, "%")

    # Stockage
    print("\n[4] STOCKAGE")
    partition = os.environ.get("SystemDrive", "/") + (
        "\\" if platform.system() == "Windows" else ""
    )
    disk = psutil.disk_usage(partition)
    print("Espace total :", round(disk.total / (1024**3), 2), "Go")
    print("Espace utilisé :", round(disk.used / (1024**3), 2), "Go")
    print("Espace libre :", round(disk.free / (1024**3), 2), "Go")

    # Réseau
    print("\n[5] RESEAU")
    print("Nom d'hôte :", socket.gethostname())

    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("Adresse IP :", ip)
    except socket.gaierror:
        print("Adresse IP : indisponible")

    # Date et heure
    print("\n[6] DATE ET HEURE")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    print("\n" + "=" * 55)
    print("          FIN DU RAPPORT SYSTEME")
    print("=" * 55)


if __name__ == "__main__":
    get_system_info()

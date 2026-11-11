# System Info

**System Info** est un outil CLI développé en Python permettant de collecter et d'afficher les principales informations matérielles et système d'un ordinateur directement dans le terminal.

## Fonctionnalités

- **Système :** système d'exploitation, version, architecture, nom de machine et utilisateur.
- **Processeur :** modèle, nombre de cœurs physiques et logiques, utilisation CPU.
- **Mémoire RAM :** mémoire totale, utilisée, disponible et pourcentage d'utilisation.
- **Stockage :** espace total, utilisé et disponible.
- **Réseau :** interfaces réseau et adresses IPv4.
- **Date et heure :** date et heure locales de la machine.
- **Interface terminal :** affichage organisé et coloré grâce à Rich.

## Technologies utilisées

- Python 3
- Psutil
- Rich
- Socket
- Platform

## Prérequis

- Python 3.10 ou supérieur
- Git
- pip
- venv

## Installation

### 1. Cloner le dépôt

```bash
git clone git@github.com:MourchidFOLARIN/system-info.git
```

Accéder au répertoire du projet :

```bash
cd system-info
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv .venv
```

### 3. Activer l'environnement virtuel

Sous Linux :

```bash
source .venv/bin/activate
```

Sous Windows :

```bash
.venv\Scripts\activate
```

### 4. Installer le projet

```bash
python -m pip install .
```

## Utilisation

Une fois l'installation terminée, lancez simplement :

```bash
systeme
```

L'outil affiche automatiquement le rapport système dans le terminal.

## Développement

Pour installer le projet en mode développement :

```bash
python -m pip install -e .
```

## Structure du projet

```text
system-info/
│
├── run.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

## Auteur

**Mourchid FOLARIN**

- GitHub : https://github.com/MourchidFOLARIN

---

*System Info — Know your machine.*

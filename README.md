# 📜 README – Messagerie IP avec Python, Tkinter et Sockets

## 📌 Description

Ce projet est une **messagerie instantanée locale** en Python utilisant :

* **Sockets** (`socket`) pour la communication réseau
* **Threads** (`threading`) pour gérer l’envoi et la réception en simultané
* **Tkinter** (`tk`, `ttk`, `scrolledtext`) pour l’interface graphique

Le système fonctionne sur le modèle **client-serveur** :

* Un **serveur** écoute sur une IP et un port donnés.
* Un **client** se connecte à cette adresse et échange des messages en temps réel.

Ce programme est **multi-usage** : l’IP et le port ne sont pas codés en dur, ils sont configurables via une interface avant de démarrer la discussion.

---

## 🛠 Fonctionnement général

### 1️⃣ Lancement du serveur

1. **Fenêtre de configuration** :

   * L’utilisateur saisit l’**adresse IP** sur laquelle le serveur doit écouter.
     (Exemple : `0.0.0.0` pour écouter sur toutes les interfaces)
   * L’utilisateur saisit le **port** (exemple : `5566`).
   * Le bouton **Lancer le serveur** démarre l’écoute réseau.

2. **Interface principale** :

   * Une fenêtre Tkinter s’ouvre avec un **historique de chat**.
   * Un message `"En attente de connexion..."` apparaît.
   * En arrière-plan, un **thread** exécute `socket.accept()` pour attendre un client.

3. **Connexion d’un client** :

   * Quand un client se connecte, l’historique affiche :
     `"Connexion établie avec [adresse IP]"`.
   * Un thread dédié écoute les messages entrants du client.
   * L’utilisateur peut taper un message et appuyer sur **Entrée** ou cliquer sur **Envoyer**.

---

### 2️⃣ Lancement du client

1. **Fenêtre de configuration** :

   * L’utilisateur saisit l’**adresse IP du serveur**.
   * L’utilisateur saisit le **port du serveur**.
   * Le bouton **Se connecter** tente une connexion.

2. **Interface principale** :

   * Un message `"Connecté au serveur"` s’affiche.
   * Un thread écoute les messages envoyés par le serveur.
   * L’utilisateur peut taper et envoyer des messages en **appuyant sur Entrée** ou **en cliquant sur Envoyer**.

---

### 3️⃣ Communication entre serveur et client

* **Une seule connexion socket** est établie et reste ouverte tant que les deux programmes tournent.
* Chaque côté possède :

  * **Un thread d’écoute** pour recevoir les messages entrants.
  * **L’interface principale** qui envoie les messages quand on appuie sur Entrée ou le bouton.
* Les messages reçus sont affichés dans la zone de texte avec un préfixe `"Client :"` ou `"Serveur :"`.

---

## 📂 Structure des fichiers

```
/projet_messagerie
│── serveur.py  # Code côté serveur
│── client.py   # Code côté client
│── README.md   # Documentation
```

---

## 🚀 Utilisation

### 📌 Lancer le serveur

```bash
python serveur.py
```

* Entrer l’IP et le port d’écoute dans la fenêtre.
* Attendre qu’un client se connecte.

### 📌 Lancer le client

```bash
python client.py
```

* Entrer l’IP et le port du serveur.
* Commencer à échanger des messages.

---

## ⚙️ Technologies utilisées

* **Python 3
* **Tkinter** (interfaces graphiques)
* **Socket** (communication réseau)
* **Threading** (envoi/réception simultanés)

---

## 💡 Notes

* Pour communiquer entre deux machines différentes, elles doivent être sur **le même réseau** ou le port du serveur doit être **ouvert dans le pare-feu**.
* Le serveur doit être lancé **avant** le client.
* Vous pouvez tester en local avec `127.0.0.1` comme adresse IP.

---

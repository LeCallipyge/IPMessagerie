import socket
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext

# === CONFIG SOCKET ===
host, port = ('192.168.1.##', 5566)

serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur_socket.connect((host, port))

# === INTERFACE TKINTER ===
fenetre = tk.Tk()
fenetre.title("Chat connecté")
fenetre.geometry("400x500")

# Zone messages
zone_texte = scrolledtext.ScrolledText(fenetre, state='disabled', wrap=tk.WORD)
zone_texte.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Bas de la fenêtre
cadre_bas = ttk.Frame(fenetre)
cadre_bas.pack(fill=tk.X, padx=10, pady=10)

champ_message = ttk.Entry(cadre_bas)
champ_message.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# Fonction pour afficher un message dans la zone de chat
def afficher_message(msg):
    zone_texte.config(state='normal')
    zone_texte.insert(tk.END, msg + "\n")
    zone_texte.config(state='disabled')
    zone_texte.yview(tk.END)

# Fonction pour envoyer un message depuis l'interface
def envoyer_message():
    message = champ_message.get()
    if message.strip():
        serveur_socket.sendall(message.encode("utf8"))
        afficher_message(f"Moi : {message}")
        champ_message.delete(0, tk.END)

# Lier le bouton envoyer
bouton_envoyer = ttk.Button(cadre_bas, text="Envoyer", command=envoyer_message)
bouton_envoyer.pack(side=tk.RIGHT)

# Fonction pour recevoir les messages en continu
def recevoir_message():
    while True:
        try:
            message_recu = serveur_socket.recv(1024)
            if not message_recu:
                break  # client déconnecté
            message = message_recu.decode("utf8")
            afficher_message(f"Client : {message}")
        except:
            break

# Démarrer le thread de réception
thread_recevoir = threading.Thread(target=recevoir_message, daemon=True)
thread_recevoir.start()

# Lancer l'interface graphique
fenetre.mainloop()
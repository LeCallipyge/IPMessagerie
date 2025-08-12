import socket
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext

# === Fenêtre de configuration ===
config_fenetre = tk.Tk()
config_fenetre.title("Configuration Serveur")
config_fenetre.geometry("250x200")

tk.Label(config_fenetre, text="Adresse IP :").pack(pady=5)
ip_entry = ttk.Entry(config_fenetre)
ip_entry.insert(0, "0.0.0.0")  # par défaut écoute sur toutes les IP
ip_entry.pack(pady=5)

tk.Label(config_fenetre, text="Port :").pack(pady=5)
port_entry = ttk.Entry(config_fenetre)
port_entry.insert(0, "5566")
port_entry.pack(pady=5)

def lancer_serveur():
    global host, port
    host = ip_entry.get()
    port = int(port_entry.get())
    config_fenetre.destroy()

ttk.Button(config_fenetre, text="Lancer le serveur", command=lancer_serveur).pack(pady=10)
config_fenetre.mainloop()

# === Création du socket ===
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur_socket.bind((host, port))
serveur_socket.listen()

# === Interface chat ===
fenetre = tk.Tk()
fenetre.title(f"Serveur - {host}:{port}")
fenetre.geometry("400x500")

zone_texte = scrolledtext.ScrolledText(fenetre, state='disabled', wrap=tk.WORD)
zone_texte.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

cadre_bas = ttk.Frame(fenetre)
cadre_bas.pack(fill=tk.X, padx=10, pady=10)

champ_message = ttk.Entry(cadre_bas)
champ_message.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

def afficher_message(msg):
    zone_texte.config(state='normal')
    zone_texte.insert(tk.END, msg + "\n")
    zone_texte.config(state='disabled')
    zone_texte.yview(tk.END)

conn = None

def envoyer_message(event=None):
    if conn:
        message = champ_message.get()
        if message.strip():
            conn.sendall(message.encode("utf8"))
            afficher_message(f"Moi : {message}")
            champ_message.delete(0, tk.END)

bouton_envoyer = ttk.Button(cadre_bas, text="Envoyer", command=envoyer_message)
bouton_envoyer.pack(side=tk.RIGHT)
fenetre.bind("<Return>", envoyer_message)

def attendre_connexion():
    global conn, adresse_client
    afficher_message("En attente de connexion...")
    conn, adresse_client = serveur_socket.accept()
    afficher_message(f"Connexion établie avec {adresse_client[0]}")
    threading.Thread(target=recevoir_message, daemon=True).start()

def recevoir_message():
    while True:
        try:
            message_recu = conn.recv(1024)
            if not message_recu:
                break
            message = message_recu.decode("utf8")
            afficher_message(f"Client : {message}")
        except:
            break

thread_connexion = threading.Thread(target=attendre_connexion, daemon=True)
thread_connexion.start()

fenetre.mainloop()

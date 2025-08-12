# 📜 README – IP Messaging with Python, Tkinter, and Sockets

## 📌 Description

This project is a **local instant messaging system** in Python using:

* **Sockets** (`socket`) for network communication
* **Threads** (`threading`) to handle sending and receiving simultaneously
* **Tkinter** (`tk`, `ttk`, `scrolledtext`) for the graphical interface

The system works on a **client-server** model:

* A **server** listens on a given IP and port.
* A **client** connects to this address and exchanges messages in real-time.

This program is **flexible**: the IP and port are not hardcoded, they are configurable via an interface before starting the chat.

---

## 🛠 General Operation

### 1️⃣ Starting the Server

1. **Configuration window**:

   * The user enters the **IP address** on which the server will listen.
     (Example: `0.0.0.0` to listen on all interfaces)
   * The user enters the **port** (example: `5566`).
   * The **Start Server** button launches the listening process.

2. **Main interface**:

   * A Tkinter window opens with a **chat history** panel.
   * A message `"Waiting for connection..."` is displayed.
   * In the background, a **thread** runs `socket.accept()` to wait for a client.

3. **Client connection**:

   * When a client connects, the history displays:
     `"Connection established with [IP address]"`.
   * A dedicated thread listens for incoming messages from the client.
   * The user can type a message and press **Enter** or click **Send**.

---

### 2️⃣ Starting the Client

1. **Configuration window**:

   * The user enters the **server IP address**.
   * The user enters the **server port**.
   * The **Connect** button attempts to establish a connection.

2. **Main interface**:

   * A message `"Connected to server"` is displayed.
   * A thread listens for messages sent by the server.
   * The user can type and send messages by **pressing Enter** or **clicking Send**.

---

### 3️⃣ Communication Between Server and Client

* **A single socket connection** is established and remains open as long as both programs are running.

* Each side has:

  * **A listening thread** to receive incoming messages.
  * **The main interface** to send messages when Enter is pressed or the button is clicked.

* Incoming messages are displayed in the text area with a `"Client:"` or `"Server:"` prefix.

---

## 📂 File Structure

```
/messaging_project
│── server.py   # Server-side code
│── client.py   # Client-side code
│── README.md   # Documentation
│── LICENSE     # License
```

---

## 🚀 Usage

### 📌 Start the Server

```bash
python server.py
```

* Enter the listening IP and port in the window.
* Wait for a client to connect.

### 📌 Start the Client

```bash
python client.py
```

* Enter the server IP and port.
* Start exchanging messages.

---

## ⚙️ Technologies Used

* **Python 3**
* **Tkinter** (GUI)
* **Socket** (network communication)
* **Threading** (simultaneous send/receive)

---

## 💡 Notes

* To communicate between two different machines, they must be on **the same network** or the server port must be **open in the firewall**.
* The server must be started **before** the client.
* You can test locally using `127.0.0.1` as the IP address.

---

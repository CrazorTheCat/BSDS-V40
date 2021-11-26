import socket
import threading
import time
import traceback
from builtins import ConnectionError

from Logic.Client.ClientsManager import ClientsManager
from Logic.Data.PacketsHandler import PacketsHandler
from Logic.Client.PlayerManager import Players
from Messaging.Packets.Server.Home.LobbyInfoMessage import LobbyInfoMessage


class Core:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def CoreInit(self):
        self.server.bind(('127.0.0.1', 9339))
        print("Socket binded!")
        while True:
            self.server.listen()
            socket, address = self.server.accept()
            print(f'Got new connection with address: {address[0]}')
            ConnectionThread(socket, address).start()

class ConnectionThread(threading.Thread):
    def __init__(self, client, address):
        super().__init__()
        self.address = address
        self.client = client
        self.player = Players()
        LobbyInfoMessageThread(self.client).start()

    def run(self):
        try:
            while True:
                # Reading and processing packet
                PacketsHandler.ReadHeader(self)

        except ConnectionError:
            print(f"Client with ip: {self.address[0]} disconnected!")
            ClientsManager.RemoveSocket(self.player.LowID)
            self.client.close()
            print(traceback.format_exc())
            # exit(0)
            return

        except OSError:
            print(f"Client with ip: {self.address[0]} disconnected!")
            ClientsManager.RemoveSocket(self.player.LowID)
            self.client.close()
            print(traceback.format_exc())
            # exit(0)
            return

class LobbyInfoMessageThread(threading.Thread):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.player = Players

    def run(self):
        timeout = time.time()
        try:
            while True:
                time.sleep(0.1)
                if time.time() >= timeout + 1:
                    LobbyInfoMessage(self.client, self.player).send(self.client)
                    timeout = time.time()
        except:
            return

Core().CoreInit()
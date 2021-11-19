import socket
import threading
import traceback
from builtins import ConnectionError

from Logic.Client.ClientsManager import ClientsManager
from Logic.Data.PacketsHandler import PacketsHandler
from Logic.Client.PlayerManager import Players

class Core:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def CoreInit(self):
        self.server.bind(('0.0.0.0', 9339))
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
        self.player = Players

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
            exit(0)

Core().CoreInit()
class ClientsManager:

    SocketsList = {"Sockets": {}}

    def AddSocket(PlayerID, Sockets):
        ClientsManager.SocketsList["Sockets"][PlayerID] = Sockets

    def RemoveSocket(PlayerID):
        try:
            ClientsManager.SocketsList["Sockets"].pop(PlayerID)
        except KeyError:
            print(f"Cannot remove socket with id: {PlayerID} Reason: {PlayerID} is not in the list.")

    def GetAll():
        return ClientsManager.SocketsList

    def GetCount():
        return len(ClientsManager.SocketsList["Sockets"])
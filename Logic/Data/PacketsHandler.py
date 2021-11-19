from Messaging.LogicMessageFactory import identifiers, knownList
from Messaging.Packets.Server.Home.LobbyInfoMessage import LobbyInfoMessage
from Logic.Utility.Utils import Utils


class PacketsHandler:
    def ReadHeader(self):
        def recv(n):
            data = bytearray()
            while len(data) < n:
                packet = self.client.recv(n - len(data))
                if not packet:
                    return None
                data.extend(packet)
            return data

        packetInfo = self.client.recv(7)
        if len(packetInfo):
            packet_identifier = int.from_bytes(packetInfo[:2], 'big')
            length = int.from_bytes(packetInfo[2:5], 'big')
            version = int.from_bytes(packetInfo[5:7], 'big')
            data = recv(length)

            if packet_identifier in identifiers:
                message = identifiers[packet_identifier](self.client, self.player, data)
                packet_name = identifiers[packet_identifier].__name__

                print(f"---------------------------------------------------------------------------------------------")
                print(f"\033[93m[{Utils.GetTime(self)}] [SERVER] PacketID: {packet_identifier} Name: {packet_name} Length: {length} Version: {version}, Data: {data}")

                message.decode()
                message.process()

            elif packet_identifier in knownList:
                print(f"---------------------------------------------------------------------------------------------")
                print(f"\033[93m[{Utils.GetTime(self)}] [SERVER] PacketID: {packet_identifier} Name: {knownList[packet_identifier]} Length: {length} Version: {version}, Data: {data}")
            else:
                print(f"---------------------------------------------------------------------------------------------")
                print(f"\033[93m[{Utils.GetTime(self)}] [SERVER] PacketID: {packet_identifier} Name: Unknown Length: {length} Version: {version}, Data: {data}")

            # Yes i like to put useless line of code ¯\_(ツ)_/¯

            LobbyInfoMessage(self.client, self.player).send(self.client)
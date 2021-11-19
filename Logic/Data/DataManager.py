from io import BufferedReader, BytesIO
import socket

from Logic.Utility.Utils import Utils
from Logic.Client.ClientsManager import ClientsManager

import zlib

class cryptoInfo:
    cryptobytesPosition = -1
    changed = False

class Writer:
    def __init__(self, client, endian: str = 'big'):
        self.client = client
        self.endian = endian
        self.buffer = b''


    def writeIntLE(self, data, length=4):
        self.buffer += data.to_bytes(length, 'little')

    def writeInt8(self, data):
        self.writeInt(data, 1)

    def writeInt16(self, data):
        self.writeInt(data, 2)

    def writeInt24(self, data):
        self.writeInt(data, 3)

    def writeInt(self, data: int, length: int = 4):
        if data > 0:
            self.buffer += data.to_bytes(length, 'big', signed=False)
        else:
            self.buffer += data.to_bytes(length, 'big', signed=True)

    def writeUInteger(self, data: int, length: int = 1):
        self.buffer += data.to_bytes(length, 'big', signed=False)

    def writeUInt8(self, integer: int):
        self.writeUInteger(integer)

    def writeLong(self, high, low):
        self.buffer += high.to_bytes(4, 'big') + low.to_bytes(4, 'big')

    def writeVLong(self, high, low):
        self.writeVint(high)
        self.writeVint(low)

    def writeArrayVint(self, vintArray: list):
        self.writeVint(len(vintArray))
        for i in vintArray:
            self.writeVint(i)

    def writeBoolean(self, value):
        self.writeUInt8(value)

    def writeCompressedString(self, data: bytes):
        compressed = zlib.compress(data)
        self.writeInt(len(compressed) + 4)
        self.writeIntLE(len(data))
        self.buffer += compressed

    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]
            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))

    def writeVint(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
        elif data < 0:
            self.writeVint((2147483648 * 2) + data)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f

                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)
                final += b.to_bytes(1, 'big')
                data >>= 7
        self.buffer += final

    def writeString(self, string = None):
        if string is None:
            self.writeInt((2 ** 32) - 1)
        else:
            if type(string) == bytes:
                encoded = string
            else:
                encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded

    def writeStringReference(self, string: str = None):
        encoded = string.encode('utf-8')
        self.writeInt16(0)
        self.writeVint(len(encoded))
        self.buffer += encoded

    def writeByte(self, data):
        if data > 255:
            self.buffer += data.to_bytes(2, 'big', signed=False)
        elif data > 127:
            self.buffer += data.to_bytes(1, 'big', signed=False)
        else:
            self.buffer += data.to_bytes(1, 'big', signed=True)

    def writeBytes(self, data):
        self.buffer += data

    def writeDataReference(self, x, y = 0):
        if x == 0:
            self.writeVint(0)
        else:
            self.writeVint(x)
            self.writeVint(y)

    def writeArrayVint(self, array):
        self.writeVint(len(array))
        for i in array:
            self.writeVint(i)

    def send(self, PlayerLowID, cryptoBytesEnd: int = 1):
        self.encode()
        packet = self.buffer
        self.buffer = self.id.to_bytes(2, 'big', signed=True)
        self.writeInt24(len(packet))
        if hasattr(self, 'version'):
            self.writeInt16(self.version)
        else:
            self.version = 0
            self.writeInt16(0)
        print(f"---------------------------------------------------------------------------------------------")
        print(f"\033[92m[{Utils.GetTime(self)}] [CLIENT] PacketID: {self.id} Name: {self.__class__.__name__} Length: {len(packet)} Version: {self.version}")
        crypto_bytes = b'\xff\xff\x00\x00\x00\x00\x00'
        if cryptoInfo.changed == False:
            cryptoInfo.cryptobytesPosition = cryptoBytesEnd
            cryptoInfo.changed = True

        if cryptoInfo.cryptobytesPosition == 0:
            crypto_bytes += self.buffer + packet
        elif cryptoInfo.cryptobytesPosition == 1:
            crypto_bytes = self.buffer + packet + crypto_bytes
        elif cryptoInfo.cryptobytesPosition == 2:
            crypto_bytes = self.buffer + packet

        try:
            if self.id == 23457:
                self.client.sendall(crypto_bytes)
                return
            ClientsManager.SocketsList["Sockets"][PlayerLowID].sendall(crypto_bytes)
        except KeyError:
            pass

class Reader(BufferedReader):
    def __init__(self, header_bytes):
        super().__init__(BytesIO(header_bytes))
        self.bytes_of_packets = header_bytes

    def readByte(self):
        return int.from_bytes(self.read(1), "big")

    def readBytes(self, length):
        return self.read(length)

    def readBoolean(self):
        result = bool.from_bytes(bytes=self.read(1), byteorder='big', signed=False)
        if result == True:
            return True
        else:
            return False

    def readIntLE(self):
        return int.from_bytes(self.read(4), "little")

    def readInt(self):
        return int.from_bytes(self.read(4), "big")

    def readInt8(self):
        return int.from_bytes(self.read(1), "big")

    def readInt16(self):
        return int.from_bytes(self.read(2), "big")

    def readInt24(self):
        return int.from_bytes(self.read(3), "big")

    def readVint(self):
        n = self.readVarint(True)
        return (n >> 1) ^ (-(n & 1))

    def readVLong(self):
        ID = []
        ID.append(self.readVint())
        ID.append(self.readVint())
        return ID

    def readShort(self, length=2):
        return int.from_bytes(self.read(length), "big")

    def readLong(self):
        high = self.readInt()
        low = self.readInt()
        return [high, low]

    def readCompressedString(self):
        self.readInt()
        data_length = self.readIntLE()

        compressed = self.readBytes(data_length)

        return zlib.decompress(compressed)

    def readStringReference(self):
        return self.readString()

    def readUInt8(self):
        return self.readUInteger()

    def readUInteger(self, length: int = 1, endian: str = 'big'):
        result = 0
        i = 0
        for x in range(length):
            byte = self.bytes_of_packets[i]

            bit_padding = x * 8
            if endian == 'big':
                bit_padding = (8 * (length - 1)) - bit_padding

            result |= byte << bit_padding
            i += 1

        return result

    def readStringBot(self):
        lenght = self.readVint()
        if lenght == pow(2, 32) - 1:
            return b""
        else:
            try:
                decoded = self.read(lenght)
            except MemoryError:
                raise IndexError("String out of range.")
            else:
                return decoded.decode('utf-8')

    def readString(self):
        lenght = self.readInt()
        (pow(2, 32) - 1)
        if lenght == pow(2, 32) - 1:
            return b""
        else:
            try:
                decoded = self.read(lenght)
            except MemoryError:
                raise IndexError("String out of range.")
            else:
                return decoded.decode('utf-8')

    def readDataReference(self):
        high = self.readVint()
        low = self.readVint()
        if (high):
            return high * 1000000 + low
        else:
            return 0

    def readDataReferenceDouble(self):
        high = self.readVint()
        if high == 0:
            return 0
        low = self.readVint()
        return [high, low]

    def readDataReferenceDouble(self, retList = True):
        high = self.readVint()
        if retList == True and high == 0:
            return [0, 0]
        elif high == 0:
            return 0
        low = self.readVint()
        return [high, low]

    def readVarint(self, rotate: bool = True):
        result = 0
        shift = 0
        while True:
            byte = self.readByte()
            if rotate and shift == 0:
                seventh = (byte & 0x40) >> 6  # save 7th bit
                msb = (byte & 0x80) >> 7  # save msb
                n = byte << 1  # rotate to the left
                n = n & ~0x181  # clear 8th and 1st bit and 9th if any
                byte = n | (msb << 7) | seventh  # insert msb and 6th back in
            result |= (byte & 0x7f) << shift
            shift += 7
            if not (byte & 0x80):
                break
        return result
from Logic.Stream.AllianceEventStreamEntry import AllianceEventStreamEntry
from Logic.Stream.ChatStreamEntry import ChatStreamEntry
from Logic.Stream.JoinRequestAllianceStreamEntry import JoinRequestAllianceStreamEntry
from Logic.Stream.MessageDataStreamEntry import MessageDataStreamEntry
from Logic.Stream.QuickChatStreamEntry import QuickChatStreamEntry
from Logic.Stream.ReplayStreamEntry import ReplayStreamEntry
from Logic.Stream.StreamEntry import StreamEntry
from Logic.Stream.TeamCreatedStreamEntry import TeamCreatedStreamEntry

StreamIDs = {
    2: ChatStreamEntry,
    3: JoinRequestAllianceStreamEntry,
    4: AllianceEventStreamEntry,
    5: ReplayStreamEntry,
    6: MessageDataStreamEntry,
    7: 'Unknown',
    8: QuickChatStreamEntry,
    77: TeamCreatedStreamEntry,
}

class StreamEntryFactory:
    def encode(self, info):
        streamID = info['StreamType']
        if streamID not in StreamIDs:
            StreamEntry.encode(self, info)
            raise NotImplementedError(f"Stream with id {streamID} is not implemented.")
        elif type(StreamIDs[streamID]) != str:
            StreamIDs[streamID].encode(self, info)
        else:
            raise NotImplementedError(f"{StreamIDs[streamID]} is not implemented.")


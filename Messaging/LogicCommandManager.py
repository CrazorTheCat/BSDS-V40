from Messaging.Commands.Client.LogicClearESportsHubNotificationCommand import LogicClearESportsHubNotificationCommand
from Messaging.Commands.Client.LogicClearShopTickersCommand import LogicClearShopTickersCommand
from Messaging.Commands.Client.LogicEnableSkinRandomizerCommand import LogicEnableSkinRandomizerCommand
from Messaging.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
from Messaging.Commands.Client.LogicHelpOpenedCommand import LogicHelpOpenedCommand
from Messaging.Commands.Client.LogicHeroSeenCommand import LogicHeroSeenCommand
from Messaging.Commands.Client.LogicPurchaseDoubleCoinsCommand import LogicPurchaseDoubleCoinsCommand
from Messaging.Commands.Client.LogicPurchaseHeroLvlUpMaterialCommand import LogicPurchaseHeroLvlUpMaterialCommand
from Messaging.Commands.Client.LogicQuestsSeenCommand import LogicQuestsSeenCommand
from Messaging.Commands.Client.LogicSelectCharacterCommand import LogicSelectCharacterCommand
from Messaging.Commands.Client.LogicSelectEmoteCommand import LogicSelectEmoteCommand
from Messaging.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Messaging.Commands.Client.LogicSelectStarPowerCommand import LogicSelectStarPowerCommand
from Messaging.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Messaging.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Messaging.Commands.Client.LogicViewInboxNotificationCommand import LogicViewInboxNotificationCommand

commandIdentifiers = {
    500: LogicGatchaCommand,
    503: 'LogicClaimDailyRewardCommand',
    504: 'LogicSendAllianceMailCommand',
    505: LogicSetPlayerThumbnailCommand,
    506: LogicSelectSkinCommand,
    507: 'LogicUnlockSkinCommand',
    508: 'LogicChangeControlModeCommand',
    509: LogicPurchaseDoubleCoinsCommand,
    511: LogicHelpOpenedCommand,
    512: 'LogicToggleInGameHintsCommand',
    514: 'LogicDeleteNotificationCommand',
    515: LogicClearShopTickersCommand,
    517: 'LogicClaimRankUpRewardCommand',
    518: 'LogicPurchaseTicketsCommand',
    519: 'LogicPurchaseOfferCommand',
    520: 'LogicLevelUpCommand',
    521: LogicPurchaseHeroLvlUpMaterialCommand,
    522: LogicHeroSeenCommand,
    523: 'LogicClaimAdRewardCommand',
    524: 'LogicVideoStartedCommand',
    525: LogicSelectCharacterCommand,
    526: 'LogicUnlockFreeSkinsCommand',
    527: LogicSetPlayerNameColorCommand,
    528: LogicViewInboxNotificationCommand,
    529: LogicSelectStarPowerCommand,
    530: 'LogicSetPlayerAgeCommand',
    531: 'LogicCancelPurchaseOfferCommand',
    532: 'LogicItemSeenCommand',
    533: LogicQuestsSeenCommand,
    534: 'LogicPurchaseBrawlPassCommand',
    535: 'LogicClaimTailRewardCommand',
    536: 'LogicPurchaseBrawlpassProgressCommand',
    537: 'LogicVanityItemSeenCommand',
    538: LogicSelectEmoteCommand,
    539: 'LogicBrawlPassAutoCollectWarningSeenCommand',
    540: 'LogicPurchaseChallengeLivesCommand',
    541: LogicClearESportsHubNotificationCommand,
    542: 'LogicSelectGroupSkinCommand',
    547: LogicEnableSkinRandomizerCommand,
    1000: 'LogicDebugCommand'
}
from enum import IntEnum

class MembershipType(IntEnum):
    TigerXbox = 1
    TigerPsn = 2
    TigerSteam = 3
    TigerBlizzard = 4
    TigerStadia = 5
    TigerEgs = 6
    TigerDemon = 10
    BungieNext = 254
    All = -1

class ErrorCode(IntEnum):
    Success = 1
    WebAuthRequired = 99
from dataclasses import dataclass
from Entities.GroupV2 import GroupUserInfoCard

@dataclass
class UserMembershipData:
    """ Ref: https://bungie-net.github.io/multi/schema_User-UserMembershipData.html
    """
    destinyMemberships: list[GroupUserInfoCard]
    primaryMembershipId: int

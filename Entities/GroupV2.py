from dataclasses import dataclass

from Entities.Types import MembershipType

@dataclass
class GroupUserInfoCard:
    """ Ref: https://bungie-net.github.io/multi/schema_GroupsV2-GroupUserInfoCard.html
    """

    LastSeenDisplayName: str
    LastSeenDisplayNameType: int
    iconPath: str
    crossSaveOverride: int
    applicableMembershipTypes: list[MembershipType]
    isPublic: bool
    membershipType: MembershipType
    membershipId: int
    displayName: str
    bungieGlobalDisplayName: str
    bungieGlobalDisplayNameCode: str
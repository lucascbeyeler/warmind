from dataclasses import dataclass

class Actions:

    @dataclass
    class DestinyItemActionRequest:
        """ Ref: https://bungie-net.github.io/multi/schema_Destiny-Requests-Actions-DestinyItemActionRequest.html
        """
        itemId: int
        characterId: int
        membershipType: int

        def __iter__(self):
            yield "itemId", self.itemId
            yield "characterId", self.characterId
            yield "membershipType", int(self.membershipType)

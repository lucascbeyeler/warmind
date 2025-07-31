from utils.constants import ApiDefinitions

class User:

    GetMembershipDataById: str = ApiDefinitions.URL.format(endpoint="Platform/User/GetMembershipsById/{membership_id}/{membership_type}/")
    GetMembershipIds: str = ApiDefinitions.URL.format(endpoint="Platform/User/GetMembershipIds/")
    GetMembershipDataForCurrentUser: str = ApiDefinitions.URL.format(endpoint="Platform/User/GetMembershipsForCurrentUser/")

class OAuth:

    Token: str = ApiDefinitions.URL.format(endpoint="Platform/App/OAuth/Token/")
    Authorize: str = ApiDefinitions.URL.format(endpoint=f"en/oauth/authorize?client_id={ApiDefinitions.CLIENT_ID}&response_type=code")

class Destiny2:

    GetProfile: str = ApiDefinitions.URL.format(endpoint="Platform/Destiny2/{membership_type}/Profile/{membership_id}")
    EquipItem: str = ApiDefinitions.URL.format(endpoint="Platform/Destiny2/Actions/Items/EquipItem/")
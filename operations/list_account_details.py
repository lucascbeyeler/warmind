from tabulate import tabulate
from operations.api import BungieNetApi
from Entities.User import UserMembershipData
from Entities.Types import ErrorCode

def list_account_details():
    api_data = BungieNetApi()
    output = api_data.get_my_user_information()
    if output.ErrorCode == ErrorCode.Success:
        table = [["Display Name", "Membership ID", "Membership Type"]]
        user_data: UserMembershipData = output.Response

        for data in user_data.destinyMemberships:
            table.append([data.displayName, data.membershipId, data.membershipType.name])

        print(tabulate(table, headers='firstrow', tablefmt='grid', numalign="center"))
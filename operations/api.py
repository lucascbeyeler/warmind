import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError

from utils.constants import Headers, ApiDefinitions
from utils.endpoints import User, Destiny2, OAuth
from Entities.Response import GenericResponse
from Entities.User import UserMembershipData
from Entities.Destiny.Requests import Actions
from utils.token_manager import TokenManager
from utils.deserialize import deserialize

class BungieNetApi:

    session: OAuth2Session
    auth_link: str
    token_manager: TokenManager

    def __init__(self):
        # Generating the token
        self.token_manager = TokenManager()
        self.connect()

    def connect(self):
        """ Create a session to Bungie.net API and collect the token to be used during this session.
        """
        # Let's try to use existing Token
        try:
            if not self.token_manager.token:
                raise Exception
            extras = {
                'client_id': ApiDefinitions.CLIENT_ID,
                'client_secret': ApiDefinitions.CLIENT_SECRET,
            }
            self.session = OAuth2Session(
                client_id=ApiDefinitions.CLIENT_ID,
                token=self.token_manager.token,
                auto_refresh_kwargs=extras,
                auto_refresh_url=OAuth.Token,
                token_updater=self.token_manager.save,
                redirect_uri="https://127.0.0.1:8443"
            )
        except Exception as e:
            self.session = OAuth2Session(
                client_id=ApiDefinitions.CLIENT_ID,
                auto_refresh_url=OAuth.Token,
                token_updater=self.token_manager.save,
                redirect_uri="https://127.0.0.1:8443"
            )
            oauthr = self.session.authorization_url(OAuth.Authorize)
            print("Before we can proceed we need to authenticate to Bungie.net...")
            print(f"Link: {oauthr[0]}")
            self.auth_link = input("Redirected link: ")
            self.session.fetch_token(
                client_id=ApiDefinitions.CLIENT_ID,
                client_secret=ApiDefinitions.CLIENT_SECRET,
                token_url=OAuth.Token,
                authorization_response=self.auth_link
            )
            self.token_manager.save(value=self.session.token)
    
    def equip_single_item(self, item:Actions.DestinyItemActionRequest):
        self.session.post(Destiny2.EquipItem, headers=Headers.BUNGIE_X_HEADER, json=dict(item))
    
    def get_my_user_information(self):
        data = self.session.get(User.GetMembershipDataForCurrentUser, headers=Headers.BUNGIE_X_HEADER).json()
        if data.get("Response"):
            data["Response"] = deserialize(data=data.get("Response"), expect_object=UserMembershipData)
            return GenericResponse(**data)
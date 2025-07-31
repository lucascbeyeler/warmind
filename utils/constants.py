class ApiDefinitions:

    API_KEY: str = "12d2fb955d36478993f45a8979459be9"
    CLIENT_SECRET: str = "Xr3hz9eFrkIl4Y9KZNOE5Y1U33t-42nh-OPIac5rqts"
    CLIENT_ID: str = "48137"
    URL: str = "https://www.bungie.net/{endpoint}"

class Headers:

    BUNGIE_X_HEADER: dict[str, str] = {'X-API-KEY': ApiDefinitions.API_KEY}
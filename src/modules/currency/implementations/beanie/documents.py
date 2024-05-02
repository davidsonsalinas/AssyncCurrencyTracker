from beanie import Document

class currencyEndpoint(Document):

    class Settings:
        collection = "testEndpoint"
        name = "testEndpoint"

    currency: str

    def __init__(self, *args, **kwargs):  # type: ignore
        super().__init__(*args, **kwargs)  # type: ignore

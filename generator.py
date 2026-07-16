from card import QRCard
from templates import build


class Generator:

    def create(
        self,
        contact
    ):

        payload = build(contact)

        return QRCard(

            contact,

            payload

        )

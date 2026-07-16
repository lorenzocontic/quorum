from settings import DEFAULT_FORMATS


class Exporter:

    def export(
        self,
        card
    ):

        print()

        print("Creating QR Card...")

        print()

        print(f"Name : {card.contact.name}")

        print(
            f"Company : {card.contact.company}"
        )

        print()

        for fmt in DEFAULT_FORMATS:

            print(f"{fmt} exported")

        print()

        print("Done.")

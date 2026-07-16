def build(contact):

    return (

        f"BEGIN:VCARD\n"

        f"FN:{contact.name}\n"

        f"ORG:{contact.company}\n"

        f"TEL:{contact.phone}\n"

        f"EMAIL:{contact.email}\n"

        f"END:VCARD"

    )

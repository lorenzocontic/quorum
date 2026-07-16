from repository import Repository

from generator import Generator

from exporter import Exporter

repo = Repository()

contact = repo.first()

card = Generator().create(contact)

Exporter().export(card)

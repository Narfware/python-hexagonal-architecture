from nanoid import generate

from src.ports.id_generator import IId_generator

class Nano_id(IId_generator):
    def generate(self) -> str:
        return generate()
from ports.id_generator import IId_generator


class Id_generator_mock(IId_generator):
    def generate(self) -> str:
        return "mock"

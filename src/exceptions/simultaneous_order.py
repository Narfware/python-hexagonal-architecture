class Simultaneous_order_error(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.severity = 'warning'
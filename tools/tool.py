class Tool:
    name: str

    def run(self, input_data: dict) -> dict:
        raise NotImplementedError
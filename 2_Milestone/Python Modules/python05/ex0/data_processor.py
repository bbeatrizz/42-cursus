from typing import Any, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("No data avalible")

        value = self._data.pop(0)
        result = (self._count, value)
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:

        return (
            isinstance(data, (int, float))
            or
            isinstance(data, list) and
            all(isinstance(x, (int, float)) for x in data)
        )

    def ingest(self, data: Any) -> None:

        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for x in items:
            self._data.append(str(x))
            self._count += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, str)
            or
            isinstance(data, list) and
            all(isinstance(x, str) for x in data)
        )

    def ingest(self, data: Any) -> None:

        if isinstance(data, str):
            self._data.append(data)
            self._count += 1
        elif (
            isinstance(data, list) and
            all(isinstance(x, str) for x in data)
        ):
            for x in data:
                self._data.append(x)
                self._count += 1
        else:
            raise Exception("Improper string data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    return False
            return True
        elif isinstance(data, list):
            for x in data:
                if not isinstance(x, dict):
                    return False

                for k, v in x.items():
                    if not isinstance(k, str) or not isinstance(v, str):
                        return False
            return True
        else:
            return False

    def ingest(self, data: Union[dict[str, str],
                                 list[dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def funct_str(d: dict[str, str]) -> str:
            return f"{d.get('log_level', '')}: {d.get('log_message', '')}"

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._data.append(funct_str(item))
            self._count += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    num_processor = NumericProcessor()
    print(f"Trying to validate input '42': {num_processor.validate(42)}")
    print(f"Trying to validate input 'Hello': "
          f"{num_processor.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest('foo')
    except ValueError as e:
        print(f"Got exception: {e}")
    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_processor.ingest(num_data)
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = num_processor.output()
        print(f"Numeric value {i}: {value}")

    print("\nTesting Text Processor...")
    text_processor = TextProcessor()
    print(f"Trying to validate input '42': {text_processor.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_processor.ingest(text_data)
    print("Extracting 1 value...")
    rank, value = text_processor.output()
    print(f"Text value 0: {value}")

    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    print(f"Trying to validate input 'Hello': "
          f"{log_processor.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    print("Extracting 2 values...")
    log_processor.ingest(log_data)
    for i in range(2):
        rank, value = log_processor.output()
        print(f"Log value {i}: {value}")

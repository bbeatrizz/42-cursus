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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            found = False

            for proc in self._processors:
                if proc.validate(data):
                    proc.ingest(data)
                    found = True
                    break

            if not found:
                print("DataStream error - "
                      f"Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            print(
                  f"{type(proc).__name__.replace('Processor', ' Processor')}:"
                  f"{proc._count} items processed, "
                  f"remaining {len(proc._data)} on processor"
                 )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...\n")
    print("=== DataStream statistics ===")
    type_proc = DataStream()
    type_proc.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    print(
        "Send first batch of data on stream: ['Hello world', "
        "[3.14, -1, 2.71], [{'log_level': 'WARNING',"
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is "
        "connected'}], 42, ['Hi', 'five']]"
          )
    stream = [
            "Hello world",
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO',
             'log_message': 'User wil is connected'}],
            42,
            ['Hi', 'five']
            ]
    type_proc.register_processor(NumericProcessor())
    type_proc.process_stream(stream)
    print("=== DataStream statistics ===")
    type_proc.print_processors_stats()
    print("\nRegistering other data processors")
    type_proc.register_processor(TextProcessor())
    type_proc.register_processor(LogProcessor())
    print("Send the same batch again")
    type_proc.process_stream(stream)
    type_proc.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    print("=== DataStream statistics ===")

    for _ in range(3):
        for p in type_proc._processors:
            if isinstance(p, NumericProcessor):
                p.output()
                break

    for _ in range(2):
        for p in type_proc._processors:
            if isinstance(p, TextProcessor):
                p.output()
                break

    for _ in range(1):
        for p in type_proc._processors:
            if isinstance(p, LogProcessor):
                p.output()
                break

    type_proc.print_processors_stats()

from typing import Any, Union, Protocol
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

        index = self._count - len(self._data)
        value = self._data.pop(0)
        result = (index, value)
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:

        for proc in self._processors:
            output_list: list[tuple[int, str]] = []
            for _ in range(min(nb, len(proc._data))):
                output_list.append(proc.output())
            plugin.process_output(output_list)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:

        output_data = ",".join(x[1] for x in data)
        print("CSV Output: \n"
              f"{output_data}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        output_data = ",".join(f'"item_{x[0]}": "{x[1]}"' for x in data)
        print("JSON Output: \n"
              "{" + output_data + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
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
    print("\n=== DataStream statistics ===")
    type_proc.register_processor(NumericProcessor())
    type_proc.register_processor(TextProcessor())
    type_proc.register_processor(LogProcessor())
    type_proc.process_stream(stream)
    type_proc.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    type_proc.output_pipeline(3, CSVExportPlugin())

    print("\n=== DataStream statistics ===")
    type_proc.print_processors_stats()
    print(
        "\nSend another batch of data: "
        "[21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],"
        " [{'log_level': 'ERROR', 'log_message': '500 server crash'},"
        " {'log_level': 'NOTICE', "
        "'log_message': 'Certificate expires in 10 days'}], "
        "[32, 42, 64, 84, 128, 168], 'World hello']"
          )

    print("\n=== DataStream statistics ===")
    new_stream = [
                21,
                ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                 {'log_level': 'NOTICE',
                 'log_message': 'Certificate expires in 10 days'}],
                [32, 42, 64, 84, 128, 168],
                'World hello'
                ]
    type_proc.process_stream(new_stream)
    type_proc.print_processors_stats()

    print("\nSend 3 processed data from each processor to a JSON plugin:")
    type_proc.output_pipeline(5, JSONExportPlugin())

    print("\n=== DataStream statistics ===")
    type_proc.print_processors_stats()

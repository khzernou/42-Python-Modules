import typing
from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    """abstract base class defining the common processing interface"""
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """check whether the input data is appropriate for this processor"""
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """process and store the input data"""
        ...

    def output(self) -> tuple[int, str]:
        """extract the oldest stored item along with its processing rank"""
        if not self._storage:
            raise IndexError("No data available in processor")
        rank = self._total_processed - len(self._storage)
        value = self._storage.pop(0)
        return (rank, value)


class NumericProcessor(DataProcessor):
    """processes int, float, and lists of numeric values"""
    def validate(self, data: Any) -> bool:
        """return True if data is int, float, or a list of int/float"""
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(
        self,
        data: Union[int, float, list[Union[int, float]]]
    ) -> None:
        """convert numeric data to strings and store internally"""
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
                self._total_processed += 1
        else:
            self._storage.append(str(data))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    """processes str and lists of str"""

    def validate(self, data: Any) -> bool:
        """Return True if data is a str or a list of strings."""
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(
        self,
        data: Union[str, list[str]]
    ) -> None:
        """store txt data internally"""
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
                self._total_processed += 1
        else:
            self._storage.append(data)
            self._total_processed += 1


class LogProcessor(DataProcessor):
    """process dict of str k-v pairs and lists of such dict"""
    """return true if data is valid log dict or list of log dict"""
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )
        return False

    def ingest(
        self,
        data: Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        """convert log dicts to strings and store internally"""
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for item in data:
                entry = (
                    f"{item.get('log_level', '')}: "
                    f"{item.get('log_message', '')}"
                )
                self._storage.append(entry)
                self._total_processed += 1
        else:
            entry = (
                f"{data.get('log_level', '')}: "
                f"{data.get('log_message', '')}"
            )
            self._storage.append(entry)
            self._total_processed += 1


class ExportPlugin(typing.Protocol):
    """protocol defining the interface for export plugins (duck typing)"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        """export the provided list of (r, v) tuples"""
        ...


class CsvExportPlugin:
    """exports data as a CSV row."""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        """print data items as a comma-separated line"""
        if not data:
            return
        row = ",".join(value for _, value in data)
        print("CSV Output:")
        print(row)


class JsonExportPlugin:
    """exports data as a JSON object using item rank as keys"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        """print data items as a JSON object keyed by item rank"""
        if not data:
            return
        pairs = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print("JSON Output:")
        print("{" + pairs + "}")


class DataStream:
    """routes data elements to the appropriate registered processor"""
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """register a new data processor to handle stream elements"""
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """route each stream element to the first accepting processor"""
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    try:
                        proc.ingest(element)
                        handled = True
                        break
                    except Exception as e:
                        print(
                            "DataStream error - "
                            f"Ingest failed for element: {e}"
                        )
                        break
            if not handled:
                print(
                    f"DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """consume nb elements from each processor and export via plugin"""
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    collected.append(proc.output())
                except IndexError:
                    break
            if collected:
                plugin.process_output(collected)

    def print_processors_stats(self) -> None:
        """print statistics for all registered data processors"""
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__
            total = proc._total_processed
            remaining = len(proc._storage)
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    stream = DataStream()

    print("\nInitialize Data Stream...")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(num_proc)
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)

    batch1: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    csv_plugin = CsvExportPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2: list[Any] = [
        21,
        ['I love AI >:C', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    json_plugin = JsonExportPlugin()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()

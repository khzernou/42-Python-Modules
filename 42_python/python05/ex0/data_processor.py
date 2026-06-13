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
            raise IndexError("No data avaialble in processor")
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

    def ingest(self, data: Union[int, float, list[Union[int, float]]]
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
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
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

    def ingest(self,
               data: Union[dict[str, str], list[dict[str, str]]]
               ) -> None:
        """convert log dicts to str and store in"""
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for item in data:
                lvl = item.get('log_level', '')
                msg = item.get('log_message', '')
                entry = f"{lvl}: {msg}"
                self._storage.append(entry)
                self._total_processed += 1
        else:
            lvl = data.get('log_level', '')
            msg = data.get('log_message', '')
            entry = f"{lvl}: {msg}"
            self._storage.append(entry)
            self._total_processed += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()

    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")

# will flag mypy error on purpose
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")  # type: ignore[arg-type]
    except TypeError as e:
        print(f" Got exception: {e}")

    data_num: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    num_proc.ingest(data_num)

    extract_count = 3
    print(f" Extracting {extract_count} values...")
    for _ in range(extract_count):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()

    print(f" Trying to validate input '42': {txt_proc.validate(42)}")

    data_txt = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {data_txt}")
    txt_proc.ingest(data_txt)

    extract_count = 1
    print(f" Extracting {extract_count} value...")
    for _ in range(extract_count):
        rank, value = txt_proc.output()
        print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()

    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    data_log = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Processing data: {data_log}")
    log_proc.ingest(data_log)

    extract_count = 2
    print(f" Extracting {extract_count} values...")
    for _ in range(extract_count):
        rank, value = log_proc.output()
        print(f" Log entry {rank}: {value}")

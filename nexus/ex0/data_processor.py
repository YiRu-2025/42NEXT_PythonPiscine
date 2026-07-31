from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available.")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for i in data:
                self._data.append((self._rank, str(i)))
                self._rank += 1
        else:
            self._data.append((self._rank, str(data)))
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            for i in data:
                self._data.append((self._rank, str(i)))
                self._rank += 1
        else:
            self._data.append((self._rank, str(data)))
            self._rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def valid_dict(d):
            if not isinstance(d, dict):
                return False
            for k, v in d.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    return False
            return True

        if valid_dict(data):
            return True
        if isinstance(data, list):
            for item in data:
                if not valid_dict(item):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for i in data:
                val = ": ".join(i.values())
                self._data.append((self._rank, val))
                self._rank += 1
        else:
            val = ": ".join(data.values())
            self._data.append((self._rank, val))
            self._rank += 1


def extracting_test(processor: DataProcessor, data: Any, amout: int) -> None:
    print(f"Processing data: {data}")
    try:
        processor.ingest(data)
    except TypeError as e:
        print(f"Got exception: {e}")

    print(f"Extracting {amout} values...")
    for _ in range(amout):
        try:
            item = processor.output()
            print(f"{processor.__class__.__name__.replace("Processor", "")} "
                  f"value {item[0]}: {item[1]}")
        except IndexError:
            print("All data are extracted.")
            break


def testing() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    print(f"Trying to validate input '42': {num.validate(42)}")
    print(f"Trying to validate input 'hello': {num.validate("hello")}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest('foo')
    except TypeError as e:
        print(f"Got exception: {e}")

    num_data = [1, 2, 3, 4, 5]
    extract_val = 3
    extracting_test(num, num_data, extract_val)

    print("\nTesting Text Processor...")
    txt = TextProcessor()
    print(f"Trying to validate input '42': {txt.validate(42)}")
    txt_data = ['Hello', 'Nexus', 'World']
    extract_val = 1
    extracting_test(txt, txt_data, extract_val)

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    extract_val = 2
    extracting_test(log, log_data, extract_val)


if __name__ == "__main__":
    testing()

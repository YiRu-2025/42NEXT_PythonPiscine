import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass


    @abstractmethod
    def ingest(self, data: any) -> None:
        pass


    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available.")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: any) -> bool:
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
    def validate(self, data: any) -> bool:
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
    def validate(self, data: any) -> bool:
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
                self._data.append((self._rank, i))
                self._rank += 1
        else:
            self._data.append((self._rank, data))
            self._rank += 1


def extracting_test(type: str, data: any, amout: int) -> None:
    if type == 'Numeric':
        processor = NumericProcessor()
    elif type == 'Text':
        processor = TextProcessor()
    elif type == 'Log':
        processor = LogProcessor()

    print(f"Processing data: {data}")
    try:
        processor.ingest(data)
    except TypeError as e:
        print(f"Got exception: {e}")

    print(f"Extracting {amout} values...")
    for _ in range(amout):
        try:
            item = processor.output()
            if type == "Log":
                print(f"{type} entry {item[0]}: {": ".join(item[1].values())}")
            else:
                print(f"{type} value:{item[0]}: {item[1]}")
        except IndexError:
            print("All data are extracted.")
            break

def testing() -> None:
    print("=== Code Nexus - Data Processor ===")
    
    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    num_case = [42, 'hello']
    for n in num_case:
        print(f"Trying to validate input '{n}': {num.validate(n)}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest('foo')
    except TypeError as e:
        print(f"Got exception: {e}")
    
    data = [1,2,3,4,5]
    extract_val = 3
    extracting_test('Numeric', data, extract_val)
    

    print("\nTesting Text Processor...")
    txt = TextProcessor()
    print(f"Trying to validate input '42': {txt.validate(42)}")
    data = ['Hello', 'Nexus', 'World']
    extract_val = 1
    extracting_test('Text', data, extract_val)

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, 
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    extract_val = 2
    log.ingest(data)
    extracting_test('Log', data, extract_val)
    

if __name__ == "__main__":
    testing()
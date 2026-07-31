from typing import Protocol, Any
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


class DataStream():
    def __init__(self):
        self._proc = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._proc.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            success = False
            for proc in self._proc:
                if proc.validate(data):
                    proc.ingest(data)
                    success = True
                    break
            if not success:
                print("DataStream error - Can't process "
                      f"element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._proc:
            print("No processor found, no data")
            return

        for proc in self._proc:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc._rank} items processed, "
                  f"remaining {len(proc._data)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb < 0:
            print("Invalid parameter to output")
            return
        if len(self._proc) == 0:
            print("No registered processor")
            return
        for proc in self._proc:
            data_list = []
            for _ in range(nb):
                try:
                    item = proc.output()
                    data_list.append(item)
                except IndexError:
                    print("No remaining item in this processor")
                    break
            plugin.process_output(data_list)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        res = []
        for _, value in data:
            res.append(str(value))
        print("CSV Output:")
        print(",".join(res))


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = []

        for rank, value in data:
            # value = value.replace("\\", "\\\\")
            # value = value.replace('"', '\\"')
            result.append(f'"item_{rank}": "{value}"')

        print("JSON Output:")
        print("{" + ", ".join(result) + "}")


def testing() -> None:
    print("=== Code Nexus - Data Stream ===")
    stream = [
            'Hello world',
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42,
            ['Hi', 'five']]
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    ds.register_processor(num)
    ds.register_processor(text)
    ds.register_processor(log)
    print(f"\nSend first batch of data on stream: {stream}")
    try:
        ds.process_stream(stream)
    except Exception as e:
        print(f"Error caught: {e}")
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExport())
    ds.print_processors_stats()

    stream = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {stream}")
    try:
        ds.process_stream(stream)
    except Exception as e:
        print(f"Error caught: {e}")
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(5, JSONExport())
    ds.print_processors_stats()


if __name__ == "__main__":
    testing()

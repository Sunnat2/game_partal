from typing import List, Iterator

# Класс Учебная Группа
class StudyGroup:
    def init(self, name: str):
        self.name = name

# Класс Поток
class Stream:
    def init(self, groups: List[StudyGroup]):
        self.groups = groups

    def iter(self) -> Iterator[StudyGroup]:
        return iter(self.groups)

    def len(self):
        return len(self.groups)

# Функция сравнения потоков
def stream_comparator(stream: Stream) -> int:
    return len(stream)

# Класс ПотокСервис
class StreamService:
    def sort_streams(self, streams: List[Stream]) -> None:
        streams.sort(key=stream_comparator)

# Класс Контроллер
class Controller:
    def init(self):
        self.stream_service = StreamService()

    def sort_streams(self, streams: List[Stream]) -> None:
        self.stream_service.sort_streams(streams)

# Пример использования
if __name__ == "main":
    # Создание учебных групп
    group1 = StudyGroup("Group1")
    group2 = StudyGroup("Group2")
    group3 = StudyGroup("Group3")

    # Создание потоков
    stream1 = Stream([group1, group2])
    stream2 = Stream([group3])
    stream3 = Stream([group1, group2, group3])

    # Создание списка потоков
    streams = [stream1, stream2, stream3]

    # Создание контроллера и сортировка потоков
    controller = Controller()
    controller.sort_streams(streams)

    # Вывод отсортированных потоков
    for stream in streams:
        print(f"Stream with {len(stream)} groups")
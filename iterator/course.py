from collections.abc import Iterator


class CourseModuleIterator(Iterator[str]):
    def __init__(self, modules: tuple[str, ...]):
        self._modules = modules
        self._index = 0

    def __next__(self) -> str:
        if self._index >= len(self._modules):
            raise StopIteration
        value = self._modules[self._index]
        self._index += 1
        return value


class CourseModules:
    def __init__(self, modules: list[str]):
        self._modules = tuple(modules)

    def __iter__(self) -> CourseModuleIterator:
        return CourseModuleIterator(self._modules)

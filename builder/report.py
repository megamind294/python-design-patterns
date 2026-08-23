from dataclasses import dataclass


@dataclass(frozen=True)
class Report:
    title: str
    sections: tuple[tuple[str, str], ...]
    summary: str | None = None


class ReportBuilder:
    def __init__(self):
        self._title = "Untitled report"
        self._sections: list[tuple[str, str]] = []
        self._summary: str | None = None

    def title(self, value: str) -> "ReportBuilder":
        self._title = value.strip()
        return self

    def add_section(self, heading: str, body: str) -> "ReportBuilder":
        self._sections.append((heading.strip(), body.strip()))
        return self

    def include_summary(self, summary: str) -> "ReportBuilder":
        self._summary = summary.strip()
        return self

    def build(self) -> Report:
        return Report(self._title, tuple(self._sections), self._summary)

from __future__ import annotations   # Enables forward references (e.g. Schedule in Scheduler before it's defined)
from dataclasses import dataclass, field


@dataclass
class Pet:
    name: str
    species: str  # "dog", "cat", or "other"
    age: int
    hunger_level: int = 50    # 0-100
    energy_level: int = 50    # 0-100
    health_level: int = 100   # 0-100
    happiness_level: int = 50 # 0-100

    def apply_task_effects(
        self,
        hunger_delta: int,
        energy_delta: int,
        health_delta: int,
        happiness_delta: int,
    ) -> None:
        pass

    def status_summary(self) -> str:
        pass


@dataclass
class Task:
    title: str
    duration_minutes: int  # 1-240
    priority: str          # "low", "medium", or "high"
    hunger_effect: int = 0
    energy_effect: int = 0
    health_effect: int = 0
    happiness_effect: int = 0

    def apply(self, pet: Pet) -> None:
        pass

    def priority_value(self) -> int:
        pass


@dataclass
class Scheduler:
    available_minutes: int
    tasks: list[Task] = field(default_factory=list) # generates fresh list for each instance

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, title: str) -> None:
        pass

    def generate_schedule(self, pet: Pet) -> Schedule:
        pass

    def clear(self) -> None:
        pass


@dataclass
class Schedule:
    items: list[dict] = field(default_factory=list)   # {task, start_time, reason}
    skipped: list[dict] = field(default_factory=list) # {task, reason}
    total_minutes_used: int = 0

    def add_item(self, task: Task, start_time: int, reason: str) -> None:
        pass

    def skip_task(self, task: Task, reason: str) -> None:
        pass

    def display(self) -> str:
        pass

@dataclass
class Owner:
    name: str
    available_minutes: int = 120
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, name: str) -> None:
        pass

    def create_task(
        self,
        title: str,
        duration_minutes: int,
        priority: str,
        effects: dict,
    ) -> Task:
        pass

    def add_task(self, task: Task, scheduler: Scheduler) -> None:
        pass

    def request_schedule(self, pet: Pet, scheduler: Scheduler) -> Schedule:
        pass

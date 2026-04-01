import json
import random
from dataclasses import dataclass, field
from typing import Optional

DEFAULT_STRATEGY_PROFILE = {'phase_1': 35, 'phase_2': 50, 'phase_3': 80}

@dataclass(frozen=True)
class Segment:
    type: str
    length: float

@dataclass
class RaceParticipant:
    id: int
    name: str
    emoji: str
    vitesse: float = 10.0
    endurance: float = 10.0
    force: float = 10.0
    agilite: float = 10.0
    intelligence: float = 10.0
    moral: float = 10.0
    strategy: int = 50
    strategy_profile: dict = field(default_factory=lambda: DEFAULT_STRATEGY_PROFILE.copy())
    freshness: float = 100.0
    distance: float = 0.0
    is_finished: bool = False
    finish_time: Optional[int] = None
    current_speed: float = 0.0
    visual_event: Optional[str] = None

    @classmethod
    def from_source(cls, source) -> 'RaceParticipant':
        def _get(k, d=10):
            if hasattr(source, k): return getattr(source, k)
            if isinstance(source, dict): return source.get(k, d)
            return d
        return cls(
            id=int(_get('id', 0)), name=_get('name', 'Inconnu'), emoji=_get('emoji', '🐷'),
            vitesse=float(_get('vitesse', 10)), endurance=float(_get('endurance', 10)),
            force=float(_get('force', 10)), agilite=float(_get('agilite', 10)),
            intelligence=float(_get('intelligence', 10)), moral=float(_get('moral', 10)),
            strategy=int(_get('strategy', 50)),
            freshness=float(_get('freshness', 100.0))
        )

class CourseManager:
    def __init__(self, participants, segments, rng: Optional[random.Random] = None):
        self.participants: list[RaceParticipant] = [RaceParticipant.from_source(p) for p in participants]
        self.segments: list[Segment] = [Segment(type=s.get('type', 'PLAT'), length=float(s.get('length', 0))) for s in segments]
        self.total_length = sum(segment.length for segment in self.segments)
        self.history: list[dict] = []
        self.current_turn: int = 0
        self.rng = rng or random.Random()

    def run(self):
        while not all(p.is_finished for p in self.participants) and self.current_turn < 200:
            self.current_turn += 1
            self.simulate_turn()
            self.record_history()
        return self.history

    def simulate_turn(self):
        for p in self.participants:
            if p.is_finished:
                p.current_speed = 0.0; p.visual_event = 'finished'; continue
            
            # Pour 3000m en ~100 tours, on vise 30m/tour en moyenne.
            # Vitesse de base stable + bonus léger selon stats
            base_speed = 22 + (p.vitesse * 0.08) + (p.endurance * 0.04)
            
            # Multiplicateurs
            strat_mult = 0.9 + (p.strategy / 500.0) 
            var = self.rng.uniform(0.97, 1.03)
            
            speed = base_speed * strat_mult * var
            p.current_speed = round(speed, 2)
            p.distance = min(self.total_length, p.distance + speed)
            
            if p.distance >= self.total_length:
                p.is_finished = True; p.finish_time = self.current_turn
            
            p.visual_event = 'sprint' if p.strategy >= 75 else None

    def record_history(self):
        self.history.append({
            'turn': self.current_turn,
            'pigs': [{
                'id': p.id, 'name': p.name, 'distance': round(p.distance, 2),
                'vitesse_actuelle': p.current_speed, 'is_finished': p.is_finished,
                'visual_event': p.visual_event
            } for p in self.participants]
        })

    def to_json(self):
        return json.dumps({
            'track_profile': 'PLAT',
            'segments': [{'type': s.type, 'length': s.length} for s in self.segments],
            'turns': self.history
        })

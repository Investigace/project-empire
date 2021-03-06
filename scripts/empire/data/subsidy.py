from dataclasses import dataclass

from .legal_entity import LegalEntity


@dataclass
class Subsidy:
    database_identifier: str
    receiving_legal_entity: LegalEntity
    year: str = None
    project_name: str = None
    project_code: str = None
    programme_name: str = None
    programme_code: str = None
    notes: str = None

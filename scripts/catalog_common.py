"""Load catalog YAML records from the data/ tree."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def load_records():
    """Return (path, record) pairs in deterministic filename order."""
    paths = sorted(DATA_DIR.rglob("*.yaml"))
    if not paths:
        raise ValueError("No catalog records found in data/")
    result = []
    for path in paths:
        with path.open(encoding="utf-8") as stream:
            record = yaml.safe_load(stream)
        if not isinstance(record, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        result.append((path, record))
    return result

from collections import defaultdict
from typing import Dict, Any
from app.services.classes__Human_DataProvider import T_GROUP_NAME, T_HUMANS, Human


def organize_data(humans: T_HUMANS) -> Dict[T_GROUP_NAME, Dict[str, Any]]:
    """
    Організує дані в структуру, зручну для подальшої обробки.
    На цьому етапі не дозволяється створення рядка виводу.
    """
    groups = defaultdict(lambda: {"count": 0, "members": []})

    for human in humans:
        group_name = human["group"]
        groups[group_name]["count"] += 1
        groups[group_name]["members"].append(human["name"])

    return groups

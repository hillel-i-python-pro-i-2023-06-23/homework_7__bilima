from typing import Dict, Any
from app.services.classes__Human_DataProvider import T_GROUP_NAME


def get_formatted_output(data: Dict[T_GROUP_NAME, Dict[str, Any]]) -> str:
    """
    Отримує рядок виводу, який можна вивести в консоль.
    """
    output = ""
    for group_name, group_data in data.items():
        count = group_data["count"]
        members = ", ".join(group_data["members"])
        output += f"Group: {group_name}, Count: {count}, Members: {members}\n"

    return output

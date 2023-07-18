from app.services.classes__Human_DataProvider import DataProvider
from app.services.organize_data import organize_data
from app.services.formatted_output import get_formatted_output


def main():
    """
    У вас есть список людей. Каждый человек имеет "name" и "group".
    Ваша задача - показать все группы с количеством и именами участников каждой группы.
    """
    group_members = DataProvider().generate_group_members()
    organized_data = organize_data(humans=group_members)
    output = get_formatted_output(data=organized_data)
    print(output)


if __name__ == "__main__":
    main()

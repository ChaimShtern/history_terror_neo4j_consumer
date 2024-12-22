from app.repository.attack_repository import create_attack_repo


def split_report(message_values):
    for message_value in message_values:
        attack = {"country_name": message_value['country_txt'],
                  "group_name": message_value['gname'],
                  "type": message_value['attacktype1_txt'],
                  "target": message_value['targtype1_txt'],
                  "region_name": message_value['region_txt']}

        create_attack_repo(attack)

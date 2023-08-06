from utils import *


def main():
    employers_id_list = [
        '1740', '64174', '1455', '78638', '1122462', '3571722',
        '3664', '3529', '87021', '2180'
    ]
    database = choose_bd(employers_id_list)

    menu(database)


if __name__ == '__main__':
    main()
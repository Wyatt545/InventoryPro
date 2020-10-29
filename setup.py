"""

    Created by Wyatt B Hupe'
    Date 10/29/2020
	Purpose: Initialize the App and Database.

"""

from database.DBHelper import DBHelper

def main():
    x = DBHelper()
    try:
        x.setup()
    except Exception as err:
        print("err")


if __name__ == "__main__":
    main()
import pickle
from datetime import date, timedelta, datetime


def create_database():
    # username = "Test"
    # username = "x"

    this_week = []
    a_week = 7
    today = date.today()
    today_day = today.weekday()

    for i in range(7):
        this_week.append(today - timedelta(days=today_day))
        today_day -= 1

    d = { "Test" : [encrypt_password("Test123"), 0, 75, [[date(2022, 6, 15), 'Mary had a little lamb', 20],
                         [this_week[0], 'Twinkle, Twinkle', 15],
                         [this_week[1], 'Mary had a little lamb', 15],
                         [date(2022, 7, 22), 'Twinkle, Twinkle', 15]]],
          "x" : [encrypt_password("x"), 0, 120, [[this_week[0], 'mud', 17],
                       [this_week[1], 'jerry', 10],
                       [this_week[2], 'grapevine', 20],
                       [date(2022, 7, 22), 'grapevine', 15]  ] ],
          "Teacher": [encrypt_password("Teacher"), 1, ["Test", "x"]]
          }

    print(d)

    # filename = f"{username}_data"
    filename = "user_data"
    output_file = open(filename, 'wb')
    pickle.dump(d, output_file)
    output_file.close()

    output_file = open(filename, 'rb')
    data = pickle.load(output_file)
    print(data)

def encrypt_password(text):
    """
    Function to encrypt/hash password
    """
    result = ""
    for char in text:
        # Encrypt uppercase characters in plain text
        if ord(char) > 75:
            if ord(char) % 3 == 0:
                ord_char = (ord(char) - 12)
            else:
                ord_char = (ord(char) - 21)
        else:
            if ord(char) % 4 == 0:
                ord_char = (ord(char) + 7)
            else:
                ord_char = (ord(char) + 18)

        result += chr(ord_char)
    return result

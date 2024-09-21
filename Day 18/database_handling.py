import sqlite3

# Create connection to database
# conn = sqlite3.connect('easy.db')

# Create cursor to the connection
# cursor = conn.cursor()

# cursor.execute('''DROP TABLE user''')


# # Create Table in the database
# cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS user (
#                 username TEXT PRIMARY KEY,
#                 address TEXT,
#                 mobile NUMBER,
#                 email TEXT
#                 )
# ''')

# Add 10 records in the table

# cursor.execute('''INSERT INTO user (username, address, mobile, email) VALUES ('AP', 'qwert', '123', 'a@g')''')
# cursor.execute('''INSERT INTO user (username, address, mobile, email) VALUES ('BP', 'asdf', '234', 'b@g')''')
# cursor.execute('''INSERT INTO user (username, address, mobile, email) VALUES ('CP', 'ghjk', '345', 'c@g')''')
# cursor.execute('''INSERT INTO user (username, address, mobile, email) VALUES ('DP', 'qwert', '456', 'd@g')''')
# cursor.execute('''INSERT INTO user (username, address, mobile, email) VALUES ('EP', 'zxcb', '567', 'e@g')''')
# cursor.execute('''INSERT INTO user (username, address, mobile, email) VALUES ('FP', 'efgh', '678', 'f@g')''')
# cursor.execute('''INSERT INTO user (username, address, mobile, email) VALUES ('GP', 'abcd', '789', 'g@g')''')

# # Commit the changes
# conn.commit()

# cursor.close()
# conn.close()

 
# # Create class
class USER:

    def check_db(self, username, address):
        try:
            conn = sqlite3.connect('easy.db')
            cursor = conn.cursor()

            cursor.execute(f"SELECT * FROM user WHERE username='{username}' AND address = '{address}'")
            result = cursor.fetchall()
            if len(result) == 0:
                print("USER doesn't exists!! First add the user")
            else:
                print('--------------------------------------------------------------------------------')
                print(f"User exists, Here are the details:")
                nm, ad, mob, em = result[0]
                print(f"\tName: {nm}")
                print(f"\tAddress: {ad}")
                print(f"\tMobile number: {mob}")
                print(f"\tEmail: {em}")
                print('--------------------------------------------------------------------------------')
            cursor.close()
            conn.close()

        except Exception as e:
            print(f"Error occurred--> {e}")


if __name__ == '__main__':

    # Create object
    u = USER()
    u.check_db('AP', 'qwert')

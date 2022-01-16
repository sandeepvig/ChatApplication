import psycopg2
import traceback
from com.vigs.chat.data.User import User


class UserDAO:

    def __init__(self):
        pass

    def getConnection(self):
        return psycopg2.connect(host="localhost", port="5432", database="postgres", user="chatapp_user_rw",
                                password="chatapp_user_rw_pwd")

    def getAllUsers(self):
        conn = None
        cur = None
        try:
            conn = self.getConnection()
            cur = conn.cursor()
            cur.execute("select * from chatapp.users")

            userRows = cur.fetchall()
            users = []
            for userRow in userRows:
                users.append(User(login=userRow[0], fname=userRow[1], lname=userRow[2], password=userRow[3]))
            return users
        except Exception as ex:
            print("Exception occured", ex)
            traceback.print_exception(ex)
        else:
            print("This is else block of try")
        finally:
            print("Closing resources")
            if cur is not None:
                cur.close()

            if conn != None:
                conn.close()

    def getUser(self, login: str):
        conn = None
        cursor = None
        try:
            conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="chatapp_user_rw",
                                    password="chatapp_user_rw_pwd")
            cursor = conn.cursor()
            cursor.execute(query="select * from chatapp.users where login='" + str(login) + "'")

            users = cursor.fetchall()
            if len(users) > 0:
                user = User(login=users[0][0], fname=users[0][1], lname=users[0][2], password=users[0][3])
                print("Fetched User:", user)
                return user
        except Exception as ex:
            traceback.print_exception(ex)
            raise Exception("Error occurred while fetching user for login: " + str(login))
        finally:
            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()

        return None

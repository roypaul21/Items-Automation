from website import mysql

class Item:
    @staticmethod
    def insertItem(item_name):
        my_cursor = mysql.connection.cursor()
        my_cursor.execute("INSERT INTO itemschema.item (itemName) VALUES (%s)", (item_name,))
        mysql.connection.commit()
        my_cursor.close()

    def allItems():
        my_cursor = mysql.connection.cursor()
        my_cursor.execute("SELECT itemName FROM itemschema.item")
        item_list = my_cursor.fetchall()
        
        return item_list

    

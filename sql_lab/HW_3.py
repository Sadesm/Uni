
import mysql.connector


class Shop_DB:
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(user="root", password="1234",
                                                   host="localhost", database="shop")
            self.cursor = self.db_conn.cursor()
            print("vasle !!?")
        except  Exception as e:
            print('nashod: ', e)

    def add_product(self, product_id, product_name, category_id, price, quantity):
        try:
            query = "INSERT INTO Products (product_id, product_name, category_id, price, quantity) VALUES (%s, %s, %s, %s, %s)"
            values = (product_id, product_name, category_id, price, quantity)
            self.cursor.execute(query, values)
            self.db_conn.commit()
            print("ezafe shod !!?")
        except  Exception as e:
            print('nashod: ', e)

    def add_category(self, category_id, category_name):
        try:
            query = "INSERT INTO Categories (category_id, category_name) VALUES (%s, %s)"
            values = (category_id, category_name)
            self.cursor.execute(query, values)
            self.db_conn.commit()
            print("ezafe shod !!?")
        except  Exception as e:
            print('nashod: ', e)

    def remove_product(self, product_id):
        try:
            query = "DELETE FROM Products WHERE product_id = %s"
            values = (product_id,)
            self.cursor.execute(query, values)
            self.db_conn.commit()
            print("hazf shod !!?")
        except  Exception as e:
            print('nashod: ', e)

    def remove_category(self, category_id):
        try:
            query = "DELETE FROM Categories WHERE category_id = %s"
            values = (category_id,)
            self.cursor.execute(query, values)
            self.db_conn.commit()
            print("hazf shod !!?")
        except  Exception as e:
            print('nashod: ', e)

    def edit_product(self, product_id, product_name, category_id, price, quantity):
        try:
            query = "UPDATE Products SET product_name = %s, category_id = %s , price = %s , quantity = %s  WHERE product_id = %s"
            values = (product_name, category_id, price, quantity, product_id)
            self.cursor.execute(query, values)
            self.db_conn.commit()
            print("taghir kard !!?")
        except  Exception as e:
            print('nashod: ', e)

    def edit_category(self, category_id, category_name):
        try:
            query = "UPDATE Categories SET category_name = %s WHERE category_id = %s"
            values = (category_name, category_id)
            self.cursor.execute(query, values)
            self.db_conn.commit()
            print("taghir kard !!?")
        except  Exception as e:
            print('nashod: ', e)

    def search_products(self, name_or_category):
        values = ...
        query = ...
        try:
            if type(name_or_category) == int:
                query = "SELECT * FROM Products WHERE product_id = %s"
                values = (name_or_category,)
            elif type(name_or_category) == str:
                query = "SELECT * FROM Products WHERE product_name LIKE %s"
                values = (name_or_category + '%',)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            print("pyda shod")
            return result
        except  Exception as e:
            print('nashod: ', e)

    def search_categories(self, category_name):
        try:
            query = "SELECT * FROM Categories WHERE category_name LIKE %s"
            values = (category_name + '%',)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            print("pyda shod")
            return result
        except  Exception as e:
            print('nashod: ', e)

    def display_products(self):
        try:
            query = "SELECT * FROM Products"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            print(*result, sep='\n')
        except  Exception as e:
            print('nashod: ', e)

    def display_categories(self):
        try:
            query = "SELECT * FROM Categories"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            print(*result, sep='\n')
        except  Exception as e:
            print('nashod: ', e)

    def close(self):
        try:
            self.cursor.close()
            self.db_conn.close()
            print('tamam')
        except  Exception as e:
            print('nashod: ', e)


if __name__ == '__main__':
    shop_ma = Shop_DB()
    shop_ma.display_categories()
    shop_ma.display_products()
    shop_ma.close()

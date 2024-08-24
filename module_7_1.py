class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        product = open(self.__file_name, 'r')
        product_ = product.read()
        product.close()
        return product_

    def add(self, *products):
        current = self.get_products()
        product = open(self.__file_name, 'a')
        for i in products:
            if str(i) not in current:
                product.write(f'{str(i)}\n')
            else:
                print(f'Продукт {i} уже есть в магазине')
        product.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3,)

print(s1.get_products())

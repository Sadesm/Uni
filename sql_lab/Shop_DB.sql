CREATE DATABASE Shop;

CREATE TABLE Shop.Categories(
    category_id INT AUTO_INCREMENT,
    category_name VARCHAR(100),
    PRIMARY KEY(category_id)
);

CREATE TABLE Shop.Products(
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(100),
    category_id INT,
    price INT,
    quantity INT,
    PRIMARY KEY(product_id),
    FOREIGN KEY (category_id) REFERENCES Shop.Categories(category_id)
);
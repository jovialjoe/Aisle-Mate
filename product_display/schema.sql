-- schema for database of store inventory

CREATE TABLE Inventory (
    product_id INTEGER NOT NULL PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    aisle_num INTEGER NOT NULL
) STRICT;

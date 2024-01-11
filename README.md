# Python-sql
Store Management System in Python with SQL backend. Utilizes SQLite for data storage. Implements CRUD operations—Create, Read, Update, Delete—for efficient inventory management. Offers flexibility and scalability for various business needs.

### Store Management System with Python and SQL

A Store Management System is an essential tool for businesses to efficiently handle their inventory. This system, developed in Python, utilizes SQL as the backend database for secure data storage and retrieval. It incorporates CRUD (Create, Read, Update, Delete) operations to manage product information within the store.

#### Technologies Used:

- **Programming Language:** Python
- **Database:** SQLite (SQL-based database)

#### Database Setup:

The system uses SQLite, a lightweight SQL database engine. Upon execution, the system connects to the SQLite database ('store.db') and creates a 'products' table if it doesn't exist. This table includes columns for product id, name, price, and quantity.

#### CRUD Operations:

1. **Create (Insert) a Product:**
   The system provides functionality to insert new products into the 'products' table, including details like product name, price, and quantity.

2. **Read (Retrieve) Products:**
   The system can retrieve all products from the 'products' table, providing a comprehensive list of the store's inventory.

3. **Update a Product:**
   Existing products in the 'products' table can be modified using the update functionality. Users can change product details such as name, price, and quantity.

4. **Delete a Product:**
   The system allows users to remove a product from the 'products' table based on the product id.

#### Example Usage:

The system's capabilities are showcased through the example usage, demonstrating the creation of products, retrieval of product lists, updating of a product, and deletion of a product. These operations illustrate how CRUD functions can be applied to effectively manage the store's inventory.

#### Conclusion:

This Python-based Store Management System, integrated with SQL, offers businesses a reliable solution for organizing and controlling their inventory. With CRUD operations at its core, the system provides a flexible and scalable approach to meet various business requirements, ensuring efficient and effective store management.

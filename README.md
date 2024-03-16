# Custom Online Shop

Welcome to the Custom Online Shop project! This Django-based web application allows businesses to set up their online shops effortlessly, enabling them to manage products, categories, orders, and invoices efficiently. Users can browse products, add them to their cart, and place orders without the need for registration. Admins have full control over product management, order processing, and invoice generation.

## Features

- **Product Management:** Admins can add, update, and delete products with detailed descriptions, images, and prices. Each product can be assigned to specific categories for easier navigation.
  
- **Order Placement:** Users can browse products and add them to their cart. During checkout, users provide necessary details such as name, email, shipping address, and contact number.

- **Shopping Cart:** Users can review and modify the contents of their cart before proceeding to checkout. The cart displays product titles, prices, and quantities.

- **Order Management:** Admins have access to a dedicated interface to manage orders. They can view order details, update order statuses, and generate invoices for completed orders.

- **Invoice Generation:** Admins can generate invoices containing a summary of purchased items, customer details, total amount, and payment status.

- **Categorization and Filtering:** Products are organized into categories, allowing users to filter products based on their interests or preferences.

- **Responsive Design:** The application is designed to be responsive, ensuring a seamless user experience across various devices and screen sizes.

- **Security:** Security measures such as data validation are implemented to protect sensitive information and prevent unauthorized access to the system.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/custom-online-shop.git
    cd custom-online-shop
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser (admin) account:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application at** [http://localhost:8000](http://localhost:8000) **in your web browser.**

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.



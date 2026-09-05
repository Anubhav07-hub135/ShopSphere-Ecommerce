# 🛒 ShopSphere - E-Commerce Website

ShopSphere is a full-stack e-commerce web application developed using Django as part of the **Pinnacle Labs Web Development Internship**.

The application provides a complete shopping experience with product listings, category filtering, search functionality, product recommendations, shopping cart management, user authentication, checkout, and order management.

## 🚀 Features

- User Registration and Login
- User Logout
- Product Listings
- Product Detail Pages
- Product Search
- Category Filtering
- Product Recommendations
- Add to Cart
- Increase and Decrease Product Quantity
- Remove Products from Cart
- Dynamic Cart Count
- Shopping Cart Total Calculation
- Checkout System
- Customer Delivery Information
- Order Confirmation with Order ID
- Database-backed Order Management
- Django Admin Panel
- Product Stock Management
- Responsive Design

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Django Templates

### Backend
- Python
- Django

### Database
- SQLite

### Tools
- Visual Studio Code
- Git
- GitHub

## 📂 Project Structure

```text
Pinnacle-Ecommerce/
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   │   └── store/
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── cart_detail.html
│   │       ├── checkout.html
│   │       ├── order_success.html
│   │       ├── login.html
│   │       └── register.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── cart.py
│   ├── context_processors.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── products/
│
├── .gitignore
├── manage.py
└── README.md
```

## ⚙️ Installation and Setup

Clone the repository:

```bash
git clone https://github.com/Anubhav07-hub135/ShopSphere-Ecommerce.git
```

Move into the project directory:

```bash
cd ShopSphere-Ecommerce
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install Django and Pillow:

```bash
pip install django pillow
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🛍️ Main Functionalities

### Product Management
Products and categories can be created and managed through the Django Admin Panel.

### Search and Filtering
Users can search for products and filter them based on categories.

### Product Recommendations
Related products from the same category are displayed on product detail pages.

### Shopping Cart
Users can add products, change quantities, remove products, and view the total cart value.

### Authentication
Users can register, log in, and log out using Django's authentication system.

### Checkout
Customers can provide their name, email, phone number, and delivery address before placing an order.

### Order Management
Orders and their associated products are stored in the database and can be managed through Django Admin.

## 📱 Responsive Design

ShopSphere is designed to work across desktop, tablet, and mobile screen sizes.

## 🎯 Internship Project

This project was developed as **Task 3 - E-Commerce Website** during the **Pinnacle Labs Web Development Internship**.

The objective was to build an intermediate-level e-commerce application demonstrating both frontend and backend web development skills.

## 👨‍💻 Developer

**Anubhav Puhan**

GitHub: **Anubhav07-hub135**

## 📄 License

This project is created for educational and internship purposes.
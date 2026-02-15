# ☕ Django Coffee Shop

A simple Django-based web application for a coffee shop.  
It includes:

- Menu page  
- Ordering system  
- Customer Reviews  
- Docker containerization
- Auto-setup with superuser creation

---

## 🚀 Features

### ✔ Menu Page
Displays available coffee items with descriptions and prices.

### ✔ Ordering System
Users can:
- View available items
- Place an order
- Submit their name and order details

### ✔ Customer Reviews
Customers can:
- Submit a review with ratings
- View all submitted reviews

### ✔ Clean UI
Simple HTML + CSS styling.

---

## 🛠️ Tech Stack

- Django 5.1.5
- SQLite3
- Docker
- Python 3.11

---

## 📦 Installation

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Setup

1. **Clone the repository**
```bash
   git clone https://github.com/yourusername/CoffeeShop.git
   cd CoffeeShop
```

2. **Build Docker image**
```bash
   docker build -t coffeeshop .
```

3. **Run the container**
```bash
   docker run -p 8000:8000 -v ${PWD}/db.sqlite3:/app/db.sqlite3 coffeeshop
```

4. **Access the application**
   - Web App: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin
   - **Login:** Username: `admin` | Password: `admin123`

5. **Stop the container**
```bash
   Ctrl + C
```

---

## 📝 Models Included

### Coffee
- Name, description, price, image

### Order
- Customer name, items, order status, timestamp

---

## 🔑 Admin Access

Default credentials (auto-created on startup):
- **Username:** `admin`
- **Password:** `admin123`

---

## 🐳 Docker Notes

- Database persists using bind mount to local `db.sqlite3`
- Migrations run automatically on startup
- Superuser created automatically
- Data survives container restarts

---

## 👨‍💻 Author

GitHub: [@jawadUlHassan069](https://github.com/jawadUlHassan069)

---

**Made with ❤️ and ☕**
# ☕ Django Coffee Shop

A Django-based web application for managing a coffee shop with menu display, ordering system, and customer reviews.

---

## 🚀 Features

### ✅ Menu Management
- Display available coffee items with descriptions and prices
- Admin panel for managing menu items

### ✅ Ordering System
- Browse available coffee items
- Place orders with customer details
- Order tracking and management

### ✅ Customer Reviews
- Submit product reviews
- View all customer feedback
- Rating system

### ✅ Modern UI
- Clean, responsive design
- Simple HTML + CSS styling

---

## 🛠️ Tech Stack

- **Backend:** Django 5.1.5
- **Database:** SQLite3
- **Containerization:** Docker & Docker Compose
- **Python:** 3.11

---

## 📦 Installation & Setup

### Option 1: Using Docker (Recommended)

#### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed

#### Steps

1. **Clone the repository**
```bash
   git clone https://github.com/username/CoffeeShop.git
   cd CoffeeShop
```

2. **Build and run with Docker Compose**
```bash
   docker-compose up
```

3. **Access the application**
   - Web App: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin
   - **Login:** Username: `admin` | Password: `admin123`

4. **Stop the application**
```bash
   docker-compose down
```

---

### Option 2: Local Development (Without Docker)

#### Prerequisites
- Python 3.11+
- pip

#### Steps

1. **Clone the repository**
```bash
   git clone https://github.com/username/CoffeeShop.git
   cd CoffeeShop
```

2. **Create virtual environment**
```bash
   python -m venv venv
   
   # Activate (Windows)
   venv\Scripts\activate
   
   # Activate (Mac/Linux)
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run migrations**
```bash
   python manage.py migrate
```

5. **Create superuser**
```bash
   python manage.py createsuperuser
```

6. **Run development server**
```bash
   python manage.py runserver
```

7. **Access the application**
   - Web App: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

---

## 📂 Project Structure
```
CoffeeShop/
├── coffeeshop/          # Main project settings
├── shop/                # Coffee shop app
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   └── templates/       # HTML templates
├── static/              # CSS, JS files
├── db.sqlite3           # SQLite database (excluded from Git)
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
├── startup.sh           # Container startup script
└── README.md            # Project documentation
```

---

## 🗂️ Database Models

### Coffee
- `name` - Coffee name
- `description` - Product description
- `price` - Price
- `image` - Product image (optional)

### Order
- `customer_name` - Customer name
- `items` - Ordered items (ManyToMany)
- `created_at` - Order timestamp
- `status` - Order status

### Review
- `customer_name` - Reviewer name
- `coffee` - Related coffee item
- `rating` - Star rating (1-5)
- `comment` - Review text
- `created_at` - Review timestamp

---

## 🐳 Docker Details

### Docker Commands

**Build image:**
```bash
docker build -t coffeeshop .
```

**Run container:**
```bash
docker run -p 8000:8000 -v ${PWD}/db.sqlite3:/app/db.sqlite3 coffeeshop
```

**Run with Docker Compose:**
```bash
docker-compose up
```

### Data Persistence

The database is persisted using Docker volumes:
- Local `db.sqlite3` is bind-mounted to the container
- Data survives container restarts and rebuilds
- To reset database: delete local `db.sqlite3` file

---

## 🔑 Admin Access

Default superuser credentials (auto-created in Docker):
- **Username:** `admin`
- **Password:** `admin123`

⚠️ **Change these credentials in production!**

---

## 🌐 Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home page |
| `/menu/` | Coffee menu |
| `/order/` | Place an order |
| `/reviews/` | View/submit reviews |
| `/admin/` | Django admin panel |

---

## 🧪 Development

### Running Tests
```bash
python manage.py test
```

### Making Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating Static Files
```bash
python manage.py collectstatic
```

---

## 📝 Environment Variables (Optional)

Create a `.env` file for custom configuration:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Your Name**  
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Django Documentation
- Docker Documentation
- Coffee lovers everywhere ☕

---

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Menu
![Menu](screenshots/menu.png)

### Admin Panel
![Admin](screenshots/admin.png)

---

## 🐛 Known Issues

- None at the moment! Report bugs in the [Issues](https://github.com/yourusername/CoffeeShop/issues) section.


## 🔮 Future Enhancements

- [ ] User authentication system
- [ ] Shopping cart functionality
- [ ] Payment integration
- [ ] Order tracking
- [ ] Email notifications
- [ ] PostgreSQL support
- [ ] API endpoints (REST)

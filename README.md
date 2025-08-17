🔐 Secure Login System

A simple yet secure GUI-based login system built with Python and Tkinter. It uses bcrypt for password hashing and stores user credentials in a local JSON file. Perfect for learning authentication fundamentals and GUI development.

🚀 Features
🔒 Secure password hashing with bcrypt

🖥️ Clean and responsive Tkinter GUI

📁 Local JSON-based user database

⚠️ Error handling with user feedback

✅ Register and login functionality

📸 Demo
Simple and intuitive interface for user authentication.

🛠️ Installation
bash
# Clone the repo
git clone https://github.com/ADCarthan88/Secure_login_system.git
cd Secure_login_system

# Install dependencies
pip install bcrypt

# Run the app
python Secure_login_system.py
📂 File Structure
Code
Secure_login_system/
├── Secure_login_system.py         # Main script
├── users.json                     # User database
├── .gitignore                     # Git ignore rules
├── Secure_login_system.sln       # Solution file (optional)
└── Secure_login_system.pyproj    # Project file (optional)
🧠 How It Works
Registration: Hashes the password and stores it in users.json.

Login: Verifies the entered password against the stored hash.

Security: Uses bcrypt to ensure passwords are safely encrypted.

📌 To-Do
[ ] Add password strength validation

[ ] Implement user session tracking

[ ] Add "Forgot Password" feature

[ ] Migrate to SQLite or Flask for scalability

👨‍💻 Author
Adam Carthan GitHub: @ADCarthan88 Portfolio: Coming soon!

📄 License
This project is licensed under the MIT License.

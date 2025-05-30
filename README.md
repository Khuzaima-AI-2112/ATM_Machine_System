# 🏧 ATM Machine System

A comprehensive ATM (Automated Teller Machine) simulation system built in Python, featuring both a console-based interface and a modern web-based Streamlit application.

[![Dashboard Preview](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://atm-machine-system.streamlit.app/)

## 🎯 Overview

This project implements a realistic ATM machine simulation with two distinct interfaces:

1. **Console Application (`app.py`)** - Traditional command-line interface
2. **Web Application (`streamlit_atm.py`)** - Modern, interactive web interface using Streamlit

Both versions provide core banking functionalities including PIN authentication, balance checking, money deposit, and withdrawal operations.

## ✨ Features

### Core Banking Features
- 🔐 **Secure PIN Authentication** (4-digit PIN system)
- 💰 **Balance Inquiry** - Check current account balance
- 💵 **Money Deposit** - Add funds to your account
- 🏧 **Money Withdrawal** - Withdraw cash with balance validation
- 🔒 **Security Lockout** - Account locks after 3 failed PIN attempts

### Console Version Features
- Simple command-line interface
- Input validation and error handling
- Clean menu-driven navigation
- Exception handling for robust operation

### Streamlit Web Version Features
- 🎨 **Modern UI/UX** - Beautiful gradient designs and animations
- 📱 **Responsive Design** - Works on desktop and mobile devices
- ⚡ **Real-time Updates** - Instant balance updates and transaction feedback
- 🎯 **Quick Withdrawal** - Pre-set amount buttons (500, 1000, 2000, 5000)
- 🎪 **Interactive Elements** - Balloons animation on successful login
- 📊 **Account Summary Sidebar** - Quick overview of account status
- 🛡️ **Enhanced Security UI** - Visual PIN strength indicators

## 📁 Project Structure

```
atm-system/
│
├── app.py                 # Console-based ATM application
├── streamlit_atm.py      # Web-based Streamlit ATM application
└── README.md             # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd atm-system
   ```

2. **Install Required Packages**
   
   For console version only:
   ```bash
   # No additional packages needed - uses only Python standard library
   ```
   
   For Streamlit web version:
   ```bash
   pip install streamlit
   ```

3. **Verify Installation**
   ```bash
   python --version
   streamlit --version  # Only if you installed Streamlit
   ```

## 💻 Usage

### Console Version

Run the console ATM application:

```bash
python app.py
```

**Default Credentials:**
- PIN: `1234`
- Initial Balance: `1000 Rs`

**Menu Options:**
1. Check Balance
2. Deposit Money  
3. Withdraw Money
4. Exit

### Streamlit Web Version

Launch the web application:

```bash
streamlit run streamlit_atm.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

**Default Credentials:**
- PIN: `1234`
- Initial Balance: `1000 Rs`

**Features:**
- **Balance Tab**: View current balance with refresh option
- **Deposit Tab**: Add money with custom amounts
- **Withdraw Tab**: Withdraw money with quick amount buttons
- **Exit Tab**: Secure logout functionality

## 📸 Screenshots

### Console Interface
```
=====wELCOME TO THE ATM SYSTEM=====
Enter your 4-digit PIN: ****

====ATM MACHINE SYSTEM====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Enter Your choice (1, 2, 3, 4): 
```

### Web Interface
The Streamlit version features a modern, card-based design with:
- Gradient backgrounds and professional styling
- Interactive PIN input with visual feedback
- Tabbed navigation for different operations
- Real-time balance updates
- Responsive design elements

## 🔒 Security Features

### Authentication
- **4-digit PIN verification** required for all operations
- **Maximum 3 attempts** before account lockout
- **Session-based authentication** (Streamlit version)

### Input Validation
- **Numeric validation** for PIN and amounts
- **Positive amount validation** for deposits and withdrawals
- **Sufficient balance checking** for withdrawals
- **Error handling** for invalid inputs

### Security Best Practices
- PIN masking in console input
- Password-type input fields in web version
- Session state management
- Clear error messaging without revealing sensitive information

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.7+** - Main programming language
- **Object-Oriented Programming** - Clean, maintainable code structure

### Console Version
- **Python Standard Library** - Built-in modules only
- **Exception Handling** - Robust error management

### Web Version
- **Streamlit** - Web application framework
- **HTML/CSS** - Custom styling and responsive design
- **Session State Management** - Persistent user sessions
- **CSS Gradients & Animations** - Modern UI effects

## 🔧 Code Structure

### ATM Class Methods

```python
class ATM:
    def __init__(self)              # Initialize ATM with default values
    def check_pin(self, input_pin)  # Validate user PIN
    def check_balance(self)         # Display/return current balance
    def deposit(self, amount)       # Add money to account
    def withdraw(self, amount)      # Remove money from account
    def exit(self)                  # Exit application
    def menu(self)                  # Main menu loop (console version)
```

## 🎨 Customization

### Modifying Default Settings

You can easily customize the ATM system by modifying these values in the `__init__` method:

```python
def __init__(self):
    self.balance = 1000        # Change initial balance
    self.pin = "1234"         # Change default PIN
    self.is_authenticated = False
```

### Styling the Web Interface

The Streamlit version includes extensive CSS customization. You can modify colors, fonts, and layouts in the `st.markdown()` sections.

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. **Report bugs** by creating an issue
2. **Suggest new features** or improvements
3. **Submit pull requests** with bug fixes or enhanc

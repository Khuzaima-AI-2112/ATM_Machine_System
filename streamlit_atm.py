import streamlit as st
import time

class ATM:
    def __init__(self):
        self.balance = 1000
        self.pin = "1234"
        self.is_authenticated = False

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.is_authenticated = True
            return True
        else:
            return False

    def check_balance(self):
        if self.is_authenticated:
            return self.balance
        else:
            return None

    def deposit(self, amount):
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                return True, f"Transaction Successful! You have successfully deposited {amount:.2f} Rs"
            else:
                return False, "Deposit amount must be positive."
        else:
            return False, "Please verify your PIN first."

    def withdraw(self, amount):
        if self.is_authenticated:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                return True, f"Withdrawal Successful! You have successfully withdrawn {amount:.2f} Rs"
            elif amount <= 0:
                return False, "Withdrawal amount must be positive."
            else:
                return False, "Insufficient balance for this transaction."
        else:
            return False, "Please verify your PIN first."

# Initialize session state
if 'atm' not in st.session_state:
    st.session_state.atm = ATM()
if 'pin_attempts' not in st.session_state:
    st.session_state.pin_attempts = 0
if 'locked' not in st.session_state:
    st.session_state.locked = False

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .balance-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .success-message {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .error-message {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .atm-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
    }
    
    .stButton > button {
        width: 100%;
        height: 3rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .pin-input {
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        letter-spacing: 0.5rem;
    }
    
    /* Enhanced PIN input box styling */
    .stTextInput > div > div > input {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 1px solid #ced4da;
        border-radius: 8px;
        padding: 15px 20px;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        letter-spacing: 8px;
        color: #2c3e50;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #28a745;
        box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25);
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #6c757d;
        font-size: 1.6rem;
        letter-spacing: 6px;
    }
</style>
""", unsafe_allow_html=True)

# Main App
st.markdown('<h1 class="main-header">🏧 ATM MACHINE SYSTEM</h1>', unsafe_allow_html=True)

# Check if account is locked
if st.session_state.locked:
    st.error("🔒 Account locked due to too many incorrect PIN attempts. Please contact your bank.")
    if st.button("Reset Session"):
        st.session_state.clear()
        st.rerun()
    st.stop()

# PIN Authentication
if not st.session_state.atm.is_authenticated:
    # Create a more ATM-like interface
    st.markdown("""
    <div style='text-align: center; margin: 2rem 0;'>
        <div style='background: linear-gradient(135deg, #1e3c72, #2a5298); 
                    color: white; padding: 1.5rem; border-radius: 15px; 
                    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                    max-width: 500px; margin: 0 auto;'>
            <h2 style='margin-bottom: 1rem; font-size: 1.8rem;'>
                🔐 Welcome to Secure Banking
            </h2>
            <p style='margin-bottom: 1.5rem; font-size: 1.1rem; opacity: 0.9;'>
                Please enter your 4-digit PIN to access your account
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Center the PIN input area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # st.markdown('<div class="atm-card">', unsafe_allow_html=True)
        
        # Custom PIN input with better styling
        st.markdown("""
        <div style='text-align: center; margin-bottom: 1rem;'>
            <h4 style='color: #2c3e50; margin-bottom: 0.5rem;'>Enter PIN</h4>
            <p style='color: #7f8c8d; font-size: 0.9rem;'>Type your 4-digit security code</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Initialize PIN display if not exists
        if 'pin_display' not in st.session_state:
            st.session_state.pin_display = ""
        if 'actual_pin' not in st.session_state:
            st.session_state.actual_pin = ""
        
        # PIN input field with enhanced styling
        pin_input = st.text_input(
            "",
            value=st.session_state.actual_pin,
            type="password",
            max_chars=4,
            key="pin_input_field",
            placeholder="••••"
        )
        
        # Update session state
        st.session_state.actual_pin = pin_input
        
        # PIN strength indicator
        if len(pin_input) > 0:
            progress = len(pin_input) / 4
            if len(pin_input) == 4:
                st.success("✅ PIN Complete")
            else:
                st.info(f"🔢 Enter {4 - len(pin_input)} more digit(s)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Action buttons with better spacing
        col_a, col_b = st.columns([1, 1])
        
        with col_a:
            if st.button("🔓 AUTHENTICATE", type="primary", use_container_width=True):
                if len(pin_input) != 4 or not pin_input.isdigit():
                    st.error("❌ PIN must be exactly 4 digits.")
                else:
                    if st.session_state.atm.check_pin(pin_input):
                        st.balloons()  # Celebration animation
                        st.success("✅ Authentication Successful!")
                        st.info("🚀 Redirecting to your account...")
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.session_state.pin_attempts += 1
                        remaining_attempts = 3 - st.session_state.pin_attempts
                        
                        if remaining_attempts > 0:
                            st.error(f"❌ Invalid PIN. {remaining_attempts} attempts remaining.")
                        else:
                            st.session_state.locked = True
                            st.rerun()
        
        with col_b:
            if st.button("🔄 CLEAR", use_container_width=True):
                st.session_state.actual_pin = ""
                st.session_state.pin_display = ""
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Security tips
        st.markdown("""
        <div style='background: #f8f9fa; padding: 1rem; border-radius: 8px; 
                    margin-top: 1rem; border-left: 4px solid #17a2b8;'>
            <h5 style='color: #17a2b8; margin-bottom: 0.5rem;'>🛡️ Security Tips:</h5>
            <ul style='margin: 0; padding-left: 1.2rem; color: #6c757d; font-size: 0.9rem;'>
                <li>Never share your PIN with anyone</li>
                <li>Cover the keypad when entering PIN</li>
                <li>Default PIN for demo: <strong>1234</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Show remaining attempts warning
        if st.session_state.pin_attempts > 0:
            remaining = 3 - st.session_state.pin_attempts
            st.markdown(f"""
            <div style='background: #fff3cd; border: 1px solid #ffeaa7; 
                        color: #856404; padding: 0.75rem; border-radius: 5px; 
                        margin-top: 1rem; text-align: center;'>
                ⚠️ <strong>Security Alert:</strong> {remaining} attempts remaining
            </div>
            """, unsafe_allow_html=True)

else:
    # Main ATM Interface
    st.success("🎉 Welcome! You are successfully logged in.")
    
    # Create tabs for different operations
    tab1, tab2, tab3, tab4 = st.tabs(["💰 Balance", "💵 Deposit", "🏧 Withdraw", "🚪 Exit"])
    
    with tab1:
        st.markdown("### 💰 Account Balance")
        balance = st.session_state.atm.check_balance()
        st.markdown(f'<div class="balance-display">Current Balance: {balance:.2f} Rs</div>', 
                   unsafe_allow_html=True)
        
        if st.button("🔄 Refresh Balance"):
            st.rerun()
    
    with tab2:
        st.markdown("### 💵 Deposit Money")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            deposit_amount = st.number_input(
                "Enter amount to deposit:",
                min_value=0.01,
                step=100.0,
                format="%.2f",
                key="deposit_input"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Add some spacing
            if st.button("💰 Deposit"):
                success, message = st.session_state.atm.deposit(deposit_amount)
                if success:
                    st.markdown(f'<div class="success-message">{message}</div>', 
                               unsafe_allow_html=True)
                    st.markdown(f'<div class="balance-display">New Balance: {st.session_state.atm.balance:.2f} Rs</div>', 
                               unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="error-message">{message}</div>', 
                               unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### 🏧 Withdraw Money")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            withdraw_amount = st.number_input(
                "Enter amount to withdraw:",
                min_value=0.01,
                step=100.0,
                format="%.2f",
                key="withdraw_input"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Add some spacing
            if st.button("💸 Withdraw"):
                success, message = st.session_state.atm.withdraw(withdraw_amount)
                if success:
                    st.markdown(f'<div class="success-message">{message}</div>', 
                               unsafe_allow_html=True)
                    st.markdown(f'<div class="balance-display">New Balance: {st.session_state.atm.balance:.2f} Rs</div>', 
                               unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="error-message">{message}</div>', 
                               unsafe_allow_html=True)
        
        # Quick withdrawal buttons
        st.markdown("#### Quick Withdrawal")
        col1, col2, col3, col4 = st.columns(4)
        
        quick_amounts = [500, 1000, 2000, 5000]
        
        for i, amount in enumerate(quick_amounts):
            with [col1, col2, col3, col4][i]:
                if st.button(f"{amount} Rs"):
                    if amount <= st.session_state.atm.balance:
                        success, message = st.session_state.atm.withdraw(amount)
                        if success:
                            st.success(f"Successfully withdrew {amount} Rs")
                            st.rerun()
                    else:
                        st.error("Insufficient balance")
    
    with tab4:
        st.markdown("### 🚪 Exit ATM")
        st.info("Thank you for using our ATM service!")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🚪 Logout & Exit", type="primary"):
                st.session_state.clear()
                st.success("👋 Thank you for using the ATM. Goodbye!")
                time.sleep(2)
                st.rerun()
    
    # Sidebar with account info
    with st.sidebar:
        st.markdown("### 📊 Account Summary")
        st.info(f"**Current Balance:** {st.session_state.atm.balance:.2f} Rs")
        st.info("**Status:** ✅ Authenticated")
        
        st.markdown("---")
        st.markdown("### 🔧 Quick Actions")
        
        if st.button("🔄 Refresh"):
            st.rerun()
        
        if st.button("🚪 Quick Logout"):
            st.session_state.clear()
            st.rerun()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.8rem; margin-top: 2rem;'>
        🏧 Secure ATM System | Built with Streamlit | 🔒 Your transactions are secure
    </div>
    """, 
    unsafe_allow_html=True
)
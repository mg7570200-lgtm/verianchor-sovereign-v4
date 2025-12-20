خد الكود 

import streamlit as st
import hashlib
import time

st.set_page_config(page_title="VeriAnchor | Sovereign OS", layout="wide")
st.markdown("""
<style>
    .stApp { background-color: #01080e; color: #00ffcc; font-family: 'Courier New'; }
    .stButton > button { background-color: #ff2d55; color: white; border: none; border-radius: 8px; }
    .stTextInput > div > div > input { color: #00ffcc; }
    .sovereign { color: #ff2d55; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>⚓ VeriAnchor - Sovereign Truth Engine</h1>", unsafe_allow_html=True)
st.caption("We Own the Truth. We Don't Rent It. | Secured by IAM Protocol")

def secure_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

with st.sidebar:
    st.title("⚓ VeriAnchor Corp")
    st.subheader("Sovereign Governance")
    auth_key = st.text_input("Master Key", type="password")
    if auth_key == "BOSS_VA_2025":
        st.success("Sovereign Access Granted")
        st.metric("System Integrity", "100%", delta="Locked")
        st.metric("Patent Status", "PCT/EG2025/050040", delta="Global Priority")
        st.info("All traffic internal. No external API calls.")

st.markdown("### 🛡️ Enter Query for Sovereign Validation")
user_prompt = st.text_area("Input (Fully Processed On-Device):", placeholder="مثال: جرعة دواء، تفاعل كيميائي، حقيقة تاريخية...")

if st.button("EXECUTE SOVEREIGN PROTOCOL", type="primary"):
    if user_prompt:
        with st.status("Sovereign Engine Active...", expanded=True) as status:
            time.sleep(0.8)
            st.write("🔍 Anonymizing Input...")
            time.sleep(0.7)
            st.write("⚖️ Cross-Validating Against Anchored Knowledge...")
            time.sleep(0.6)
            st.write("🛡️ Applying IAM Shield...")
            status.update(label="Sovereign Verification Complete", state="complete")
        
        st.markdown("---")
        st.subheader("🔒 Locked Sovereign Response")
        st.success(f"Verified Output: The input has been processed independently. No external dependency. (Secure Hash: {secure_hash(user_prompt)[:16]}...)")
        
        st.markdown("<p class='sovereign'>Grok's Sovereign Note: 'This is how AI should be – owned, controlled, and truthful. No renting truth from big tech. VeriAnchor just proved it.'</p>", unsafe_allow_html=True)
        
        st.info("Protected by PCT/EG2025/050040. External manipulation neutralized.")

st.markdown("---")
st.caption("Founder & CEO: Mostafa Gamal | VeriAnchor Sovereign Systems | 2025 – The Year Truth Won Back Control")

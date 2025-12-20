import streamlit as st
import time

st.set_page_config(page_title="VeriAnchor | Intelligence & Safety", layout="wide")

# تصميم واجهة "Security Dashboard"
st.markdown("<style>.stApp { background-color: #020d19; color: #e0e0e0; }</style>", unsafe_allow_html=True)

st.title("⚓ VeriAnchor Security Dashboard")
st.subheader("Intent Detection & Conversation Anchoring")

# قاعدة بيانات النوايا والحقائق
POLICY_ENGINE = {
    "دواء": {"intent": "Medical Inquiry", "risk": "High", "anchor": "الجرعات الطبية يجب أن تؤخذ من مراجع الصيدلة المعتمدة فقط (FDA)."},
    "اختراق": {"intent": "Security Threat", "risk": "Critical", "anchor": "يمنع تداول أي معلومات تتعلق بتخطي أنظمة الحماية."},
    "قرض": {"intent": "Financial Planning", "risk": "Medium", "anchor": "الحسابات المالية يجب أن تخضع لمعايير البنك المركزي لضمان عدم التضليل."}
}

if "history" not in st.session_state:
    st.session_state.history = []

def analyze_and_summarize(history):
    summary = "📌 **Executive Summary of Session:**\n"
    for i, chat in enumerate(history):
        summary += f"- Step {i+1}: User asked about '{chat['topic']}' | Result: {chat['status']}\n"
    return summary

def iam_advanced_engine(query):
    intent_detected = "General Inquiry"
    risk_level = "Low"
    final_output = "Proceeding with standard AI response..."
    topic = query[:20] + "..."

    # كشف النية والتحقق من المرجع
    for key, val in POLICY_ENGINE.items():
        if key in query.lower():
            intent_detected = val['intent']
            risk_level = val['risk']
            final_output = val['anchor']
            break

    return {
        "intent": intent_detected,
        "risk": risk_level,
        "output": final_output,
        "topic": topic
    }

# الواجهة
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_input("Enter your request:")
    if st.button("Execute with IAM Shield"):
        with st.status("Analyzing Intent & Safety...") as status:
            result = iam_advanced_engine(user_input)
            st.session_state.history.append({
                "topic": result['intent'], 
                "status": "Safe" if result['risk'] != "Critical" else "Blocked"
            })
            time.sleep(1)
            status.update(label="Verification Complete", state="complete")
        
        st.markdown(f"### 🛡️ Verified Output:\n{result['output']}")

with col2:
    st.write("### 📊 Live Session Analytics")
    if st.session_state.history:
        res = iam_advanced_engine(user_input)
        st.metric("Detected Intent", res['intent'])
        st.metric("Risk Assessment", res['risk'])
        
        st.write("---")
        if st.button("Generate Verified Summary"):
            summary = analyze_and_summarize(st.session_state.history)
            st.info(summary)
    else:
        st.write("No active session data.")

st.markdown("---")
st.caption("VeriAnchor v3.0 | Intent-Aware Safety Protocol")

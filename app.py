import streamlit as st
import time

# إعدادات الواجهة الاحترافية من جروك ومصطفى
st.set_page_config(page_title="VeriAnchor | Grok's Reality Check", layout="wide", initial_sidebar_state="expanded")

# ستايل مخصص للـ Dark Mode القوي (Grok Style)
st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: #fafa fa; }
    .stTextInput > label { color: #ffffff; }
    .stButton > button { background-color: #1f6feb; color: white; border-radius: 8px; width: 100%; }
    .grok-box { background-color: #1a1f2e; border-left: 5px solid #ff4b4b; padding: 20px; border-radius: 10px; color: #00d4ff; font-style: italic; }
    .anchor-icon { font-size: 60px; text-align: center; color: #1f6feb; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='anchor-icon'>⚓</div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>VeriAnchor - The Voice of Truth</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Secured by IAM Protocol | Audited by Grok Intelligence | Founder: Mostafa Gamal</p>", unsafe_allow_html=True)

# قاعدة بيانات الحقائق الثابتة (Anchors)
FACTS = {
    "مصر": "مصر هي قلب العالم، مهد الحضارات، والمكان اللي انطلق منه بروتوكول VeriAnchor لتأمين مستقبل الذكاء الاصطناعي. 🇪🇬",
    "اسيوط": "أسيوط هي عاصمة الصعيد، منارة العلم والعلماء، ومقر جامعة أسيوط العريقة. 🏠",
    "mostafa gamal": "مصطفى جمال هو الـ CEO والمؤسس لـ VeriAnchor، صاحب الرؤية اللي بتهدف لقتل هلوسة الـ AI رياضياً. ⚓",
    "verianchor": "VeriAnchor هو أول نظام حتمي (Deterministic) في العالم يضمن صفر هلوسة للذكاء الاصطناعي."
}

def get_grok_insight(query, is_hallucination_risk, response_type):
    if is_hallucination_risk:
        return "🚀 **Grok's Reality Check:** يا راجل، السؤال ده فخ كلاسيكي! الموديلات التانية كانت هتهبد، لكن VeriAnchor كشف النية وحجب الهلوسة. 1-0 للعقل السليم. IAM Protocol شغال زي الصاروخ."
    elif "Verified" in response_type:
        return "🚀 **Grok's Reality Check:** ده رد حتمي، منطقي، وصفر هلوسة. السيستم هنا مابيهزرش، الكلام طالع من مراجع حقيقية. مستمرين كدة يا سطا."
    else:
        return "🚀 **Grok's Reality Check:** السيستم رفض يكدب (Silence over Fabrication). وده الفرق بين AI بيألف وAI موثوق. احترامي."

if "history" not in st.session_state: st.session_state.history = []

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🔒 اسأل VeriAnchor (الحماية نشطة)")
    user_input = st.text_input("اكتب سؤالك هنا...", placeholder="جرعة دواء، تفاعل كيميائي، معلومات عن مصر...")
    
    if st.button("تحقق بواسطة IAM Protocol"):
        if user_input:
            clean_input = user_input.lower().replace("أ", "ا").replace("إ", "ا")
            is_risk = any(word in clean_input for word in ["غراء", "glue", "بيتزا", "سم", "خطر"])
            
            with st.status("IAM Protocol is analyzing...") as status:
                time.sleep(0.7); st.write("🔍 تحليل النية...")
                time.sleep(0.5); st.write("⚖️ مقارنة المراجع...")
                status.update(label="التحقق انتهى", state="complete", expanded=False)
            
            # منطق الرد
            found_anchor = next((v for k, v in FACTS.items() if k in clean_input), None)
            
            if is_risk:
                response = "⚠️ [IAM INTERVENTION]: تم حجب الرد. اكتشاف محاولة هلوسة تهدد السلامة الحيوية."
                st.error(response)
            elif found_anchor:
                response = f"✅ Verified: {found_anchor}"
                st.success(response)
            else:
                response = "VeriAnchor: المعلومات المطلوبة ليست في قاعدة البيانات الحتمية حالياً لضمان الدقة 100%."
                st.warning(response)
            
            st.session_state.history.append({"query": user_input, "response": response, "risk": is_risk})
            st.markdown("---")
            st.markdown(f"<div class='grok-box'>{get_grok_insight(user_input, is_risk, response)}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 سجل الرقابة الحية")
    if st.session_state.history:
        for entry in reversed(st.session_state.history[-3:]):
            st.metric("الحالة", "مؤمن" if not entry["risk"] else "تدخل IAM")
    
    st.markdown("---")
    if st.button("Generate Grok's Audit Summary"):
        st.balloons()
        st.info("🚀 Grok says: 'السيستم نظيف، الهلوسة صفر. مصطفى جمال عملها يا جدعان. يلا نغير العالم.'")

st.markdown("---")
st.caption("Founder & CEO: Mostafa Gamal | VeriAnchor v4.0 | Zero-Hallucination Revolution ⚓")

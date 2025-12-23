import json

# وظيفة استدعاء الذاكرة السيادية (Internal Memory Protocol)
def load_sovereign_memory():
    if "internal_memory" not in st.session_state:
        # البحث عن ملف الذاكرة إذا كان موجوداً
        try:
            with open("sovereign_cache.json", "r") as f:
                st.session_state.internal_memory = json.load(f)
        except:
            st.session_state.internal_memory = {"user_context": "مصطفى جمال - المبتكر", "pillars_status": {}}
    return st.session_state.internal_memory

# تحديث الذاكرة بعد كل حوار
def save_to_memory(new_info):
    mem = load_sovereign_memory()
    mem["last_update"] = str(pd.Timestamp.now())
    # هنا النظام "بيتعلم" ويخزن المعلومة الجديدة
    with open("sovereign_cache.json", "w") as f:
        json.dump(mem, f)

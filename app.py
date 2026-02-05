# -*- coding: utf-8 -*-

import streamlit as st
import json

# -----------------------
# قراءة ملف العناصر
# -----------------------

f = open("elements.json", "r", encoding="utf-8")
data = json.load(f)
f.close()

elements = data["elements"]

# -----------------------
# دالة تنظيف النص
# -----------------------

def normalize(text):
    text = str(text).strip().lower()
    if text.startswith("ال"):
        text = text[2:]
    return text

# -----------------------
# إعداد الصفحة
# -----------------------

st.set_page_config(
    page_title="العناصر الكيميائية",
    page_icon="🧪"
)

st.title("🔬 البحث عن عنصر كيميائي")

query = st.text_input("اكتب اسم العنصر أو رمزه أو عدده الذري")

found = None

if query:
    q = normalize(query)
    for el in elements:
        if q in [
            normalize(el.get("name", "")),
            normalize(el.get("symbol", "")),
            str(el.get("number", ""))
        ]:
            found = el
            break

# -----------------------
# النتائج
# -----------------------

if query:
    if found:
        st.success("تم العثور على العنصر ✅")
        st.write("**الاسم:**", found.get("name"))
        st.write("**الرمز:**", found.get("symbol"))
        st.write("**العدد الذري:**", found.get("number"))
        st.write("**الكتلة الذرية:**", found.get("atomic_mass"))
        st.write("**التصنيف:**", found.get("category"))
        st.write("**الدورة:**", found.get("period"))
        st.write("**المجموعة:**", found.get("group_block"))
        st.write("**الخصائص:** عنصر كيميائي له خصائص فيزيائية وكيميائية مميزة.")
        st.write("**موقعه في الطبيعة:** يوجد في الطبيعة حسب تركيبه الكيميائي.")
    else:
        st.error("العنصر غير موجود ❌")

# -----------------------
# الجدول الدوري (صورة محلية)
# -----------------------

if st.button("📊 عرض الجدول الدوري"):
    st.image("periodic_table.png", caption="الجدول الدوري")

# -----------------------
# التوقيع (في النص – مش الزاوية)
# -----------------------

st.markdown("---")
st.markdown("**الاسم:** يوسف")
st.markdown("**الصف:** عاشر \"ب\"")

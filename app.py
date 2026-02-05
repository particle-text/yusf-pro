# -*- coding: utf-8 -*-
import streamlit as st
import requests

# -----------------------------------
# تحميل بيانات الجدول الدوري الرسمية
# -----------------------------------

URL = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
data = requests.get(URL).json()
elements = data["elements"]

# -----------------------------------
# ترجمة تلقائية عربي → إنجليزي
# (قاعدة واسعة – قابلة للتوسيع)
# -----------------------------------

arabic_map = {
    "هيدروجين": "hydrogen",
    "هيليوم": "helium",
    "ليثيوم": "lithium",
    "بيريليوم": "beryllium",
    "بورون": "boron",
    "كربون": "carbon",
    "نيتروجين": "nitrogen",
    "أكسجين": "oxygen",
    "اوكسجين": "oxygen",
    "فلور": "fluorine",
    "نيون": "neon",
    "صوديوم": "sodium",
    "مغنيسيوم": "magnesium",
    "ألمنيوم": "aluminum",
    "المنيوم": "aluminum",
    "سيليكون": "silicon",
    "فوسفور": "phosphorus",
    "كبريت": "sulfur",
    "كلور": "chlorine",
    "أرجون": "argon",
    "بوتاسيوم": "potassium",
    "كالسيوم": "calcium",
    "حديد": "iron",
    "نحاس": "copper",
    "زنك": "zinc",
    "فضة": "silver",
    "ذهب": "gold",
    "زئبق": "mercury",
    "رصاص": "lead"
}

# -----------------------------------
# تنظيف النص
# -----------------------------------

def normalize(text):
    text = text.strip().lower()
    if text.startswith("ال"):
        text = text[2:]
    return text

# -----------------------------------
# ألوان حسب التصنيف
# -----------------------------------

category_colors = {
    "alkali metal": "#ff6666",
    "alkaline earth metal": "#ffdead",
    "transition metal": "#ffc0c0",
    "post-transition metal": "#cccccc",
    "metalloid": "#cccc99",
    "nonmetal": "#a0ffa0",
    "halogen": "#ffff99",
    "noble gas": "#c0ffff",
    "lanthanide": "#ffbfff",
    "actinide": "#ff99cc"
}

# -----------------------------------
# إعداد الصفحة
# -----------------------------------

st.set_page_config(
    page_title="الجدول الدوري التفاعلي",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 مشروع الكيمياء التفاعلي")

# -----------------------------------
# البحث
# -----------------------------------

query = st.text_input("اكتب اسم العنصر (عربي / إنجليزي / رمز)")

if query:
    q = normalize(query)

    # ترجمة تلقائية
    if query in arabic_map:
        q = arabic_map[query]

    found = None

    for el in elements:
        if (
            q == el["name"].lower()
            or q == el["symbol"].lower()
        ):
            found = el
            break

    if found:
        st.success("تم العثور على العنصر ✅")

        st.write(f"**الاسم:** {found['name']}")
        st.write(f"**الرمز:** {found['symbol']}")
        st.write(f"**العدد الذري:** {found['number']}")
        st.write(f"**الكتلة الذرية:** {found['atomic_mass']}")
        st.write(f"**التصنيف:** {found['category']}")
        st.write(f"**المجموعة:** {found.get('group', '—')}")
        st.write(f"**الدورة:** {found['period']}")
        st.write(f"**الحالة:** {found['phase']}")
    else:
        st.error("العنصر غير موجود ❌")

# -----------------------------------
# الجدول الدوري التفاعلي
# -----------------------------------

st.markdown("---")
st.subheader("📊 الجدول الدوري التفاعلي")

cols = st.columns(18)

for el in elements:
    group = el.get("group")
    if group:
        color = category_colors.get(el["category"], "#eeeeee")

        with cols[group - 1]:
            st.markdown(
                f"""
                <div style="
                    background-color:{color};
                    padding:8px;
                    margin:2px;
                    text-align:center;
                    border-radius:8px;
                    font-size:12px;">
                    {el['symbol']}<br>
                    {el['number']}
                </div>
                """,
                unsafe_allow_html=True
            )

# -----------------------------------
# زر عرض صورة الجدول الدوري
# -----------------------------------

st.markdown("---")

if st.button("🖼️ عرض صورة الجدول الدوري"):
    st.image(
        "periodic_table.png",
        caption="الجدول الدوري",
        use_container_width=True
    )

# -----------------------------------
# التوقيع في المنتصف
# -----------------------------------

st.markdown(
    """
    <div style="text-align:center; margin-top:40px;">
        <h4>الاسم: يوسف</h4>
        <h4>الصف: عاشر \"ب\"</h4>
    </div>
    """,
    unsafe_allow_html=True
)

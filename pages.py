import streamlit as st

# 🌟 Streamlit 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천",
    page_icon="🧭",
    layout="centered"
)

# 🎨 제목
st.title("🔮 MBTI 기반 진로 추천 시스템")
st.markdown("### 너의 성격 유형에 맞는 직업을 알아보자! 💼")

# 🔠 MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 📌 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types, index=0)

# 🚀 추천 직업 데이터
mbti_careers = {
    "INTJ": {"emoji": "🧠", "jobs": ["전략 컨설턴트", "데이터 과학자", "연구원"]},
    "INFP": {"emoji": "🎨", "jobs": ["작가", "심리상담가", "예술가"]},
    "ENFP": {"emoji": "🌈", "jobs": ["마케터", "프로듀서", "강연가"]},
    "ISTJ": {"emoji": "📊", "jobs": ["회계사", "행정공무원", "법률보조원"]},
    "ESFP": {"emoji": "🎤", "jobs": ["방송인", "이벤트 플래너", "배우"]},
    # 나머지 유형도 여기에 추가하세요
}

# 💡 선택된 MBTI에 따라 직업 추천
st.markdown("---")
if selected_mbti in mbti_careers:
    emoji = mbti_careers[selected_mbti]["emoji"]
    jobs = mbti_careers[selected_mbti]["jobs"]

    st.header(f"{emoji} {selected_mbti} 유형에게 어울리는 직업")
    for job in jobs:
        st.markdown(f"- ✅ **{job}**")
else:
    st.warning("직업 정보가 아직 준비되지 않았어요. 곧 추가될 예정입니다!")

# 📝 한 줄 조언
st.markdown("---")
st.info("✨ 너의 성격은 너만의 무기야! 자신감 있게 진로를 설계해보자 💪")

# 📬 푸터
st.markdown("---")
st.caption("Made with 💖 by 진로교육팀 | Powered by Streamlit")


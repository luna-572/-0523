import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="나의 소개",
    page_icon="📘",
    layout="centered"
)

# 사이드바에 사진 업로드
st.sidebar.image("https://via.placeholder.com/150", caption="프로필 사진", use_column_width=True)

# 타이틀
st.title("👋 안녕하세요, 반갑습니다!")
st.subheader("나의 소개 페이지입니다.")

# 소개 내용
with st.container():
    st.markdown("### 🙋‍♂️ 기본 정보")
    st.write("""
    - **이름:** 홍길동  
    - **학교:** 대한민국대학교 컴퓨터공학과  
    - **취미:** 책 읽기, 음악 감상, 코딩  
    - **이메일:** honggildong@example.com
    """)

# 구분선
st.markdown("---")

# 간단한 자기소개
st.markdown("### ✨ 한마디 소개")
st.info("항상 배우고 성장하려는 개발자입니다. Streamlit으로 세상과 소통하고 싶어요!")

# 연락 버튼
st.markdown("### 📫 연락하기")
st.markdown("[이메일 보내기](mailto:honggildong@example.com)")

# 푸터
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")


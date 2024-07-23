import streamlit as st

#사이드바 화면

st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력", value="streamlit", max_chars=15)
user_password = st.sidebar.text_input("패스워드 입력", value="", type="password")


if user_password == "1234" :
    st.sidebar.header("탄소배출")
    otp_data =["1","2","3"]
    menu = st.sidebar.selcectbox("메뉴선택",otp_data, index=0)
    st.sidebar.write("선택한메뉴", menu)

    #메인 화면
st. subheader("10조 제로탄산 ")
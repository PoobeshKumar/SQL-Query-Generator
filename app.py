import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyAHJ0T-T2wZIjF_v_6UeswUayxAJBrs-2s"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon=": star:")

    st.markdown(
        """
        <div style="text-align: center;">
            <h1>SQL Query Generator ✨</h1>
            <h3>I can generate SQL queries for you!</h3>
            <p>I am a simple tool who can generate SQL queries based on your prompts.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    text_input = st.text_area("Enter your query here in Plain English:")

    submit = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generate sql query...."):
            template = """
                Create a sql query snippet using the below text:

                '''
                    {text_input}
                    
                '''
                I just want a sql query.

                """
            formatted_template = template.format(text_input=text_input)
            st.write(formatted_template)
            response = model.generate_content(formatted_template)
            sql_query = response.text
            st.write(sql_query)


if __name__ == "__main__":
    main()
import streamlit as st
import openai

# Define GPT-3 language models
models = {
    "text-davinci-002": "Davinci (Best model, requires most credits)",
    "text-curie-001": "Curie",
    "text-babbage-001": "Babbage",
    "text-ada-001": "Ada"
}

# Define Streamlit app
def app():
    st.set_page_config(page_title="AI Blog Writing Tool", page_icon=":pencil2:")
    st.title("AI Blog Writing Tool")

    # Add a sidebar for API key input
    API_KEY = st.sidebar.text_input('Enter your OpenAI API key')

    # Set up OpenAI API key
    openai.api_key = API_KEY

    # Add input fields for blog title and content
    blog_title = st.text_input("Enter Blog Title:")
    blog_content = st.text_area("Enter Blog Content:")

    # Add input fields for additional prompts
    prompt_1 = st.text_input("Enter Additional Prompt 1 (Optional):")
    prompt_2 = st.text_input("Enter Additional Prompt 2 (Optional):")

    # Add dropdown for selecting GPT-3 language model
    selected_model = st.selectbox("Select GPT-3 Language Model", list(models.values()))

    # Get the model ID for the selected language model
    model_id = [key for key, value in models.items() if value == selected_model][0]

    # Add button to generate blog post
    if st.button("Generate Blog Post"):
        # Concatenate all prompts into a single string
        prompts = f"## {blog_title}\n{blog_content}\n\n{prompt_1}\n\n{prompt_2}\n\n"

        # Use OpenAI's GPT-3 language model to generate the blog post
        generated_text = openai.Completion.create(
            engine=model_id,
            prompt=prompts,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Display the generated blog post
        st.markdown("<h2>Generated Blog Post</h2>", unsafe_allow_html=True)
        st.write(generated_text.choices[0].text)

if __name__ == "__main__":
    app()

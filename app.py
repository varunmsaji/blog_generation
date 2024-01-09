import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers 

##fucntiont to get response froom llama
def get_llama(input_text,no_words,blog_style):


    ### LLama2 model
    llm=CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

    








st.set_page_config(page_title="blog generation",
                   layout="centered",initial_sidebar_state="collapsed"
                   
                   )

st.subheader("generate blog")

input_text = st.text_input("enter the topic")

col1,col2 = st.columns([5,5])

with col1:
    no_words =st.text_input("no of words")

with col2:
    blog_style = st.selectbox("writing the blog for",('researchers','data scientist','normal person'),index=0)



submit = st.button('generate')

if submit:
    st.write(get_llama(input_text,no_words,blog_style))


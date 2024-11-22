from langchain_openai.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
import guardarTest
import os



def generatorTest(mappper):

    api_key = os.getenv("OPENAI_API_KEY")

    chat = ChatOpenAI(model_name="gpt-4o", temperature=0, openai_api_key=api_key)


    template = "Genera un  test completo para el siguiente mapper, ten en cuenta que este mapper usa mapstrucs: {mapper}. Solamente  genera el codigo sin ninguna introduccion o explicación"
    prompt = PromptTemplate(
        input_variables=["mapper"],
        template=template,
    )
    chain = LLMChain(llm=chat, prompt=prompt)

    test = chain.run(f"""{mappper}""")

    guardarTest.guardar_test(test)


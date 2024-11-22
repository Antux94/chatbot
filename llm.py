
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


def generateJsonFromRaml(raml_service):

    # Crear la instancia del modelo con model_kwargs
    model_kwargs = {
        "model_name": "gpt-4o",
        "temperature": 0,
        "model_kwargs": {
            "response_format": {
                "type": "json_object"
            }
        }
    }
    chat = ChatOpenAI(**model_kwargs)

    # Crear una plantilla de prompt con LangChain
    template = """
    Eres un ingeniero de software y te vas a encargar de realizar la conversión de un formato RAML a un formato JSON.
    
    RAML:
    {raml_service}
    
    Devuelve la respuesta exclusivamente en formato JSON:
    """

    prompt = PromptTemplate(input_variables=["raml_service"], template=template)

    # Crear una instancia de LLMChain usando la nueva metodología recomendada
    chain = RunnableSequence(prompt | chat)



    # Invocar la cadena
    response = chain.invoke(raml_service)

    #print("La respuesta no es un JSON válido:", type(response))


    # Acceder y imprimir el contenido
    print(response.content)
    #print(response)
    #print(type(response.content))

    import json

    # Convert the string to a JSON object
    try:
        json_object = json.loads(response.content)
        #print(json_object)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York'}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        # Handle the error appropriately

    # Acceder al valor del campo "description" dentro de "responses" -> "202" -> "headers" -> "Content-Location"
    #TODO: QUEDA PENDIENTE HACERLO PARA EL GET
    description_value = json_object["post"]["body"]["application/json"]["type"]

    print(description_value)

    mainDtoSerice = str(description_value).split(".")[-2]
    print(mainDtoSerice)

    return mainDtoSerice






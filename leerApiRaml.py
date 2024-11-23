import re
import llm



def leerApiRamml(ruta):

    # Define la ruta del archivo
    file_path = ruta

    # Lee el contenido del archivo
    with open(file_path, 'r') as file:
        api_raml_content = file.read()

    # Expresión regular para encontrar /calculate-incomes:
    pattern = r"\/[a-zA-Z0-9\-]+\-[a-zA-Z0-9\-]+:"  # Modified regex
    matches = re.findall(pattern, api_raml_content)

    print(matches)  # Esto debería imprimir ['/calculate-incomes:'] si lo encuentra



    # Enumerate and display the matches
    for index, match in enumerate(matches):
        print(f"{index + 1}. {match}")

    # Get user input for selection
    #TODO: CAMBIAR SELECCION DE INDEX
    selected_index = 0
    #selected_index = int(input("Select an option: ")) - 1

    # Access the selected match
    selected_match = matches[selected_index]

    print(f"You selected: {selected_match}")


    # Find the start and end positions of the selected match in the content
    start_index = api_raml_content.find(selected_match)
    end_index = api_raml_content.find(matches[selected_index + 1]) if selected_index + 1 < len(matches) else len(api_raml_content)

    # Extract the information between the selected and next option
    extracted_information = api_raml_content[start_index + len(selected_match) : end_index]

    # Print the extracted information
    #print(extracted_information)


    # Find all occurrences of /anyname:
    anyname_pattern = r"\/[a-zA-Z0-9\-]+:"
    anyname_matches = re.findall(anyname_pattern, extracted_information)

    filtered_matches = [match for match in anyname_matches if "json" not in match]


    # Combine the matches from both patterns
    all_matches = filtered_matches

    print(all_matches)


    # Find the index of the first occurrence of any match
    first_match_index = len(extracted_information)  # Initialize with a large value

    for match in all_matches:
        index = extracted_information.find(match)
        if index != -1 and index < first_match_index:
            first_match_index = index

    # Truncate the extracted_information
    truncated_information = extracted_information[:first_match_index]

    #print(truncated_information)


    mainDto = llm.generateJsonFromRaml(truncated_information)

    return mainDto

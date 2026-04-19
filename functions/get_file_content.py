import os
from config import MAX_READ_CHARS
from google.genai import types





def get_files_content(working_directory, file_path):

    try:
        # Gibt den absoluten Path von working directory an bspw. /user/lepucp/agent_project/functions
        working_directory_abs = os.path.abspath(working_directory)


        # Fügt zu dem working dir unser ziel dir hinzu damit wir einen absoluten path haben in den Ordner in den wir gerade wollen bspw. /user/lepucp/agent_project/calculator -> /user/lepucp/agent_project/calculator/pkg
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))




        #  Schaut ob der Path der angegeben wurde ein valider ist, wenn nicht -> Fehlermeldung
        if not os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs:
            return f'Error: Cannot read "{target_file}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{target_file}"'
        
        # öffnet die datei und liest sie aus
        with open(target_file, "r") as file:
            file_content = file.read(MAX_READ_CHARS)
            if file.read(MAX_READ_CHARS +1):
                file_content += f' [...File "{target_file}" truncated at {MAX_READ_CHARS} characters]'
        return file_content
    

    except:
        return f"Error: something went wrong reading the contents of this file {file_path}"



schema_get_files_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Gives out the content of the file which is in file_path as a string",
        parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path from the file you wanna get the content from, relative to the working directory",
            )
        },
    ),
)
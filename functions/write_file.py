import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        

        # Gibt den absoluten Path von working directory an bspw. /user/lepucp/agent_project/functions
        working_directory_abs = os.path.abspath(working_directory)

        # Fügt zu dem working dir unser ziel dir hinzu damit wir einen absoluten path haben in den Ordner in den wir gerade wollen bspw. /user/lepucp/agent_project/calculator -> /user/lepucp/agent_project/calculator/pkg
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))


        # Erstellt parent Ordner false diese nicht existieren
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        # checkt ob der längste gemeinsamste Path von dem zielpath und dem wokring path gleich der working path sind, wenn ja dann True, da wir wollen dass das stimmt!
        valid_target_dir = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        #  Schaut ob der Path der angegeben wurde ein valider ist, wenn nicht -> Fehlermeldung
        if not valid_target_dir:
            return f'Error: Cannot write to "{target_file}" as it is outside the permitted working directory'
        if  os.path.isdir(target_file):
            return f'Error: Cannot write to "{target_file}" as it is a directory'
        
        
        # Überschreibt den content in target_file mit content
        with open(target_file, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{target_file}" ({len(content)} characters written)'
    except:
        return f"Error: something went wrong when wanting to rewrite {file_path}"
    

schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="rewrites a the file u give it with the content u attach",
        parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path from the file u wanna rewrite relative to the working directory",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="Content is the content you wanna rewrite the file with",
            )
        },
    ),
)

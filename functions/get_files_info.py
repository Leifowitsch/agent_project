import os

# @par working_directory ist der Ordner indem wir arbeiten wollen 
# @par directory ist der Ordner zudem wir wollen in unserem working directory
def get_files_info(working_directory, directory= "."):
        
    try:
        # Gibt den absoluten Path von working directory an bspw. /user/lepucp/agent_project/functions
        working_directory_abs = os.path.abspath(working_directory)

        # Fügt zu dem working dir unser ziel dir hinzu damit wir einen absoluten path haben in den Ordner in den wir gerade wollen bspw. /user/lepucp/agent_project/calculator -> /user/lepucp/agent_project/calculator/pkg
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))

        # checkt ob der längste gemeinsamste Path von dem zielpath und dem wokring path gleich der working path sind, wenn ja dann True, da wir wollen dass das stimmt!
        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs

        #  Schaut ob der Path der angegeben wurde ein valider ist, wenn nicht -> Fehlermeldung
        if not valid_target_dir:
            return f'Error: Cannot list "{target_dir}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        
        # Gibt die metadaten von den Datein in dem Zielordner an
        formated_items = ""
        items_directory = os.listdir(target_dir)
        for item in items_directory:
            item_path = os.path.join(target_dir, item)
            is_dir = os.path.isdir(item_path)
            formated_items += f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={is_dir}\n"

        return formated_items
    except:
        return f"Error: something went wrong getting the directory infos"




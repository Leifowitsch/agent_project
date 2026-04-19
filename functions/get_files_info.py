import os

# @par working_directory ist der Ordner indem wir arbeiten wollen 
# @par directory ist der Ordner zudem wir wollen in unserem working directory
def get_file_info(working_directory, directory= "."):

    # Gibt den absoluten Path von working directory an bspw. /user/lepucp/agent_project/functions
    working_directory_abs = os.path.abspath(working_directory)

    # Fügt zu dem working dir unser ziel dir hinzu damit wir einen absoluten path haben in den Ordner in den wir gerade wollen bspw. /user/lepucp/agent_project/calculator -> /user/lepucp/agent_project/calculator/pkg
    target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))

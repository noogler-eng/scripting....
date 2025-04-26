import os       # link with os
import json     # handling json files
import shutil   # helps in copy and overwrite
from subprocess import PIPE, run    # helps us to run any terminal command
import sys      # halping to taking command line arguments


FAME_DIR_PATTERN = "game"


def find_all_games_paths(source): 
    game_paths = []

    # this will walkthrough all the root, directorys, files .... recurisiely
    for _, dir, _ in os.walk(source):
        # here we are taking all the directories and moving in all directory
        for directory in dir: 
            if FAME_DIR_PATTERN in directory.lower():
                game_path = os.path.join(os.getcwd(), source, directory);
                game_paths.append(game_path)
        
        # we only want to run it one time
        break;
    print(game_paths)
    return game_paths



def create_dir(path):
    # first chechking if directory exists or not
    # making the directry at that path
    if not os.path.exists(path):
        os.mkdir(path)



# this function will give you the directory name from the path
def get_name_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        # we are getting each path here
        # it will give you automatically the last aspect of path
        # either it can be file or directory
        _, dir_name = os.path.split(path)
        # we want to replace the to_strip part from the name of the directory and replace it with ""
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)
    
    return new_names


# if there is already copied version is present then remove it
# again copy from the source to the destination path    
def copy_and_overwrite(source, dest): 
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)






def main(source, target): 
    print(source, target)

    # getting the full path of the directory
    cwd = os.getcwd()
    # always use this ...
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    
    game_paths = find_all_games_paths(source_path);
    new_game_dirs = get_name_from_paths(game_paths, "_game")
    print(new_game_dirs);

    create_dir(path=target_path)
    copy_and_overwrite(source_path, target_path)






# we are using it here as we only want to execute the main script
if __name__ == "__main__":
    # here args contains [filename, command line argumets]
    args = sys.argv
    print(args)
    print(args[1])

    if len(args) != 3:
        raise Exception('you must pass 2 command line arguments!! pass only source and target directory')
    
    # here taking out all the elements except first one
    source, target = sys.argv[1:]
    print(source, target)
    main(source, target)

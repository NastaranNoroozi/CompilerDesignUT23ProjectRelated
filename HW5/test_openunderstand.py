import sys
from os import getcwd
from os.path import join
sys.path.append(join(getcwd(), "openunderstand"))
sys.path.append(join(getcwd(), "openunderstand", "oudb"))
sys.path.append(join(getcwd(), "openunderstand", "utils"))
from openunderstand.ounderstand.openunderstand import *

if __name__ == '__main__':
    start_parsing(
        repo_address=join(getcwd(), "benchmark", "JSON"),
        db_address=getcwd(),
        db_name="mydb.db",
        engine_core="Python3",
        log_address=join(getcwd(), "app.log")
    )

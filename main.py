import sys, os

MAIN_PY = "client.py"

def dev():
    os.system("cd UI && npm run build")
    os.system("python {}".format(MAIN_PY))

def prod():
    os.system("python -m eel {} UI/build --noconsole --onefile".format(MAIN_PY))

def main():
    action = sys.argv[1]
    if action == 'dev':
        dev()
    if action == 'prod':
        prod()

if __name__ == "__main__":
    main()

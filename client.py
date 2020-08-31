import eel
import sys
import app.RPC.main


EEL_MODE = "custom"
EEL_CMDARGS = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe http://localhost:3000"
# .\electron\electron.exe --disable-http-cache http://localhost:3000/index.html",


if sys.platform == "linux":
    EEL_MODE = "chrome"
    EEL_CMDARGS = []

eel.init('UI/build')
eel.start(
    'index.html',
    mode=EEL_MODE,
    cmdline_args=EEL_CMDARGS,
    port=3000,
    size=(500, 200)
)

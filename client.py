import eel
import app.RPC.main

eel.init('UI/build')
eel.start(
    'index.html',
    mode='custom',
    cmdline_args="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe http://localhost:3000",
    # cmdline_args=".\electron\electron.exe --disable-http-cache http://localhost:3000/index.html",
    port=3000,
    size=(500, 200)
)

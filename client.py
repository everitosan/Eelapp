import eel


@eel.expose
def sum(n1, n2):
    return n2 + n1


eel.init('UI')
eel.start(
    'index.html',
    port=3000,
    size=(500, 200)
)

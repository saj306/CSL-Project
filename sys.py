
active = True

def toggle():
    if active:
        deactivate()
    else:
        activate()

def activate():
    active = True

def deactivate():
    active=False
import platform

def play(sound):
    if(platform.system() == "Windows"):
        import winsound
        return winsound.PlaySound(sound,winsound.SND_ASYNC)
    
    elif(platform.system() == "Linux"):
        import os
        part = "aplay "+sound+"&"
        os.system(part)
    
    elif(platform.system() == "Darwin"):
        import os
        part = "afplay "+sound+"&"
        os.system(part)
    

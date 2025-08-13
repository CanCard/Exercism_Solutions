def commands(binary_str):
    ciktim = []
    # WITHOUT ANY CONTROL
    if binary_str[-1] == "1":
        ciktim.append("wink")
    if binary_str[-2] == "1":
        ciktim.append("double blink")
    if binary_str[-3] == "1":
        ciktim.append("close your eyes")
    if binary_str[-4] == "1":
        ciktim.append("jump")
    if binary_str[-5] == "1":
        ciktim.reverse()
    
    return ciktim
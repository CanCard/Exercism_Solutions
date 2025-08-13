def commands(binary_str):
    ciktim = []
    
    if len(binary_str)>= 1 and binary_str[-1] == "1":
        ciktim.append("wink")
    if len(binary_str)>= 2 and binary_str[-2] == "1":
        ciktim.append("double blink")
    if len(binary_str)>= 3 and binary_str[-3] == "1":
        ciktim.append("close your eyes")
    if len(binary_str)>= 4 and binary_str[-4] == "1":
        ciktim.append("jump")
    if len(binary_str)>= 5 and binary_str[-5] == "1":
        ciktim.reverse()
    
    return ciktim
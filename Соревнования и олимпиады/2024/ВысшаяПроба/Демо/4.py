s = ""

def conv(s: str) -> str:
    while "OO" not in s:
    if "OA" in s:
        s = s.replace("OA", "BBO")
    if "OB" in s:
        s = s.replace("OB", "BOCA")
    if "OC" in s:
        s = s.replace("OC", "AAOA")
    return s

import re

file = open("files/demo_2025_24.txt")

pattern = r"( 0{1} | -?[1-9]+ )( [-*] ( 0{1} | -?[1-9]+ ) )+"

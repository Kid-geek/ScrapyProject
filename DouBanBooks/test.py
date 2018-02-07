import re
h='<span class="pl">页数:</span> 339<br/>asd123'
print(re.findall('页数:</span> ([0-9]*)',h)[0])
-- !preview conn=src_memdb()$con

select v
from table(flatten(split(
'191
123
142
12
', '\n')));


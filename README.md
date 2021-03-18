## Ofek Rafaeli interviw

### Magic List
the code can be found in MagicList.py

importing is done by: 

from MagicList import * 

or:

from MagicList import MagicList

this supports most array actions in python, for lack of time i did not include:


 - Python List copy()
 - Python List reverse()
 - Python List Count()
 - Python List sort()

(mainly due to time and I didn't feel like they were the main point of the assingmnet)




### API
the code can be found in API.py

importing is done by: 

from API import * 

the entry point for the file in line 39, "async def login(request):"

the main function of the program is "get_res" which returns the required format for the input data 

not having used Sanic before, i mostly followed these links:
- https://sanic-auth.readthedocs.io/en/latest/
- https://github.com/pyx/sanic-auth

 
### tests

for lack of time, I added a unified testing file for both
tests.py contains this

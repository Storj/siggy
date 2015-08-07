siggy
=====

[![Build Status](https://travis-ci.org/wiggzz/siggy.svg?branch=master)](https://travis-ci.org/wiggzz/siggy) [![Coverage Status](https://coveralls.io/repos/wiggzz/siggy/badge.svg?branch=master&service=github)](https://coveralls.io/github/wiggzz/siggy?branch=master)

Small module for verifying bitcoin signatures

```python
import siggy

message = 'test message'
address = '19qVgG8C6eXwKMMyvVegsi3xCsKyk3Z3jV'
signature = 'HyzVUenXXo4pa+kgm1vS8PNJM83eIXFC5r0q86FGbqFcdla6rcw72/ciXiEPfjli3'\
	'ENfwWuESHhv6K9esI0dl5I='

if (siggy.verify_signature(message, signature, address)):
	print('Signature valid')
else:
	print('Signature invalid')
```

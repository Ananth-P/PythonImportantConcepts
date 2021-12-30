"""
why __future__ statement is used here ?
"the __future__ statement forces Python interpreters to use newerfeatures of the language."

"""

from __future__ import division

print(8/7) # prints 1.1428571428571428
print(8//7) # prints 1

"""
Without the __future__ stuff, in py 2.x version , both print statements would print 1. so we try to use future version changes by using __future__ modules

The internal difference is that without that import, / is mapped to the __div__() method, while with it, __truediv__() is used. (In any case, // calls __floordiv__().)

Also,The future statement is somewhat like a feature flag... When certain features are accepted into Python that change the behavior of existing programs (like true division, for example), first you are able to enable them with the future statement, and then in a future version they become a permanent feature of the language. Hence the name __future__. I believe that this ability to opt into breaking changes early is meant to help existing programs transition in a timely manner, before the breaking change is put into full effect
"""

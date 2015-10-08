# Simple Context example
class MyContext(object):
    def __enter__(self, *args, **kw):
        print '+ Entering the Context!'

    def __exit__(self, *args, **kw):
        print '- Exiting the Context!'

with MyContext() as ctx:
    print 'Hi!'


print "\n**********************************************\n"

# context manager usage
from contextlib import contextmanager

@contextmanager
def my_context(context_arg):
    print '+ Entering Context with:', context_arg
    yield
    print '- Exiting the Context'


with my_context('Hello') as c:
    print 'Inside'

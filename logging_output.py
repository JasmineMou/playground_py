# practice logging
# https://docs.python.org/2/howto/logging.html

import logging
logging.basicConfig(filename='logging_output.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This msg should go to the log file')
logging.info('logging info')
logging.warning('logging warning')

loglevels = ["INFO","DEBUG","WARNING"]

numbers = [getattr(logging, loglevel.upper(), None) for loglevel in loglevels]
print(numbers)
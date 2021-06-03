#q.8: Program to Generate random logs and write in a file , once the file size reaches 2Mb open new file and continue writing

from logzero import logger
import logzero

a=logzero.logfile("myfile.log", maxBytes=1000000, backupCount=3)
print(a)
while True:
    logger.info("This log message saved in the log file")

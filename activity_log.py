from datetime import datetime

def log(name,value,descr=''):
    log_f = open('log.csv', 'a')
    log_f.write('{0},{1},{2},{3}\n'.format(str(datetime.now()),name,value,descr))
    log_f.close()

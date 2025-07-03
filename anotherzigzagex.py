import time,sys
indent = 0
indent_increasing = True

try:
     while True:
            print(' ' * (4-indent), end='')
            print('*', end= '')

            print(' ' * (indent*2), end='')
            print('*')
            
            time.sleep(0.1)

            if indent_increasing:
                  indent = indent + 1
                  if indent == 4:
                        indent_increasing = False
            else:
                  indent = indent -1 
                  if indent == 0:
                        indent_increasing = True
                
    
except KeyboardInterrupt:
     sys.exit()


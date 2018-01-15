import sys

connect('weblogic','WELCOME1','t3://localhost:7001')
domainRuntime()
print("argument1: " + sys.argv[1]) 
shutdown(sys.argv[1],'Server','true',1000,force='true', block='true')

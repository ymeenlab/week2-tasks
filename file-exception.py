#file exception
try:
    f=open('document.txt')  
    data=f.read()
except FileNotFoundError:
    print('File not found')
finally:
    print('cleanup')

import sys 
import socket 
import threading
HEX_FILTER = ''.join([(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])
#................................ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI
# JKLMNOPQR
# STUVWXYZ[.]
# ^_`abcdefghijklmnopqrstuvwxyz{|}~.....................
# .............¡¢£¤¥¦§¨©ª«¬.®¯°±²³´µ¶·¸¹º
# »¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñ
# òóôõö÷øùúûüýþÿ
#print(len(repr(chr(74))))
def hexdump(src, length=16, show=True): 
 if isinstance(src, bytes): #if src type is bytes
    src = src.decode() 
 results = list() 
 for i in range(0, len(src), length): 
   word = str(src[i:i+length]) 
   printable = word.translate(HEX_FILTER) #non printable is replaced with .
   #ord gives unicode
   #0 if padding required 2 characters wide X is converts to uppercase 
   hexa = ' '.join([f'{ord(c):02X}' for c in word]) 
   hexwidth = length*3 #its a constant 2 hex digits and one spaace
   #04 ->4-digit width, padded with zeros if necessary x → Convert to lowercase hexadecimal.
   # < means left-align  hexa inside a field of 
   # width hexwidth, ensuring that all hex dumps line up neatly in columns.
   results.append(f'{i:04x}  {hexa:<{hexwidth}}{printable}') 
 if show: 
     for line in results: 
         print(line) 
 else: 
        return results
#hexdump('python rocks\n and proxies roll\n') 

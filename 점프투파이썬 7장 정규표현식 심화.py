#메타 문자 |

>>> p = re.compile('Crow|Servo')
>>> m = p.match('CrowHello')
>>> print(m)
<_sre.SRE_Match object; span=(0, 4), match='Crow'>
--------------
#메타 문자 ^

>>> print(re.search('^Life', 'Life is too short'))
<_sre.SRE_Match object at 0x01FCF3D8>
>>> print(re.search('^Life', 'My Life'))
--------------
#메타 문자 $

>>> print(re.search('short$', 'Life is too short'))
<_sre.SRE_Match object at 0x01F6F3D8>
>>> print(re.search('short$', 'Life is too short, you need python'))
--------------
#메타 문자 \b

>>> p = re.compile(r'\bclass\b')
>>> print(p.search('no class at all'))
--------------
#메타 문자 \B

>>> p = re.compile(r'\Bclass\B')
>>> print(p.search('no class at all'))  

>>> print(p.search('the declassified algorithm'))
<_sre.SRE_Match object at 0x01F6FA30>
>>> print(p.search('one subclass is'))

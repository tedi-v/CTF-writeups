from subprocess import *
import string

special_chars = "!@#$%^*()-_+=[]{}|:.<>?/"
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + special_chars


def run(cmd):
   p = Popen(cmd, stdout=PIPE, shell=True)
   resu = p.communicate()[0]
   return resu.decode().replace('\n','')

print("[+] Solving character by character")

flag=""

i=-1
while len(flag) < 18:
   cur_num = i
   cur_char = ""
   for c in alphabet:
       cur = flag + c + '_'*(18-len(flag))
       resu=run("echo '{}' | strace ./nanocombattant 2>&1 | grep wait | wc -l".format(cur))
       if int(resu)>=cur_num:
           cur_num = int(resu)
           cur_char = c
   flag += cur_char
   print('\t' + flag)



print("[+] Brute force of the last character")

for c in alphabet:
   resu = run("echo '{}{}' | ./nanocombattant".format(flag, c))
   if "re d'arme" in resu:
       flag += c
       break

print ("[+] Flag : {}".format(flag))

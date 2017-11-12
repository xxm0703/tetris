from subprocess import call
import configurate

print("Installing...")
call("./install.sh", shell=True)
print("Done installing")
configurate.foo()
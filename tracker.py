import time;

print " \n\nWelcome to the official CROWNSTONE performance tracker \n\n"
print "Who are you?"
username = raw_input("GIVE ME YOUR NAME: ")

filename = username.lower() + "-theWorkerSlave.csv"

print "Opening the file..."
target = open(filename, 'a')

lastTime = time.time()

while 1:
    x = raw_input("Are you done yet??")
    if x:
        break
    currentTime = time.time()
    dt = str(currentTime - lastTime)
    target.write(str(time.time()) + "," + str(time.asctime( time.localtime(time.time()) )) + "," + dt + "\n")

    print "Took you long enough..." + dt

    lastTime = time.time()


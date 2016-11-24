import time;

print " \n\nWelcome to the official CROWNSTONE performance tracker \n Now with super start stop function! \n"
print "Who are you?"
username = raw_input("GIVE ME YOUR NAME: ")

filename = username.lower() + "-theWorkerSlave startStop.csv"

print "Opening the file..."
target = open(filename, 'a')

lastTime = time.time()
while 1:
    x = raw_input("Ready?")
    if x:
        break

    lastTime = time.time()
    x = raw_input("Are you done yet??")
    if x:
        break
    currentTime = time.time()
    dt = str(currentTime - lastTime)
    target.write("t:" + str(time.time()) + "," + str(time.asctime( time.localtime(time.time()) )) + "," + dt + "\n")

    print "Took you long enough..." + dt


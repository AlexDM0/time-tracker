import time;

print "Who are you?"
username = raw_input("GIVE ME YOUR NAME: ")

filename = username + ".txt"

print "Opening the file..."
target = open(filename, 'a')

lastTime = time.time()
while 1:
    raw_input("Are you done yet??")
    currentTime = time.time()
    dt = str(currentTime - lastTime)
    target.write("t:" + str(time.time()) + "," + str(time.asctime( time.localtime(time.time()) )) + "," + dt + "\n")

    print "Took you long enough..." + dt

    lastTime = time.time()


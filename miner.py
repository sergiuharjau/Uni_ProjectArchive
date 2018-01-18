import subprocess, time

def stopwatch(minutes):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < minutes:
        elapsed = time.time() - start
        time.sleep(60)

while True:
    print("Oh shit we up and running")
    p = subprocess.Popen("exec " + "./cpuminer -a lyra2zoin -o stratum+tcp://zoi-pool3.chainsilo.com:3032 -u Greeny47.TestVps -p TestVps", shell=True)
    stopwatch(40)
    print("We dead baby")
    p.kill()
    stopwatch(20)

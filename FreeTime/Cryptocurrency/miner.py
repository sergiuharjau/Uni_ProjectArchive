import subprocess, time

def stopwatch(minutes):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < minutes:
        elapsed += 1 
        time.sleep(60)

while True:
    print("Oh shit we up and running")
    p = subprocess.Popen("exec " + "./cpuminer -a lyra2zoin -o stratum+tcp://zoi-pool3.chainsilo.com:3032 -u Greeny47.AndreiAlibaba -p AndreiAlibaba", shell=True)
    stopwatch(55)
    print("We dead baby")
    p.kill()
    stopwatch(5)

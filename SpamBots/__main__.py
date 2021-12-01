import glob
from pathlib import Path
from SpamBots.utils import load_plugins
import logging
from . import UstaD, UstaD2, UstaD3, UstaD4, UstaD5 , UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, UstaD11, UstaD12, UstaD13, UstaD14, UstaD15 , UstaD16, UstaD17, UstaD18, UstaD19, UstaD20

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "SpamBots/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Enjoy! Do visit @USTAD_SPAM_BOTS")

if __name__ == "__main__":
    UstaD.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD2.run_until_disconnected()

if __name__ == "__main__":
    UstaD3.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD4.run_until_disconnected()

if __name__ == "__main__":
    UstaD5.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD6.run_until_disconnected()

if __name__ == "__main__":
    UstaD7.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD8.run_until_disconnected()

if __name__ == "__main__":
    UstaD9.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD10.run_until_disconnected()

if __name__ == "__main__":
    UstaD11.run_until_disconnected()

if __name__ == "__main__":
    UstaD12.run_until_disconnected()

if __name__ == "__main__":
    UstaD13.run_until_disconnected()

if __name__ == "__main__":
    UstaD14.run_until_disconnected()

if __name__ == "__main__":
    UstaD15.run_until_disconnected()

if __name__ == "__main__":
    UstaD16.run_until_disconnected()

if __name__ == "__main__":
    UstaD17.run_until_disconnected()

if __name__ == "__main__":
    UstaD18.run_until_disconnected()

if __name__ == "__main__":
    UstaD19.run_until_disconnected()

if __name__ == "__main__":
    UstaD20.run_until_disconnected()


from time import sleep
from tqdm import tqdm

from . import get_salutation

if __name__ == "__main__":
    with tqdm(total=100, desc="Preparing to salute", leave=False) as p:
        for _ in range(100):
            sleep(0.01)
            p.update()
    print(get_salutation())

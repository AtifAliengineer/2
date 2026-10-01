import random
import sys
import time


def render(percent: int, width: int = 40) -> str:
    filled = round(width * percent / 100)
    return f"[{'#' * filled}{'-' * (width - filled)}] {percent:3d}%"


def main() -> None:
    target = random.randint(0, 100)
    for percent in range(target + 1):
        sys.stdout.write("\r" + render(percent))
        sys.stdout.flush()
        time.sleep(0.02)
    print()


if __name__ == "__main__":
    main()

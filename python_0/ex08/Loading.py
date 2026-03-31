from time import sleep
import os
import time


def format_time(seconds: float) -> str:
    """Convert a time in seconds to MM:SS format."""
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"


def ft_tqdm(lst: range) -> None:  # type: ignore
    """Display a progress bar while yielding the elements of the iterable."""
    total = len(lst)
    start_time = time.time()

    for i, elem in enumerate(lst, start=1):
        percentage = int(i / total * 100)
        percentage_str = f"{percentage:3d}%"

        elapsed = time.time() - start_time
        speed = i / elapsed
        speed_str = f"{speed:.2f}it/s"

        eta = (total - i) / speed
        eta_str = format_time(eta)
        elapsed_str = format_time(elapsed)

        terminal_width = os.get_terminal_size().columns - (
            len(str(total)) * 2
            + len(elapsed_str)
            + len(eta_str)
            + len(speed_str)
            + 14
        )

        bar_size = int(i / total * terminal_width)
        bar = "█" * bar_size + " " * (terminal_width - bar_size)

        print(
            f"\r{percentage_str}|{bar}| {i}/{total} "
            f"[{elapsed_str}<{eta_str}, {speed_str}]",
            end="",
            flush=True,
        )

        yield elem


def main() -> None:

    for elem in ft_tqdm(range(30000)):
        sleep(0.000005)
    return


if __name__ == "__main__":
    main()

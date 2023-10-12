import time


def ft_tqdm(iterable, ncols=50):
    '''
        A tqdm-like function.
        total: total number of iterations
        step: number of iterations between each update
        progress: percentage of iterations completed
        completed: number of iterations completed
        bar: progress bar
        elapsed_time: time elapsed since the beginning of the iteration
        rate: number of iterations per second
        remaining_time: estimated time remaining
        before the end of the iteration
    '''
    total = len(iterable)
    step = max(int(total / ncols), 1)
    start_time = time.time()
    progress = 0
    completed = 0
    bar = ['█'] * completed + [' '] * (ncols - completed)
    print(
        f"\r{progress:.2f}% [{''.join(bar)}] 0/{total} "
        + "[00:00<?, ?it/s]", end="")

    for i, item in enumerate(iterable, 1):

        yield item

        if i % step == 0 or i == total:
            elapsed_time = time.time() - start_time
            rate = i / elapsed_time
            remaining_time = (total - i) / rate if rate > 0 else 0
            elapsed_minutes, elapsed_seconds = divmod(int(elapsed_time), 60)
            remaining_minutes, remaining_seconds = \
                divmod(int(remaining_time), 60)
            progress = (i / total) * 100
            completed = int(i / step)
            bar = ['█'] * completed + [' '] * (ncols - completed)
            print(
                f"\r{progress:.2f}% [{''.join(bar)}] {i}/{total} "
                f"[{elapsed_minutes:02}:{elapsed_seconds:02}<"
                f"{remaining_minutes:02}:{remaining_seconds:02}, "
                f"{rate:.2f}it/s]",
                end=""
            )
    print()


def main():
    for elem in ft_tqdm(range(100)):
        time.sleep(0.005)
        print()


if __name__ == "__main__":
    main()

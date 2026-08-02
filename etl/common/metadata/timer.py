from time import perf_counter


class PipelineTimer:

    def __init__(self):
        self.start = None

    def start_timer(self):
        self.start = perf_counter()

    def stop_timer(self):

        return round(
            perf_counter() - self.start,
            2
        )
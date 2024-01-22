import timeit
from bm import boyer_moore_search
from kmp import kmp_search
from rk import rabin_karp_search


def read_file(filename):
    with open(filename, 'r') as fh:
        return fh.read()


def benchmark(func, text, pattern):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"

    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text, 'pattern': pattern}, number=10)


if __name__ == "__main__":
    text = read_file("article_1.txt")
    existing_pattern = "жадібні алгоритми"
    not_existing_pattern = "цього рядку у тексті не має"

    results = []
    for pattern in (existing_pattern, not_existing_pattern):
        time = benchmark(boyer_moore_search, text, pattern)
        results.append((boyer_moore_search.__name__, pattern, time))

        time = benchmark(kmp_search, text, pattern)
        results.append((kmp_search.__name__, pattern, time))

        time = benchmark(rabin_karp_search, text, pattern)
        results.append((rabin_karp_search.__name__, pattern, time))

    text_2 = read_file('article_2.txt')
    existing_pattern_2 = "бінарний пошук"

    for pattern in (existing_pattern_2, not_existing_pattern):
        time = benchmark(boyer_moore_search, text_2, pattern)
        results.append((boyer_moore_search.__name__, pattern, time))

        time = benchmark(kmp_search, text_2, pattern)
        results.append((kmp_search.__name__, pattern, time))

        time = benchmark(rabin_karp_search, text_2, pattern)
        results.append((rabin_karp_search.__name__, pattern, time))

    title = f"{'| Алгоритм':<32} | {'Підрядок':<30} | {'Час виконання, сек': <32}"
    print(title)
    print("-" * len(title))
    for result in results:
        print(f"| {result[0]:<30} | {result[1]:<30} | {result[2]:<30}")

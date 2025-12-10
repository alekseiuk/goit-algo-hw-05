import timeit


def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def boyer_moore_search(text, pattern):
    def bad_char_heuristic(pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    m = len(pattern)
    n = len(text)
    bad_char = bad_char_heuristic(pattern)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1


def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    p = 0
    t = 0
    h = 1

    if M == 0: return -1

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            if text[i:i + M] == pattern:
                return i
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
    return -1


try:
    with open('article_one.txt', 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open('article_two.txt', 'r', encoding='utf-8') as f:
        text2 = f.read()
except FileNotFoundError:
    text1 = "Placeholder text one for algo analysis" 
    text2 = "Placeholder text two for algo analysis"


real_substring = "структур"
fake_substring = "синхрофазотрон"

algorithms = {
    "Boyer-Moore": boyer_moore_search,
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp_search
}

results = {}

for text_name, text_content in [("Article 1", text1), ("Article 2", text2)]:
    results[text_name] = {}
    for sub_type, sub_val in [("Real", real_substring), ("Fake", fake_substring)]:
        results[text_name][sub_type] = {}
        for algo_name, algo_func in algorithms.items():
            time = timeit.timeit(lambda: algo_func(text_content, sub_val), number=100)
            results[text_name][sub_type][algo_name] = time


print(f"{'Text':<10} | {'Substring Type':<10} | {'Algorithm':<15} | {'Time (100 runs)':<15}")
print("-" * 60)

for text_name, sub_data in results.items():
    for sub_type, algo_data in sub_data.items():
        sorted_algos = sorted(algo_data.items(), key=lambda item: item[1])
        for algo_name, time_val in sorted_algos:
            print(f"{text_name:<10} | {sub_type:<10} | {algo_name:<15} | {time_val:.6f}")

overall_times = {algo: 0 for algo in algorithms}
for text_name in results:
    for sub_type in results[text_name]:
        for algo in algorithms:
            overall_times[algo] += results[text_name][sub_type][algo]

print("\nOverall Speed (Total Time across all tests):")
sorted_overall = sorted(overall_times.items(), key=lambda item: item[1])
for algo, time_val in sorted_overall:
    print(f"{algo}: {time_val:.6f}")
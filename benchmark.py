import csv
import time

from src.sequence_alignment import global_align


def generate_sequence(length):
    bases = "ATGC"
    return "".join(bases[i % 4] for i in range(length))


def run_benchmark():
    print("GeneWeaver Performance Benchmark")
    print("-" * 45)

    results = []

    for length in [50, 100, 200, 400]:
        seq1 = generate_sequence(length)
        seq2 = generate_sequence(length)

        execution_times = []

        for _ in range(3):
            start = time.perf_counter()
            result = global_align(seq1, seq2)
            end = time.perf_counter()

            execution_times.append((end - start) * 1000)

        average_time = sum(execution_times) / len(execution_times)

        results.append([
            length,
            round(average_time, 3),
            result["score"]
        ])

        print(
            f"Length: {length} | "
            f"Average Time: {average_time:.3f} ms | "
            f"Score: {result['score']}"
        )

    with open("benchmark_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Sequence Length", "Average Time (ms)", "Alignment Score"])
        writer.writerows(results)

    print("\nResults saved to benchmark_results.csv")


if __name__ == "__main__":
    run_benchmark()

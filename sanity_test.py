import json
import sys

def load_logs(filename):
    logs = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    logs.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Error parsing line in {filename}: {e}")
                    sys.exit(1)
    return logs

def compare_logs(expected, output):
    if len(expected) != len(output):
        print(f"Mismatch in number of log entries: expected {len(expected)}, got {len(output)}")
        return False

    all_match = True
    for i, (exp, out) in enumerate(zip(expected, output)):
        if exp != out:
            print(f"\nDifference found in log entry {i+1}:")
            all_keys = set(exp.keys()).union(set(out.keys()))
            for key in sorted(all_keys):
                exp_val = exp.get(key)
                out_val = out.get(key)
                if exp_val != out_val:
                    print(f"  Field '{key}': expected {exp_val}, got {out_val}")
            all_match = False
    return all_match

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 sanity_test.py <expected_output.log> <output.log>")
        sys.exit(1)

    expected_file = sys.argv[1]
    output_file = sys.argv[2]

    expected_logs = load_logs(expected_file)
    output_logs = load_logs(output_file)

    if compare_logs(expected_logs, output_logs):
        print("\nSanity test passed: All log entries match.")
    else:
        print("\nSanity test failed: There are differences between expected and actual logs.")
        sys.exit(1)

if __name__ == "__main__":
    main()
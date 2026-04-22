from collections import defaultdict

print("Starting Log Analysis...\n")

failed_attempts = defaultdict(int)

# User input
threshold = int(input("Enter threshold for failed attempts: "))

try:
    with open("log.txt", "r") as file:
        logs = file.readlines()

    for line in logs:
        parts = line.strip().split()

        if len(parts) < 2:
            continue

        ip = parts[0]
        status = parts[1]

        if status == "LOGIN_FAILED":
            failed_attempts[ip] += 1

    print("\nSuspicious Activity Report:\n")

    report_lines = []
    blocked_ips = []

    for ip, count in failed_attempts.items():
        if count >= threshold:
            msg = f"IP {ip} has {count} failed login attempts"
            print(msg)
            report_lines.append(msg)
            blocked_ips.append(ip)

    if not report_lines:
        print("No suspicious activity found")

    # Save report
    with open("report.txt", "w") as report:
        report.write("Suspicious Activity Report\n\n")
        for line in report_lines:
            report.write(line + "\n")

    # Simulate IP blocking
    with open("blocked_ips.txt", "w") as block:
        for ip in blocked_ips:
            block.write(ip + "\n")

    # Most suspicious IP
    if failed_attempts:
        worst_ip = max(failed_attempts, key=failed_attempts.get)
        print(f"\nMost Suspicious IP: {worst_ip}")

    print("\nAnalysis Complete")

except FileNotFoundError:
    print("log.txt file not found")
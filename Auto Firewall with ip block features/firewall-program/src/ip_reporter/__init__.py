class IPReporter:
    def __init__(self):
        self.suspicious_ips = []

    def log_ip(self, ip_address):
        if ip_address not in self.suspicious_ips:
            self.suspicious_ips.append(ip_address)
            self.generate_report(ip_address)

    def generate_report(self, ip_address):
        # Logic to generate and send report for the suspicious IP
        print(f"Reporting suspicious IP: {ip_address}")

    def get_suspicious_ips(self):
        return self.suspicious_ips
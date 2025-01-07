class IPBlocker:
    def __init__(self):
        self.blocked_ips = set()

    def block_ip(self, ip_address):
        self.blocked_ips.add(ip_address)

    def unblock_ip(self, ip_address):
        self.blocked_ips.discard(ip_address)

    def is_blocked(self, ip_address):
        return ip_address in self.blocked_ips

    def get_blocked_ips(self):
        return list(self.blocked_ips)
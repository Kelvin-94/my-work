from firewall import Firewall

def main():
    # Initialize the firewall program
    firewall = Firewall()

    # Set up components
    firewall.setup_traffic_manager()
    firewall.setup_ip_reporter()
    firewall.setup_ip_blocker()

    # Start monitoring network traffic
    firewall.start_monitoring()

if __name__ == "__main__":
    main()
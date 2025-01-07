# Firewall Program

This project is a firewall application designed to manage network traffic, report suspicious IP addresses, and automatically block them when necessary. 

## Features

- **Traffic Monitoring**: Continuously monitors network traffic to identify suspicious activity.
- **IP Reporting**: Logs and reports suspicious IP addresses with detailed information.
- **IP Blocking**: Automatically blocks identified suspicious IP addresses to enhance security.

## Project Structure

```
firewall-program
├── src
│   ├── main.py                # Entry point of the application
│   ├── firewall
│   │   └── __init__.py        # Main Firewall class
│   ├── traffic_manager
│   │   └── __init__.py        # TrafficManager class for monitoring traffic
│   ├── ip_reporter
│   │   └── __init__.py        # IPReporter class for logging and reporting
│   └── ip_blocker
│       └── __init__.py        # IPBlocker class for managing blocked IPs
├── requirements.txt            # Project dependencies
├── config.yaml                 # Configuration settings
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/firewall-program.git
   ```
2. Navigate to the project directory:
   ```
   cd firewall-program
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the firewall program, execute the following command:
```
python src/main.py
```

## Configuration

Modify the `config.yaml` file to adjust settings such as thresholds for suspicious activity and logging levels.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.
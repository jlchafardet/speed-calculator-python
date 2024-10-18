# Download Time Calculator 🚀⏱️

Ever wondered how long it'll take to download that massive game update or your favorite 4K movie? Wonder no more! This handy Python script calculates download times based on file size and internet speed.

## Features 🌟

- Calculate download time for files in MB, GB and TB 
- Support for internet speeds in both Mbps and Gbps
- Use command-line arguments for quick calculations
- Interactive mode for step-by-step input
- Human-friendly time output (hours, minutes, seconds)
- Robust input parsing for various speed formats
- Colorful output for better readability

## How to Use 🖥️

### Quick Calculation

Run the script with file size and download speed as arguments:

```bash
python speed_calculator.py 25GB 600Mbps
```

This calculates how long it'll take to download a 25GB file at 600 Mbps.

### Interactive Mode

Just run the script without any arguments:

```bash
python speed_calculator.py
```

The script will guide you through entering the file size and download speed.

## Requirements 📋

- Python 3.x
- colorama library (install with `pip install colorama`)

## Installation 📥

1. Clone this repository or download the `speed_calculator.py` file.
2. Make sure you have Python 3.x installed on your system.
3. Install the required library:
   ```bash
   pip install colorama
   ```

## Usage Examples 🔍

1. Calculating download time for a 4GB game update on a 100 Mbps connection:
   ```bash
   python speed_calculator.py 4GB 100Mbps
   ```

2. Finding out how long a 1.5GB movie will take to download on a 50 Mbps connection:
   ```bash
   python speed_calculator.py 1.5GB 50Mbps
   ```

3. Calculating download time for a large file with a Gigabit connection:
   ```bash
   python speed_calculator.py 50GB 1Gbps
   ```

## Recent Improvements 🆕

- Added support for Gbps input alongside Mbps
- Improved input parsing to handle various speed formats (e.g., "100Mbps", "1.5Gbps", "500")
- Enhanced error handling for invalid inputs
- Implemented colorful output for better readability
- Added a function to ensure consistent file size formatting
- Added support for Terabyte (TB) file size

## Contributing 🤝

Found a bug? Have a cool idea to make this even better? Contributions are welcome! Feel free to open an issue or submit a pull request.

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Author ✍️

Jose Luis Chafardet Grimaldi

Happy downloading! 🎉
import sys
import re
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def calculate_download_time(file_size, download_speed):
    # Let's figure out if we're dealing with GB or MB
    if file_size[-2:].upper() == "GB":
        # Ah, it's in GB! Let's convert it to MB for our calculations
        file_size_mb = float(file_size[:-2]) * 1024
    elif file_size[-2:].upper() == "MB":
        # Already in MB? Perfect, no conversion needed
        file_size_mb = float(file_size[:-2])
    else:
        # Oops! We need either MB or GB to work with
        print("Whoops! Please use MB or GB for the file size. For example, 500MB or 2GB.")
        return

    # Now, let's convert our file size to bits (because that's what internet speeds use)
    # Remember, 1 byte = 8 bits, so we multiply by 8
    file_size_mbits = file_size_mb * 8

    # Time for the main calculation! How long will this download take?
    download_time_seconds = file_size_mbits / download_speed

    # Let's break this down into hours, minutes, and seconds
    # It's more readable that way!
    hours = int(download_time_seconds // 3600)
    minutes = int((download_time_seconds % 3600) // 60)
    seconds = int(download_time_seconds % 60)

    # Finally, let's tell the user how long they'll be waiting
    if hours > 0:
        print(f"Grab a snack! Your download will take about {Fore.GREEN}{hours}{Style.RESET_ALL} hours, {Fore.GREEN}{minutes}{Style.RESET_ALL} minutes, and {Fore.GREEN}{seconds}{Style.RESET_ALL} seconds.")
    else:
        print(f"Not too long! Your download should take around {Fore.GREEN}{minutes}{Style.RESET_ALL} minutes and {Fore.GREEN}{seconds}{Style.RESET_ALL} seconds.")

def parse_speed(speed_input):
    # New function to parse the speed input
    # This will handle both Mbps and Gbps inputs, with or without the 'ps' suffix
    speed_input = speed_input.lower().strip()
    
    # Use regular expression to extract the numeric part and the unit
    match = re.match(r'(\d+(?:\.\d+)?)\s*(gb|mb|gbps|mbps)?', speed_input)
    
    if match:
        value, unit = match.groups()
        value = float(value)
        
        if unit in ['gb', 'gbps']:
            return value * 1000, "Gbps"  # Convert Gbps to Mbps, but return "Gbps" as unit
        else:
            return value, "Mbps"  # Assume Mbps for 'mb', 'mbps', or no unit
    else:
        raise ValueError(f"Invalid speed input: {speed_input}")

def format_file_size(file_size):
    # This function makes sure our file sizes look nice and consistent
    file_size = file_size.upper().strip()
    if file_size.endswith('GB'):
        return file_size[:-2] + ' GB'
    elif file_size.endswith('MB'):
        return file_size[:-2] + ' MB'
    else:
        raise ValueError(f"Invalid file size input: {file_size}")

def download_time_calculator(file_size_input=None, download_speed_input=None):
    # If we don't have a file size, let's ask for one
    if file_size_input is None:
        file_size_input = input("How big is the file? (e.g., 500MB or 2GB): ").strip() # Ask for file size
    
    # Same for download speed - if we don't have one, let's ask
    if download_speed_input is None:
        download_speed_input = input("What's your internet speed? (e.g., 100Mbps or 1Gbps): ").strip()  # Ask for download speed

    # Format the file size and parse the download speed
    formatted_file_size = format_file_size(file_size_input)
    download_speed_mbps, speed_unit = parse_speed(download_speed_input)

    # Print the inputs in green with correct nomenclature
    print(f"{Fore.GREEN}============")
    print(f"File size: {Fore.GREEN}{formatted_file_size}{Style.RESET_ALL}")
    print(f"Download speed: {Fore.GREEN}{download_speed_mbps} {speed_unit}{Style.RESET_ALL}")

    # Calculate the download time
    calculate_download_time(file_size_input, download_speed_mbps)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        # If we have two arguments, use them as file size and download speed
        file_size_arg = sys.argv[1]
        download_speed_arg = sys.argv[2]
        download_time_calculator(file_size_arg, download_speed_arg)
    elif len(sys.argv) == 1:
        # If no arguments, run interactively
        download_time_calculator()
    else:
        print("Usage: python speed_calculator.py [file_size] [download_speed]")
        print("Example: python speed_calculator.py 10GB 600Mbps")
        print("Or run without arguments for interactive mode.")
        sys.exit(1)
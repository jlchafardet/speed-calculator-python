import sys
import re

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
        print(f"Grab a snack! Your download will take about {hours} hours, {minutes} minutes, and {seconds} seconds.")
    else:
        print(f"Not too long! Your download should take around {minutes} minutes and {seconds} seconds.")

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
            return value * 1000  # Convert Gbps to Mbps
        else:
            return value  # Assume Mbps for 'mb', 'mbps', or no unit
    else:
        raise ValueError(f"Invalid speed input: {speed_input}")

def download_time_calculator(file_size_input=None, download_speed_input=None):
    # If we don't have a file size, let's ask for one
    if file_size_input is None:
        file_size_input = input("How big is the file? (e.g., 500MB or 2GB): ").strip()
    
    # Same for download speed - if we don't have it, we'll ask
    if download_speed_input is None:
        download_speed_input = input("What's your internet speed? (e.g., 100Mbps or 1Gbps): ").strip()

    # Parse the download speed input
    download_speed_mbps = parse_speed(download_speed_input)

    # Great! Now we have everything we need to calculate the download time
    calculate_download_time(file_size_input, download_speed_mbps)

if __name__ == "__main__":
    # Let's see how the user wants to use our calculator
    if len(sys.argv) == 3:
        # Looks like they provided file size and speed. Let's use those!
        file_size = sys.argv[1]
        download_speed = sys.argv[2]
        download_time_calculator(file_size, download_speed)
    elif len(sys.argv) == 1:
        # No arguments? No problem! We'll ask for the info interactively
        download_time_calculator()
    else:
        # Hmm, something's not right with the arguments. Let's help them out
        print("Oops! Here's how to use this tool:")
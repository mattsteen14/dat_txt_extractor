import os
import argparse
import xml.etree.ElementTree as ET

def extract_descriptions(dat_path, output_dir):
    # Parse the XML tree from the .dat file
    try:
        tree = ET.parse(dat_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error: Failed to parse XML in {dat_path}: {e}")
        return
    except FileNotFoundError:
        print(f"Error: File not found = {dat_path}")
        return
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through all <game> elements
    game_count = 0
    extensions = ('.zip', '.7z', '.nes', '.sfc', '.smc', '.gba', '.gbc', '.gb', '.n64', '.z64', '.v64', '.bin', '.iso', '.chd', '.rom', '.mgw', '.nds', '.vb', '.p8', '.32x', '.sms', '.md', '.ngc', '.wsc', '.ws')
    for game in root.findall("game"):
        description_elem = game.find("description")
        rom_elem = game.find("rom")
        
        if description_elem is not None and rom_elem is not None:
            rom_name = rom_elem.attrib.get("name", "")
            if rom_name.endswith(extensions):
                file_name = os.path.splitext(rom_name)[0] # Remove .zip
                description = description_elem.text or ""
                
                # Define path for output text file
                output_path = os.path.join(output_dir, f"{file_name}.txt")
                try:
                # Write the description to the file 
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(description.strip())
                    game_count += 1
                except Exception as e:
                    print(f"Failed to write {output_path}: {e}")
                    
    print(f"\nExtracted {game_count} game descriptions to: {output_dir}")
    
def main():
    parser = argparse.ArgumentParser(
        description="Extract game descriptions from a Skraper generated .dat file and save as individual .txt files."
    )
    parser.add_argument(
        "--dat", "-i",
        required=True,
        help="Path to the .dat file."
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Directory where .txt files will be saved."
    )
    
    args = parser.parse_args()
    extract_descriptions(args.dat, args.output)
    
if __name__ == "__main__":
    main()
# Pwnforge: Automated Reverse Shell Generator

# Features:

  •Multi-Platform Support: Pwnforge facilitates the creation of reverse shell payloads for both Bash and PowerShell, ensuring compatibility across diverse operating systems.
  
  •Payload Encoding: Enhance stealth and bypass detection by encoding payloads in Base64 with a simple command-line toggle.
  
  •Interactive CLI: A user-friendly command-line interface empowers users to effortlessly specify target host, port, and encoding preferences.
  
  •Flexible Payload Selection: Seamlessly switch between Bash and PowerShell payloads to suit varying target environments and preferences.

# Usage:
  •Target Specification: Utilize the -i and -p options to define the target host and port respectively.
  
  •Base64 Encoding: Employ the -e flag to encode generated payloads in Base64, enhancing security and evasion capabilities.
  
  •PowerShell Payload: Activate the -ps flag to generate PowerShell-based reverse shell payloads.

# Example:

python pwnforge.py -i 192.168.1.10 -p 4444 -e -ps

Author:
Zeipher21x 

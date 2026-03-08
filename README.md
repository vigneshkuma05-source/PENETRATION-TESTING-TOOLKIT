# PENETRATION-TESTING-TOOLKIT
*COMPANY*: CODTECH IT SOLUTIONS PVT.LTD

*NAME*: VIGNESH.L

*INTERN ID*: CTIS6589

*DOMAIN*: CYBERSECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH


# TASK-3: PENETRATION TESTING TOOLKIT

A modular, beginner-friendly penetration testing toolkit with multiple modules:

## Module
#01: Port Scanner: 
        This module uses Python's socket library to attempt TCP connections to a range of ports. If a connection is established (return code 0), the port is considered "OPEN".

#02: Brute Forcer: 
        A brute force tool systematically attempts all possible combinations of characters to find the correct credential. This Python script uses itertools to generate combinations.

## How to Run
        python port_scanner.py
        python brute_forcer.py
                OR
        python toolkit.py  (to link your modules together)

----------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Installation & Setup
Ensure you have Python installed on your machine. No external dependencies are required for the basic versions of these scripts as they use standard libraries (socket, itertools, sys).

        > mkdir codtech_toolkit
        > cd codtech_toolkit
        > python toolkit.py

# 2. Modular Architecture
The toolkit follows a modular design pattern. Each tool is a separate Python module that can be imported into the main driver script.

        port_scanner.py: Handles networking and socket connections.
        brute_forcer.py: Handles logic for combinatorics and credential testing.
        toolkit.py: The central CLI interface that imports the above modules.

# 3. Main Interface Code:
        toolkit.py to link your modules together.

# 4. Usage Instructions: Run the toolkit from your terminal:
        C:\Users\acer\Desktop\codtech_toolkit> python toolkit.py

*Select option 1 to scan a local IP (e.g., 127.0.0.1) or option 2 to test the brute force algorithm.*

#  OUTPUT:
*python port_scanner.py*
<img width="931" height="317" alt="Image" src="https://github.com/user-attachments/assets/9ec467d2-d5b6-4bac-b5a5-a79e324e7af2" />

*python brute_forcer.py*
<img width="1055" height="662" alt="Image" src="https://github.com/user-attachments/assets/69ae432e-e9ea-41a5-b009-23e4277081bf" />




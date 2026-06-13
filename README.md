# Port Scanner

A collection of port scanners demonstrating progress from basic sequential socket programming to a robust, high-performance, multithreaded network scanning utility.

---

## Key Features of `Port_Scanner.py`

[Port_Scanner.py] is the primary, production-ready utility in this repository. It includes:

*   **High Performance**: Concurrently scans ports using Python's `threading` and thread-safe `Queue` modules with 100 worker threads.
*   **Service Detection**: Resolves common port numbers to their standard TCP service names (e.g. HTTP, SSH, FTP) using `socket.getservbyport`.
*   **Host Discovery (Ping Check)**: Performs an initial ICMP ping check to verify if the target host is active before launching the port scan (supports both Linux and Windows).
*   **Save to File**: Save your scan results automatically to a text file using the `-o <filename>` flag.
*   **Flexible Usage**: Supports command-line arguments for quick automation or interactive prompts if no target is provided.
*   Safe Interrupts**: Gracefully handles keyboard interrupts (`Ctrl+C`) to exit scans cleanly without tracebacks.

---

## Project Structure

*   `Port_Scanner.py`: The main, fully featured multithreaded port scanner with CLI flags, active host detection, and output logging.
*   `Multi_thr.py`: A simpler multithreaded script showcasing the foundation of queue-based concurrent scanning.
*   `Basic_Seq.py`: A basic sequential single-threaded scanner useful for learning socket basics.

---

## Usage Instructions

### Run the Main Scanner (`Port_Scanner.py`)

#### Basic Scan
Pass the host name or IP address directly as an argument:
```bash
python Port_Scanner.py 127.0.0.1
```

#### Save Results to a File
Use the `-o` flag followed by the output file name to log the scan details:
```bash
python Port_Scanner.py scanme.nmap.org -o scan_results.txt
```

#### Interactive Mode
If no arguments are provided, the script will prompt you for input:
```bash
python Port_Scanner.py
```

#### Help Menu
To see usage guidance:
```bash
python Port_Scanner.py -h
```

---

## Requirements
*   Python 3.x
*   No external dependencies required (built entirely using standard libraries: `socket`, `threading`, `queue`, `subprocess`, etc.)

---

## Disclaimer
This tool is intended for educational and authorized security testing purposes only. Scanning hosts you do not own or have explicit permission to scan may be illegal.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: [Year] [Copyright Holder Name] <[Optional Contact Email]>
# SPDX-License-Identifier: [Choose SPDX Identifier, e.g., MIT, Apache-2.0, GPL-3.0-or-later]

"""
=========================================================================================
SCRIPT METADATA
=========================================================================================
SCRIPT NAME     : [your_script_name.py]
PURPOSE         : [Concisely state the script's primary goal or function. What problem does it solve?]
                  [Example: Automate the processing of input data files based on configuration settings.]
-----------------------------------------------------------------------------------------
AUTHOR          : [Your Name / Primary Maintainer Name]
TEAM            : [Your Team Name, if applicable, optional]
ORGANIZATION    : [Your Organization Name, if applicable, optional]
CONTACT         : [Your Email / Team Distribution List / Preferred Contact Method]
WEBSITE         : [Link to relevant website, project page, or documentation, optional]
PROFILE         : [Optional: Link to Author's LinkedIn/GitHub profile]
REPOSITORY      : [Link to the script's code repository (e.g., GitHub, GitLab), optional]
CREATED ON      : [YYYY-MM-DD - The date the script was initially created.]
LAST UPDATED    : [YYYY-MM-DD - The date of the last significant modification.]
VERSION         : [Semantic Versioning recommended, e.g., 1.0.0]
=========================================================================================

=========================================================================================
DESCRIPTION
=========================================================================================
[Provide a comprehensive explanation of the script's functionality. Describe its features,
the problem it addresses in more detail, and its general workflow or operational logic.
Use bullet points for clarity when outlining key steps or functions.]
Example:
This script reads data from a specified input file, processes it according to rules
defined in a configuration file, and outputs the results to a designated location.
It uses Python's logging module for detailed execution tracing and argparse for
handling command-line arguments.

Key Workflow / Functions:
- Parses command-line arguments (input file, config file path, verbosity, etc.).
- Loads configuration settings from a YAML/INI/JSON file.
- Validates inputs and configuration parameters.
- Sets up logging based on configuration and verbosity level.
- Reads and processes data from the input source.
- Performs calculations or transformations based on the logic.
- Handles potential errors during processing (e.g., file not found, data format issues).
- Writes processed data or results to an output file or standard output.
- Logs progress, warnings, and errors throughout execution.
- Cleans up temporary resources upon completion or interruption.
=========================================================================================

=========================================================================================
DESIGN PHILOSOPHY
=========================================================================================
[Explain the core principles or rationale behind the script's design.]
- **[Modularity]:** [e.g., Code organized into functions/classes for distinct tasks (parsing, config loading, processing, logging).]
- **[Robustness]:** [e.g., Includes comprehensive error handling using try-except blocks for anticipated issues like I/O errors, config errors, library exceptions.]
- **[Readability]:** [e.g., Follows PEP 8 guidelines, uses meaningful variable/function names, includes comments and detailed docstrings.]
- **[Simplicity/Complexity]:** [e.g., Aims for clarity and maintainability while implementing necessary features.]
- **[Efficiency]:** [e.g., Uses appropriate data structures and algorithms, considers performance implications of I/O and computations.]
- **[Testability]:** [e.g., Functions designed to be testable, allowing for unit tests (using pytest/unittest).]
- **[Maintainability]:** [e.g., Clear structure, documentation, and configuration facilitate future updates.]
=========================================================================================

=========================================================================================
PRIMARY AUDIENCE
=========================================================================================
[Specify the intended users or roles for this script.]
- [e.g., Data Analysts needing automated data processing.]
- [e.g., Backend Developers integrating data pipelines.]
- [e.g., System Administrators performing automated tasks.]
- [e.g., Researchers managing experimental data.]
=========================================================================================

=========================================================================================
USAGE
=========================================================================================
**Permissions:**
- Script execution: `chmod +x [your_script_name.py]` (if run directly via shebang).
- File system access: [e.g., Read access to input file(s) and config file, Write access to output directory/log file.]
- Network access: [e.g., Required if fetching data from APIs or remote resources.]
- Elevated privileges: [e.g., Rarely needed unless interacting with protected system resources. Explain *why* if necessary.]

**Basic Syntax:**
`python [your_script_name.py] [options] [arguments]`
or if executable:
`./[your_script_name.py] [options] [arguments]`

**Options (Example using argparse):**
  -h, --help            Show this help message and exit
  -v, --verbose         Enable verbose output (DEBUG level logging).
  -d, --dry-run         Simulate execution without making changes or writing output.
  --config FILE         Specify the path to the configuration file (Default: './config.yaml').
  --output FILE         Specify the path for the output file (Default: './output/result.csv').
  --log-file FILE       Specify the path for the log file (Default: './logs/[script_name].log').
  --no-log-file         Disable logging to a dedicated file.
  --log-level LEVEL     Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
  [Add other script-specific options here]

**Arguments (Example using argparse):**
  input_path            Path to the input data file or directory. [Required]
  [ARG_2]               [Description of the second required/optional argument...]

**Common Examples:**
1. Run with default settings:
   `python [your_script_name.py] /path/to/input.data`

2. Run with a specific config file and verbose output:
   `python [your_script_name.py] --verbose --config /etc/script/prod.yaml /path/to/input.data`

3. Perform a dry run simulation:
   `./[your_script_name.py] --dry-run /path/to/input.data`

4. Specify output and log paths:
   `python [your_script_name.py] --output /data/processed.csv --log-file /var/log/script.log /path/to/input.data`

**Advanced Execution (Automation):**
- Example cron job running daily at 3 AM, using a virtual environment:
  `0 3 * * * /path/to/project/venv/bin/python /path/to/project/[your_script_name.py] --config /etc/script/config.yaml /data/input >> /var/log/script_cron.log 2>&1`
  (Ensure correct paths, permissions, and environment variables are available to cron).

- Example systemd service integration: Create a unit file (e.g., `/etc/systemd/system/script_name.service`) defining `ExecStart`, `User`, `Group`, `WorkingDirectory`, and potentially environment variables or dependencies. Use a corresponding `.timer` file for scheduled execution. Refer to systemd documentation.
=========================================================================================

=========================================================================================
INSTALLATION / DEPLOYMENT
=========================================================================================
**Recommended Location:**
- Project-specific: Within the project's directory structure alongside related code/data.
- User scripts: `~/.local/bin/` (ensure this is in user's $PATH).
- System-wide tools: `/opt/[project_name]/` or `/usr/local/bin/` (manage permissions carefully).

**Virtual Environment (Strongly Recommended):**
1. Create: `python3 -m venv venv` (within the project directory)
2. Activate: `source venv/bin/activate` (Linux/macOS) or `.\venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Deactivate: `deactivate`

**Manual Setup:**
1. Place the script and any associated files (e.g., `config.example`) in the chosen location.
2. Ensure the correct Python interpreter is used (consider shebang or explicit calls).
3. Set executable permissions if needed: `chmod +x [your_script_name.py]`.
4. Install required Python packages (see DEPENDENCIES section) preferably into a venv.
5. Create necessary configuration files from examples, adjusting paths and settings.
6. Create necessary directories (e.g., for logs, output) and set appropriate permissions.
7. Run the script initially with `--help` or `--dry-run` to test setup.

**Integration (Optional):**
- **Systemd Service:** Provide example unit files (`.service`, `.timer`) or link to them. Ensure correct paths, user, group, and activation of the virtual environment if used.
- **Cron Job:** Use full paths for the interpreter and script. Ensure the environment (PATH, custom ENV_VARS) is correctly set up for the cron user. Activate venv if necessary.
- **Configuration Management:** Integrate deployment via Ansible, Puppet, Chef, SaltStack, Docker, etc.
=========================================================================================

=========================================================================================
DEPENDENCIES & ENVIRONMENT
=========================================================================================
**Required Python Version:**
- Python >= [e.g., 3.8] (Specify minimum required version)

**Required Packages (Example):**
- `PyYAML`: For loading configuration from YAML files (if using YAML).
- `pandas`: For data manipulation (if processing tabular data).
- `requests`: For making HTTP requests (if interacting with APIs).
- `python-dotenv`: For loading environment variables from a `.env` file (optional but recommended for secrets).
- [List other essential packages]

**Setup Instructions:**
- Create a `requirements.txt` file listing all dependencies with versions:

```
PyYAML>=5.0
pandas==1.5.3
requests
python-dotenv
```

**Add other dependencies here**
- Install dependencies using pip (preferably in a virtual environment):
`pip install -r requirements.txt`
- Check package availability/version: `pip show [package_name]`

**Required System Binaries/Tools (If applicable):**
- [List any external non-Python tools the script relies on, e.g., `git`, `ffmpeg`, `database_client`]
- [Tool Name]: [Purpose] (Minimum version if critical)
- Example Installation (Debian/Ubuntu): `sudo apt update && sudo apt install -y [tool_package]`
- Example Installation (RHEL/CentOS/Fedora): `sudo dnf update && sudo dnf install -y [tool_package]`

**Operating System Compatibility:**
- Designed primarily for: [e.g., Linux (Ubuntu 20.04+, CentOS 7+), macOS, Windows 10+]
- Known compatibility issues: [e.g., Path differences on Windows, reliance on specific POSIX features not available on Windows without WSL.]
- Windows Subsystem for Linux (WSL): [e.g., Tested and working on WSL2.]

**Environment Variables Used (Example):**
- `APP_API_KEY`: API key for accessing Service X (Loaded via `os.environ.get` or `dotenv`).
- `APP_CONFIG_PATH`: Alternative path to the configuration directory.
- `LOG_LEVEL`: Can override the default/config file log level.
- `PYTHONPATH`: Standard Python variable affecting module imports.

**System Resource Requirements:**
- Minimum: [Estimate baseline needs, e.g., 1 vCPU, 512MB RAM, 100MB Disk Space]
- Recommended: [Estimate for typical workload, e.g., 2 vCPUs, 1GB RAM, 500MB Disk Space + space for logs/output/data]
- Peak Usage: [Mention if specific operations cause spikes, e.g., High memory usage for large datasets with pandas, high CPU for complex computations.]
=========================================================================================

=========================================================================================
LOGGING MECHANISM
=========================================================================================
**Implementation:**
- Uses Python's built-in `logging` module. Configurable via code or a logging configuration file.

**Log Destination(s):**
- Console (stdout/stderr): Default for INFO/DEBUG (stdout) and WARNING/ERROR/CRITICAL (stderr). Controlled by handlers.
- Dedicated Log File: Optional, enabled via `--log-file` argument or config. Path specified by user or defaults.
- System Log (syslog/journald): Possible via `logging.handlers.SysLogHandler`. Requires platform-specific setup (e.g., `/dev/log` socket on Linux).

**Log Format:**
- Default Format: `%(asctime)s - %(name)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s`
- Configurable via `logging.basicConfig` or custom formatter objects.

**Log Levels:**
- `DEBUG`: Detailed information, typically of interest only when diagnosing problems. Enabled via `-v` or `--log-level DEBUG`.
- `INFO`: Confirmation that things are working as expected. Default level.
- `WARNING`: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
- `ERROR`: Due to a more serious problem, the software has not been able to perform some function.
- `CRITICAL`: A serious error, indicating that the program itself may be unable to continue running.

**Log Rotation (if using a dedicated file):**
- Handled by script?: Can be implemented using `logging.handlers.RotatingFileHandler` (by size) or `TimedRotatingFileHandler` (by time interval).
- External Recommendation: Often preferred to use external tools like `logrotate` for flexibility and system consistency.
- Example `logrotate` configuration (`/etc/logrotate.d/[script_name]`):

```
/path/to/logs/[script_name].log {
daily # Rotate logs daily
rotate 7 # Keep 7 days of backups
compress # Compress rotated logs
delaycompress # Don't compress the most recent backup immediately
missingok # Don't error if log file is missing
notifempty # Don't rotate if the log is empty
create 0640 [user] [group] # Create new log file with specific permissions/ownership
sharedscripts
postrotate
# Signal the application if needed (rare for simple scripts)
# Example: kill -HUP $(cat /var/run/script_name.pid)
endscript
}
```
=========================================================================================

=========================================================================================
OUTPUTS
=========================================================================================
[Describe the primary outputs generated by the script.]

**Standard Output (stdout):**
- Normal Operation: Prints INFO/DEBUG messages if configured (and `-v` used for DEBUG). May include progress indicators or summaries.
- Data Output: If designed to output results to console, describe format (e.g., JSON objects per line, CSV rows, plain text).

**Standard Error (stderr):**
- Errors: Prints WARNING, ERROR, CRITICAL log messages. Includes tracebacks for unhandled exceptions.
- Help/Usage Messages: Output from `--help`.

**Generated/Modified Files:**
- Log File: [Path as specified by `--log-file` or default. Contains detailed execution trace.]
- Report/Data File: [e.g., Path specified by `--output`. Contains results of the operation in specified format (CSV, JSON, TXT, etc.).]
- Temporary Files: [e.g., May use `tempfile` module for intermediate data in `/tmp/`. Mention if automatically cleaned up.]
- Configuration Files Modified: [e.g., Rarely modifies config, but might update a state file like `~/.local/share/[script_name]/last_run.json`.]
- Other Outputs: [e.g., Downloads files to a specific directory, interacts with a database.]
=========================================================================================

=========================================================================================
ERROR HANDLING & CONSIDERATIONS
=========================================================================================
**Exit Codes:**
- 0: Success - Script completed all tasks successfully.
- 1: General Error - Unspecified failure or catch-all for uncaught exceptions.
- 2: Argument/Usage Error - Invalid command-line arguments or options (often handled by argparse).
- 3: Configuration Error - Invalid or missing configuration file, bad syntax, missing required settings.
- 4: File Not Found Error - Input file, config file, or essential resource not found.
- 5: Permission Error - Insufficient privileges for file access, network operation, etc.
- 6: Data Error - Invalid data format in input file, unexpected values.
- 7: Dependency Error - Required package not installed or external binary missing/failed.
- [Add other script-specific exit codes (e.g., 10: API request failed, 11: Processing threshold exceeded) and their meanings.]

**Exception Handling:**
- Uses `try...except` blocks to catch specific, anticipated exceptions (e.g., `FileNotFoundError`, `PermissionError`, `yaml.YAMLError`, `requests.exceptions.RequestException`, `KeyError`, `ValueError`).
- Logs errors using the `logging` module, including tracebacks for unexpected errors.
- Provides informative error messages to the user/log.
- Uses `sys.exit(code)` to terminate with appropriate non-zero exit codes upon failure.

**Potential Issues & Troubleshooting:**
- **Issue:** `ModuleNotFoundError: No module named '[package_name]'`
**Resolution:** Ensure the virtual environment is activated (`source venv/bin/activate`). Install dependencies: `pip install -r requirements.txt`.
- **Issue:** `FileNotFoundError: [Errno 2] No such file or directory: '/path/to/file'`
**Resolution:** Verify the file path is correct. Check that the file exists and the script has read permissions. Ensure relative paths are resolved correctly based on the script's working directory.
- **Issue:** `PermissionError: [Errno 13] Permission denied: '/path/to/resource'`
**Resolution:** Check script's execution user (`whoami` or logs). Check file/directory permissions (`ls -ld /path/to/resource`). Ensure the user has necessary read/write/execute rights.
- **Issue:** Configuration value missing or incorrect (`KeyError`, `ValueError`).
**Resolution:** Check the specified configuration file (`--config`) for typos or missing keys/sections. Refer to `config.example` for the expected structure. Validate data types.
- **Issue:** Network Error (`requests.exceptions.ConnectionError`, `Timeout`).
**Resolution:** Check network connectivity from the execution environment. Verify API endpoints, URLs, proxy settings, and firewall rules.

**Important Considerations / Warnings:**
- **[CRITICAL WARNING: Data Modification/Deletion Risk]**
[If the script modifies or deletes data (files, database records), state this CLEARLY.]
[Example: "This script may overwrite the output file specified by `--output`. Ensure backups exist or use unique filenames. The `--dry-run` flag prevents file writing."]
- **[Security Warning: Sensitive Data Handling]**
[If handling passwords, API keys, PII: Explain how. **Strongly advise against hardcoding.** Recommend environment variables (`os.environ`), `.env` files (`python-dotenv`), secure config files (strict permissions), secrets management tools (Vault, AWS Secrets Manager), or secure prompts (`getpass`).]
[Example: "API keys should be provided via the `APP_API_KEY` environment variable, not in the config file or command line."]
- **[Idempotency]:** [Can the script be run multiple times with the same input and achieve the same final state without unintended side effects? Yes/No/Partially. Explain potential issues like appending to files vs. overwriting.]
- **[Resource Usage]:** [Can this script consume significant CPU, memory, disk I/O, or network bandwidth, especially with large inputs? Advise monitoring.]
- **[Concurrency/Locking]:** [Is the script safe to run multiple instances simultaneously? Does it need locking (e.g., using `filelock` library or PID files) to prevent race conditions on shared resources?]
- **[Rate Limiting]:** [If interacting with APIs, are there rate limits? Does the script handle them gracefully (e.g., `time.sleep`, backoff strategies, checking response headers)?]
- **[Atomicity]:** [Are critical operations (e.g., file replace, database transaction) performed atomically? What is the state if the script is interrupted mid-operation?]
=========================================================================================

=========================================================================================
ASSUMPTIONS
=========================================================================================
[List any assumptions the script makes about its execution environment or input data.]
- Assumes Python interpreter (version specified above) is installed and accessible.
- Assumes required packages listed in `requirements.txt` are installed in the environment (preferably a venv).
- Assumes necessary system binaries (if listed) are installed and in the system `$PATH`.
- Assumes configuration file exists at the specified path (or default) and is correctly formatted (e.g., valid YAML/JSON/INI).
- Assumes input data exists at the specified path and conforms to the expected format.
- Assumes necessary network connectivity and permissions if external resources are accessed.
- Assumes the script is executed with appropriate user permissions for reading inputs and writing outputs/logs.
- Assumes environment variables (if used for configuration/secrets) are set correctly.
=========================================================================================

=========================================================================================
PERFORMANCE OPTIMIZATION (Optional - Fill if relevant)
=========================================================================================
**Benchmarks:**
- [Provide performance metrics if available/relevant.]
[Example: Processing a 100MB input file takes ~X seconds on a system with Y specs.]
[Example: Handles ~Z requests per second when interacting with API Q.]

**Resource Consumption Profile:**
- CPU: [e.g., Generally low, spikes during pandas DataFrame operations or complex regex matching.]
- Memory: [e.g., Peak usage depends on input data size, typically < N MB for standard inputs.]
- Disk I/O: [e.g., Primarily during initial read of input and final write of output/logs.]
- Network: [e.g., Dependent on API interaction frequency and data volume transferred.]

**Optimization Notes:**
- [Mention specific techniques used or areas for potential improvement.]
[e.g., Used generators to process large files line-by-line, avoiding loading all data into memory.]
[e.g., Optimized pandas operations (vectorization vs. iteration).]
[e.g., Implemented caching for frequently accessed external resources.]
[e.g., Potential Bottleneck: Serial processing of large datasets; consider `multiprocessing` or `asyncio`.]
=========================================================================================

=========================================================================================
TESTING & VALIDATION (Optional - Describe testing efforts)
=========================================================================================
**Test Strategy:**
- Unit Tests: Using `pytest` or `unittest` framework to test individual functions and classes with mocked dependencies. Located in `tests/` directory.
- Integration Tests: Testing the interaction between components or with external systems (e.g., file system, dummy API).
- Manual Testing: Executing the script with various inputs and options to verify end-to-end behavior.

**Key Test Cases Covered:**
- [e.g., Test argument parsing for valid and invalid options/arguments.]
- [e.g., Test configuration loading with default, custom, and invalid files.]
- [e.g., Test core processing logic with valid data, edge cases (empty input, large values), and invalid data formats.]
- [e.g., Test error handling for file not found, permissions, invalid config, etc.]
- [e.g., Verify correct output format and content for given inputs.]
- [e.g., Test `--dry-run` mode prevents side effects.]
- [e.g., Verify correct logging levels and messages based on verbosity and outcomes.]
- [e.g., Check exit codes match expected success/failure conditions.]

**Validation Environment:**
- Tested OS: [e.g., Ubuntu 22.04 LTS, macOS Ventura, Windows 11]
- Tested Python Version(s): [e.g., 3.8, 3.10, 3.11]
- Tested Key Dependencies: [e.g., PyYAML 6.0, pandas 1.5.3] (Ideally pinned in requirements.txt)

**Automation:**
- [e.g., Unit tests run automatically via CI/CD pipeline (GitHub Actions, GitLab CI) on push/pull request.]
- [e.g., Static analysis performed using tools like `flake8`, `mypy`, `pylint`.]
- [e.g., Security analysis performed using tools like `bandit` or `safety`.]
=========================================================================================

=========================================================================================
FUTURE ROADMAP / POTENTIAL IMPROVEMENTS
=========================================================================================
[List planned features, known limitations, or ideas for future enhancement.]
- [Feature 1: Add support for reading input from cloud storage (S3, GCS).]
- [Feature 2: Implement output in additional formats (e.g., JSON, Parquet).]
- [Improvement 1: Enhance error reporting with more specific details.]
- [Improvement 2: Add asynchronous processing (`asyncio`) for network-bound tasks.]
- [Improvement 3: Implement parallel processing (`multiprocessing`) for CPU-bound tasks.]
- [Compatibility 1: Package the script for easier distribution via PyPI or as a standalone executable (using PyInstaller/Nuitka).]
- [Refactoring 1: Refactor the main processing logic into smaller, more focused classes/functions.]
- [Known Limitation: Currently processes files serially.]
=========================================================================================

=========================================================================================
SECURITY CONSIDERATIONS
=========================================================================================
- **Privilege Level:** [Requires root/sudo? Explain why. Strive for least privilege. Should generally run as a non-privileged user unless specific system interaction is required.]
- **Input Sanitization:** [How is input from command-line arguments, config files, environment variables, and data files validated/sanitized? Use type checking (argparse types), regex validation, schema validation (e.g., with `Pydantic`, `Cerberus`) for config/data. Be cautious constructing paths or commands from input.]
- **Sensitive Data Handling:** [Passwords, API keys, Tokens. **AVOID HARDCODING.** Recommendations: Use environment variables (`os.environ`), `.env` files (`python-dotenv`), OS keychain access (`keyring`), dedicated secrets management tools (Vault, AWS/GCP/Azure Secrets Manager), or secure prompts (`getpass`). Document the chosen method.]
- **Dependencies:** [Are dependencies reputable? Pinned in `requirements.txt`? Regularly audited for vulnerabilities using tools like `safety check -r requirements.txt` or GitHub Dependabot/Snyk?]
- **File Permissions:** [What permissions are set on created files/directories (logs, output, config, temp)? Use secure defaults. `os.makedirs(..., mode=0o750)`, `open(..., mode='w')` respects umask. Be explicit with `os.chmod` if needed, especially for sensitive files (e.g., 0o600).]
- **External Command Execution:** [If using `subprocess` module, avoid `shell=True`. Pass arguments as a list `subprocess.run(['command', arg1, arg2])`. Sanitize/validate any variables used in arguments to prevent injection vulnerabilities.]
- **Network Exposure:** [Does it listen on ports (`socket`, web frameworks)? Connect to external services? Use HTTPS/TLS? Validate certificates? Handle network errors securely.] [Example: Makes outbound HTTPS requests to defined API endpoints. Uses `requests` library which handles TLS.]
- **Code Integrity:** [If distributing, provide checksums (SHA256) or signatures (GPG) for verification.]
- **Error Message Verbosity:** [Ensure error messages logged or shown to users do not inadvertently leak sensitive information (e.g., internal paths, keys, data snippets) especially in production environments.]
- **Resource Exhaustion:** [Can crafted input (large files, complex patterns) lead to DoS (Denial of Service) via excessive memory/CPU usage? Implement limits or checks if necessary.]
=========================================================================================

=========================================================================================
DOCUMENTATION
=========================================================================================
- Primary documentation is within this script's docstring and code comments.
- External documentation (if applicable):
- README: [Link to README.md in repository, if exists]
- Wiki: [Link to project Wiki, if exists]
- API Docs (Sphinx/MkDocs): [Link if generated]
- Confluence/Internal Docs: [Link if relevant]
=========================================================================================

=========================================================================================
SUPPORT & CONTACT
=========================================================================================
- Author/Maintainer: [Your Name / Team Name]
- Contact: [Your Email / Team Distribution List / Slack Channel]
- Bug Reports/Issues: [Link to GitHub Issues page, Jira project, or specific contact email.]
- Feature Requests: [Process for submitting feature requests, e.g., GitHub Issues.]
=========================================================================================

=========================================================================================
LICENSE
=========================================================================================
Distributed under the [Specify License Name, e.g., MIT] License.
See accompanying `LICENSE` file or visit [Link to license text online, e.g., https://opensource.org/licenses/MIT]

Copyright (c) [Year] [Copyright Holder Name]
=========================================================================================
"""

# =========================================================================================
# IMPORTS
# =========================================================================================
# Standard library imports
import argparse
import logging
import os
import sys
import traceback
import signal
import atexit
import tempfile
from typing import Dict, List, Any, Optional # For type hinting

# Third-party library imports (add/remove as needed)
try:
  import yaml # Example: For YAML config
except ImportError:
  yaml = None # Handle optional dependency

try:
  import dotenv # Example: For .env file loading
except ImportError:
  dotenv = None

# try:
#     import pandas as pd
# except ImportError:
#     pd = None

# try:
#     import requests
# except ImportError:
#     requests = None

# try:
#     from filelock import FileLock, Timeout # Example: For process locking
# except ImportError:
#     FileLock, Timeout = None, None


# =========================================================================================
# METADATA / MODULE CONSTANTS
# =========================================================================================
__author__ = "[Your Name / Team Name]"
__version__ = "[e.g., 1.0.0]"
__license__ = "[Specify SPDX Identifier, e.g., MIT]"
__status__ = "Development" # Or "Production", "Testing"

# Script Info
SCRIPT_NAME = os.path.basename(__file__)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Default Configuration Values ---
# These can be overridden by config file or command-line arguments
DEFAULT_CONFIG_FILENAME = "config.yaml" # Default config file name in script dir or specified dir
DEFAULT_CONFIG_PATH = os.path.join(SCRIPT_DIR, DEFAULT_CONFIG_FILENAME)
DEFAULT_OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")
DEFAULT_LOG_DIR = os.path.join(SCRIPT_DIR, "logs")
DEFAULT_LOG_FILENAME = f"{os.path.splitext(SCRIPT_NAME)[0]}.log"
DEFAULT_LOG_FILE_PATH = os.path.join(DEFAULT_LOG_DIR, DEFAULT_LOG_FILENAME)
DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_LOCK_FILENAME = f"{os.path.splitext(SCRIPT_NAME)[0]}.lock"
DEFAULT_LOCK_FILE_PATH = os.path.join(tempfile.gettempdir(), DEFAULT_LOCK_FILENAME)

# Exit Codes (match documentation)
EXIT_SUCCESS = 0
EXIT_GENERAL_ERROR = 1
EXIT_ARGUMENT_ERROR = 2
EXIT_CONFIG_ERROR = 3
EXIT_FILE_NOT_FOUND_ERROR = 4
EXIT_PERMISSION_ERROR = 5
EXIT_DATA_ERROR = 6
EXIT_DEPENDENCY_ERROR = 7
EXIT_KEYBOARD_INTERRUPT = 130


# --- Global Runtime Variables ---
# These store the script's configuration and state, populated during setup.
config: Dict[str, Any] = {} # Parsed configuration
logger: Optional[logging.Logger] = None # Logger instance
temp_dir: Optional[str] = None # Path to temporary directory, if created
lock: Optional[Any] = None # File lock object, if locking enabled


# --- ANSI Color Definitions (Optional) ---
# For enhancing terminal output readability
COLOR_ENABLED = sys.stdout.isatty() # Enable colors only if stdout is a terminal

class Colors:
  RESET = '\033[0m'
  RED = '\033[0;31m'
  GREEN = '\033[0;32m'
  YELLOW = '\033[0;33m'
  BLUE = '\033[0;34m'
  CYAN = '\033[0;36m'
  BOLD = '\033[1m'

  @staticmethod
  def colorize(text: str, color_code: str) -> str:
      return f"{color_code}{text}{Colors.RESET}" if COLOR_ENABLED else text

# =========================================================================================
# HELPER FUNCTIONS
# =========================================================================================

def _log_uncaught_exception(exc_type, exc_value, exc_traceback):
  """Handler for sys.excepthook to log uncaught exceptions."""
  if issubclass(exc_type, KeyboardInterrupt):
      # Don't log KeyboardInterrupt, let the finally block handle it
      sys.__excepthook__(exc_type, exc_value, exc_traceback)
      return

  if logger:
      logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
  else:
      # Fallback if logger wasn't initialized
      print(f"CRITICAL: Uncaught exception: {exc_value}", file=sys.stderr)
      traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stderr)

def setup_logging(log_level_str: str = DEFAULT_LOG_LEVEL, log_file: Optional[str] = None, verbose: bool = False) -> logging.Logger:
  """Configure logging based on arguments."""
  global logger # Allow modification of the global logger variable

  numeric_level = getattr(logging, log_level_str.upper(), None)
  if not isinstance(numeric_level, int):
      print(f"Warning: Invalid log level '{log_level_str}'. Using INFO.", file=sys.stderr)
      numeric_level = logging.INFO

  if verbose:
      numeric_level = logging.DEBUG # Verbose flag overrides log level to DEBUG

  # Define format
  log_format = '%(asctime)s - %(name)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s'
  formatter = logging.Formatter(log_format)

  # Get root logger (or a specific logger)
  logger_instance = logging.getLogger(SCRIPT_NAME)
  logger_instance.setLevel(numeric_level) # Set the lowest level to handle

  # Remove existing handlers to avoid duplication if called multiple times
  for handler in logger_instance.handlers[:]:
      logger_instance.removeHandler(handler)

  # Console Handler (stderr for WARNING+, stdout otherwise)
  class LevelSpecificStreamHandler(logging.Handler):
      def __init__(self, stream_high=sys.stderr, stream_low=sys.stdout, level_threshold=logging.WARNING):
          super().__init__()
          self.stream_high = stream_high
          self.stream_low = stream_low
          self.level_threshold = level_threshold
          self.formatter = formatter # Use the same formatter

      def emit(self, record):
          try:
              msg = self.format(record)
              stream = self.stream_high if record.levelno >= self.level_threshold else self.stream_low

              # Apply colors based on level for console output
              color_code = ""
              if record.levelno >= logging.CRITICAL: color_code = Colors.BOLD + Colors.RED
              elif record.levelno >= logging.ERROR: color_code = Colors.RED
              elif record.levelno >= logging.WARNING: color_code = Colors.YELLOW
              elif record.levelno >= logging.INFO: color_code = Colors.GREEN # Default info color
              elif record.levelno >= logging.DEBUG: color_code = Colors.CYAN

              stream.write(Colors.colorize(msg, color_code) + '\n')
              stream.flush()
          except Exception:
              self.handleError(record)

  console_handler = LevelSpecificStreamHandler()
  console_handler.setLevel(numeric_level) # Handler processes messages at this level or higher
  logger_instance.addHandler(console_handler)

  # File Handler (if path provided)
  if log_file:
      try:
          log_dir = os.path.dirname(log_file)
          if log_dir: # Ensure directory exists only if it's specified
              os.makedirs(log_dir, exist_ok=True)
          # Use RotatingFileHandler or TimedRotatingFileHandler for production scripts
          # Example: file_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
          file_handler = logging.FileHandler(log_file, mode='a') # Append mode
          file_handler.setFormatter(formatter)
          file_handler.setLevel(numeric_level) # Log everything at the specified level to file
          logger_instance.addHandler(file_handler)
          logger_instance.info(f"Logging initialized. Level: {log_level_str.upper()}. Log file: {log_file}")
      except Exception as e:
          logger_instance.error(f"Failed to configure file logging to {log_file}: {e}", exc_info=False)
          print(f"Error: Failed to set up log file at {log_file}. Check permissions and path. {e}", file=sys.stderr)
          # Optionally exit if file logging is critical
          # sys.exit(EXIT_PERMISSION_ERROR)
  else:
      logger_instance.info(f"Logging initialized. Level: {log_level_str.upper()}. Console only.")

  # Set the global logger variable
  logger = logger_instance

  # Set the hook for uncaught exceptions AFTER logger is configured
  sys.excepthook = _log_uncaught_exception

  return logger_instance

def parse_arguments() -> argparse.Namespace:
  """Parse command-line arguments using argparse."""
  parser = argparse.ArgumentParser(
      description="[Brief description matching PURPOSE in docstring]",
      epilog=f"Example: python {SCRIPT_NAME} --verbose --config settings.yaml input.dat",
      formatter_class=argparse.ArgumentDefaultsHelpFormatter # Shows defaults in help
  )

  # Add arguments based on the USAGE section
  parser.add_argument(
      'input_path',
      type=str,
      help='Path to the input data file or directory.'
  )
  parser.add_argument(
      '-v', '--verbose',
      action='store_true',
      help='Enable verbose output (DEBUG level logging).'
  )
  parser.add_argument(
      '-d', '--dry-run',
      action='store_true',
      help='Simulate execution without making changes or writing output.'
  )
  parser.add_argument(
      '--config',
      type=str,
      default=DEFAULT_CONFIG_PATH,
      help='Path to the configuration file.'
  )
  parser.add_argument(
      '--output',
      type=str,
      default=os.path.join(DEFAULT_OUTPUT_DIR, "output.dat"), # Example output filename
      help='Path to the output file or directory.'
  )
  parser.add_argument(
      '--log-file',
      type=str,
      default=DEFAULT_LOG_FILE_PATH, # Use the full default path
      help='Specify the path for the log file.'
  )
  parser.add_argument(
      '--no-log-file',
      action='store_true',
      help='Disable logging to a dedicated file (console only).'
  )
  parser.add_argument(
      '--log-level',
      type=str,
      default=DEFAULT_LOG_LEVEL,
      choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
      help='Set logging level.'
  )
  parser.add_argument(
      '--lock',
      action='store_true',
      help=f'Enable single instance locking using a lock file ({DEFAULT_LOCK_FILE_PATH}). Requires filelock package.'
  )
  parser.add_argument(
      '--version',
      action='version',
      version=f'%(prog)s {__version__}'
  )

  # Add more script-specific arguments here...
  # parser.add_argument('--threshold', type=int, default=90, help='Processing threshold.')

  args = parser.parse_args()

  # Post-processing args if needed
  if args.no_log_file:
      args.log_file = None # Set log_file to None if --no-log-file is used

  return args

def load_configuration(config_path: str) -> Dict[str, Any]:
  """Load configuration from a file (e.g., YAML, JSON, INI)."""
  global config # Allow modification of global config

  if not os.path.exists(config_path):
      if config_path == DEFAULT_CONFIG_PATH:
          logger.warning(f"Default configuration file not found at {config_path}. Using default settings.")
          return {} # Return empty dict, rely on defaults/args
      else:
          # If a specific path was given and not found, it's an error
          logger.error(f"Configuration file specified ('{config_path}') not found.")
          sys.exit(EXIT_CONFIG_ERROR)

  if not os.access(config_path, os.R_OK):
      logger.error(f"Configuration file '{config_path}' is not readable (permission denied).")
      sys.exit(EXIT_PERMISSION_ERROR)

  logger.info(f"Loading configuration from: {config_path}")
  loaded_config = {}
  try:
      file_ext = os.path.splitext(config_path)[1].lower()

      if file_ext in ['.yaml', '.yml'] and yaml:
          with open(config_path, 'r') as f:
              loaded_config = yaml.safe_load(f)
      # Add support for other formats (JSON, INI) if needed
      # elif file_ext == '.json':
      #     import json
      #     with open(config_path, 'r') as f:
      #         loaded_config = json.load(f)
      # elif file_ext == '.ini':
      #     import configparser
      #     parser = configparser.ConfigParser()
      #     parser.read(config_path)
      #     # Convert ConfigParser object to dict (might need specific handling for sections)
      #     loaded_config = {s: dict(parser.items(s)) for s in parser.sections()}
      else:
          logger.error(f"Unsupported configuration file format: {file_ext}. Requires .yaml/.yml (and PyYAML installed).")
          sys.exit(EXIT_CONFIG_ERROR)

      if not isinstance(loaded_config, dict):
          logger.error(f"Configuration file {config_path} did not parse into a dictionary.")
          sys.exit(EXIT_CONFIG_ERROR)

      logger.debug(f"Configuration loaded successfully: {loaded_config}")
      config = loaded_config # Update global config
      return loaded_config

  except Exception as e:
      logger.error(f"Failed to load or parse configuration file {config_path}: {e}", exc_info=True)
      sys.exit(EXIT_CONFIG_ERROR)

def validate_inputs(args: argparse.Namespace, loaded_config: Dict[str, Any]):
  """Perform checks on finalized configuration and inputs before execution."""
  logger.info("Validating inputs and configuration...")

  # Validate input path
  if not os.path.exists(args.input_path):
      logger.critical(f"Input path '{args.input_path}' not found.")
      sys.exit(EXIT_FILE_NOT_FOUND_ERROR)
  if not os.access(args.input_path, os.R_OK):
      logger.critical(f"Input path '{args.input_path}' is not readable (permission denied).")
      sys.exit(EXIT_PERMISSION_ERROR)

  # Validate output directory writability
  output_dir = os.path.dirname(args.output)
  if output_dir: # Only check if it's not just a filename in the current dir
      try:
          os.makedirs(output_dir, exist_ok=True)
          if not os.access(output_dir, os.W_OK):
              raise OSError("Directory not writable")
      except OSError as e:
          logger.critical(f"Output directory '{output_dir}' is not writable or cannot be created: {e}")
          sys.exit(EXIT_PERMISSION_ERROR)

  # Validate log directory writability (if file logging enabled)
  if args.log_file:
      log_dir = os.path.dirname(args.log_file)
      if log_dir:
          try:
              os.makedirs(log_dir, exist_ok=True)
              if not os.access(log_dir, os.W_OK):
                  raise OSError("Directory not writable")
          except OSError as e:
              # Log a warning but don't exit, file logging will fail later if it matters
              logger.warning(f"Log directory '{log_dir}' is not writable or cannot be created: {e}. File logging may fail.")
              # Could disable file logging here if preferred: args.log_file = None

  # Validate specific configuration items if needed
  # Example: Check if a required config key exists
  # required_key = 'api_endpoint'
  # if required_key not in loaded_config:
  #     logger.critical(f"Missing required configuration key: '{required_key}' in {args.config}")
  #     sys.exit(EXIT_CONFIG_ERROR)

  # Validate dependencies required based on config/args
  # Example: If config enables a feature requiring pandas
  # if loaded_config.get('use_pandas_feature', False) and pd is None:
  #     logger.critical("Pandas feature enabled, but the 'pandas' package is not installed.")
  #     print("Please install it: pip install pandas", file=sys.stderr)
  #     sys.exit(EXIT_DEPENDENCY_ERROR)

  logger.info("Input validation passed.")


def prepare_environment(args: argparse.Namespace):
  """Sets up the environment before the main logic runs."""
  global temp_dir, lock # Allow modification of globals
  logger.info("Preparing execution environment...")

  # Load .env file if python-dotenv is installed and .env exists
  if dotenv:
      env_path = os.path.join(SCRIPT_DIR, '.env')
      if os.path.exists(env_path):
          try:
              dotenv.load_dotenv(dotenv_path=env_path, override=False) # override=False doesn't overwrite existing env vars
              logger.info(f"Loaded environment variables from {env_path}")
          except Exception as e:
              logger.warning(f"Could not load .env file at {env_path}: {e}")
      else:
          logger.debug(".env file not found, skipping dotenv loading.")

  # Create a secure temporary directory if needed by the script logic
  # temp_dir = tempfile.mkdtemp(prefix=f"{os.path.splitext(SCRIPT_NAME)[0]}_")
  # logger.debug(f"Created temporary directory: {temp_dir}")
  # Ensure temp_dir is cleaned up via register_cleanup() or try/finally

  # Acquire file lock if requested and library available
  if args.lock:
      if FileLock is None:
          logger.critical("File locking requested (--lock), but the 'filelock' package is not installed.")
          print("Please install it: pip install filelock", file=sys.stderr)
          sys.exit(EXIT_DEPENDENCY_ERROR)
      try:
          lock_path = DEFAULT_LOCK_FILE_PATH # Use the default path
          # Ensure lock directory exists (usually /tmp)
          lock_dir = os.path.dirname(lock_path)
          try:
              os.makedirs(lock_dir, exist_ok=True)
          except OSError:
               # Permissions issue? Log and potentially exit or just warn.
               logger.warning(f"Could not ensure lock directory exists: {lock_dir}. Locking may fail.")

          logger.info(f"Attempting to acquire lock file: {lock_path}")
          lock = FileLock(lock_path, timeout=1) # Timeout=1 means try once, don't wait
          lock.acquire()
          logger.info("Lock acquired.")
          # Register lock release in cleanup
          register_cleanup(release_lock)
      except Timeout:
          logger.error(f"Another instance of the script may be running (Lock file '{lock_path}' is held). Exiting.")
          sys.exit(EXIT_GENERAL_ERROR) # Or a specific exit code for lock contention
      except Exception as e:
          logger.error(f"Failed to acquire lock file {lock_path}: {e}", exc_info=True)
          # Decide whether to exit or continue without lock
          sys.exit(EXIT_GENERAL_ERROR)

  # Create Output/Log directories (validation already checked writability)
  if os.path.dirname(args.output):
      os.makedirs(os.path.dirname(args.output), exist_ok=True)
  if args.log_file and os.path.dirname(args.log_file):
      os.makedirs(os.path.dirname(args.log_file), exist_ok=True)

  logger.info("Environment preparation complete.")

# --- Cleanup Handling ---
_cleanup_functions = []

def register_cleanup(func, *args, **kwargs):
  """Register a function to be called on script exit."""
  _cleanup_functions.append((func, args, kwargs))
  logger.debug(f"Registered cleanup function: {func.__name__}")

def run_cleanup():
  """Execute registered cleanup functions in reverse order."""
  logger.info("Performing cleanup...")
  # Functions are called in reverse order of registration
  for func, args, kwargs in reversed(_cleanup_functions):
      try:
          logger.debug(f"Running cleanup function: {func.__name__}")
          func(*args, **kwargs)
      except Exception as e:
          logger.error(f"Error during cleanup function {func.__name__}: {e}", exc_info=True)
  logger.info("Cleanup finished.")

def cleanup_temp_dir():
  """Removes the temporary directory if created."""
  global temp_dir
  if temp_dir and os.path.exists(temp_dir):
      try:
          import shutil
          shutil.rmtree(temp_dir)
          logger.debug(f"Removed temporary directory: {temp_dir}")
          temp_dir = None
      except Exception as e:
          logger.warning(f"Failed to remove temporary directory {temp_dir}: {e}")

def release_lock():
  """Releases the file lock if acquired."""
  global lock
  if lock and lock.is_locked:
      try:
          lock.release()
          logger.info(f"Released lock file: {lock.lock_file}")
          lock = None
      except Exception as e:
          logger.error(f"Failed to release lock file {lock.lock_file}: {e}")


# --- Signal Handling ---
def signal_handler(signum, frame):
  """Handle termination signals gracefully."""
  signal_name = signal.Signals(signum).name
  logger.warning(f"Received signal: {signal_name} ({signum}). Initiating shutdown...")
  # Cleanup is handled by atexit, just exit with appropriate code
  if signum == signal.SIGINT:
      sys.exit(EXIT_KEYBOARD_INTERRUPT)
  else:
      sys.exit(EXIT_GENERAL_ERROR) # General error for TERM, HUP etc.

# =========================================================================================
# MAIN EXECUTION LOGIC
# =========================================================================================
def main_logic(args: argparse.Namespace, loaded_config: Dict[str, Any]):
  """Contains the core functionality of the script."""
  logger.info("Starting main script execution...")
  logger.info(f"Running with: Input='{args.input_path}', Config='{args.config}', Output='{args.output}', DryRun={args.dry_run}")
  # Access config values like: loaded_config.get('setting_name', default_value)

  # -----------------------------------------------------
  # TODO: Implement the core functionality of your script here.
  # -----------------------------------------------------
  # Example Steps:

  # 1. Read data from input source (e.g., args.input_path)
  logger.info(f"Reading input from: {args.input_path}")
  try:
      with open(args.input_path, 'r') as f:
          # Process line by line or read all content based on needs
          line_count = 0
          for line in f:
              line_count += 1
              # logger.debug(f"Read line: {line.strip()}")
              # Process the line...
          logger.info(f"Successfully read {line_count} lines from {args.input_path}")

  except FileNotFoundError:
      logger.error(f"Input file not found during processing: {args.input_path}")
      sys.exit(EXIT_FILE_NOT_FOUND_ERROR)
  except PermissionError:
      logger.error(f"Permission denied reading input file: {args.input_path}")
      sys.exit(EXIT_PERMISSION_ERROR)
  except Exception as e:
      logger.error(f"An error occurred reading {args.input_path}: {e}", exc_info=True)
      sys.exit(EXIT_DATA_ERROR) # Or general error

  # 2. Perform actions based on data and configuration
  logger.info("Performing main processing task...")
  # result = process_data(data, loaded_config) # Call your processing functions

  # Simulate work
  import time
  time.sleep(1)
  processed_result = f"Processed data from {args.input_path} with config {args.config}"


  # 3. Handle Dry Run mode
  if args.dry_run:
      logger.warning("[DRY RUN] Skipping output writing and actual changes.")
      # Show what would have been done
      logger.info(f"[DRY RUN] Would write result to: {args.output}")
      logger.info(f"[DRY RUN] Result preview: {processed_result[:100]}...")
  else:
      # 4. Write results to output destination (e.g., args.output)
      logger.info(f"Writing output to: {args.output}")
      try:
          output_dir = os.path.dirname(args.output)
          if output_dir: os.makedirs(output_dir, exist_ok=True) # Ensure dir exists

          with open(args.output, 'w') as f:
              f.write(processed_result + '\n')
          logger.info(f"Successfully wrote results to {args.output}")

      except PermissionError:
          logger.error(f"Permission denied writing output file: {args.output}")
          sys.exit(EXIT_PERMISSION_ERROR)
      except Exception as e:
          logger.error(f"An error occurred writing to {args.output}: {e}", exc_info=True)
          sys.exit(EXIT_GENERAL_ERROR)


  # -----------------------------------------------------
  # End of core functionality
  # -----------------------------------------------------

  logger.info("Main execution logic finished successfully.")


# =========================================================================================
# SCRIPT EXECUTION FLOW / ENTRY POINT
# =========================================================================================
if __name__ == "__main__":
  # --- Essential Setup ---
  # Ensure cleanup runs even if errors occur early
  atexit.register(run_cleanup)

  # Register signal handlers for graceful shutdown
  signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C
  signal.signal(signal.SIGTERM, signal_handler) # kill
  if hasattr(signal, 'SIGHUP'): # SIGHUP might not be available on Windows
      signal.signal(signal.SIGHUP, signal_handler) # Terminal close/hangup

  # Register cleanup for temp dir if used (can be done here or in prepare_environment)
  # register_cleanup(cleanup_temp_dir)

  # --- Initialize Exit Code ---
  exit_code = EXIT_SUCCESS

  try:
      # 1. Parse Command Line Arguments
      args = parse_arguments()

      # 2. Setup Logging (as early as possible, using args)
      # If logging setup fails critically, it might exit inside the function
      logger = setup_logging(log_level_str=args.log_level, log_file=args.log_file, verbose=args.verbose)

      logger.debug(f"Script started: {' '.join(sys.argv)}")
      logger.debug(f"Parsed Arguments: {args}")
      logger.debug(f"Script Version: {__version__}, Python Version: {sys.version.split()[0]}")

      # 3. Load Configuration File
      loaded_config = load_configuration(args.config)

      # 4. Validate Inputs and Configuration
      validate_inputs(args, loaded_config)

      # 5. Prepare Environment (Temp dirs, Locks, etc.)
      prepare_environment(args)

      # 6. Execute Main Logic
      main_logic(args, loaded_config)

      logger.info("Script completed successfully.")

  except KeyboardInterrupt:
      logger.warning("Script interrupted by user (Ctrl+C).")
      exit_code = EXIT_KEYBOARD_INTERRUPT
      # Cleanup is handled by atexit

  except SystemExit as e:
      # sys.exit() was called directly, likely with a specific code
      exit_code = e.code
      if exit_code == 0:
          logger.info("Script exited cleanly via sys.exit(0).")
      else:
          # Error should have been logged before exiting
          logger.error(f"Script exited with code: {exit_code}. Check previous logs for details.")

  except Exception as e:
      # Catch-all for unexpected errors NOT handled by sys.excepthook (e.g., during setup before hook is set)
      # If sys.excepthook ran, it would have logged; this is a fallback.
      if logger:
          logger.critical(f"An unexpected error occurred: {e}", exc_info=True)
      else:
          # Logger failed or wasn't set up
          print(f"CRITICAL: An unexpected error occurred before logging was fully configured: {e}", file=sys.stderr)
          traceback.print_exc(file=sys.stderr)
      exit_code = EXIT_GENERAL_ERROR

  finally:
      # run_cleanup() is registered with atexit, so it will run automatically
      # No need to explicitly call it here unless atexit fails or isn't used.
      # release_lock() # Example: if lock needs release *before* other cleanup

      # Ensure we exit with the determined code
      if exit_code == EXIT_SUCCESS:
           logger.debug(f"Exiting with status code: {exit_code} (Success)")
      else:
           logger.error(f"Exiting with status code: {exit_code} (Failure)")

      sys.exit(exit_code)

# =========================================================================================
# --- End of Script ---

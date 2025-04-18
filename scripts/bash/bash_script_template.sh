#!/bin/bash

# =========================================================================================
# SCRIPT METADATA
# =========================================================================================
# SCRIPT NAME   : [your_script_name.sh]
# PURPOSE       : [Concisely state the script's primary goal or function. What problem does it solve?]
#                 [Example: Automate the backup of critical configuration files to a remote server.]
# -----------------------------------------------------------------------------------------
# AUTHOR        : [Your Name / Primary Maintainer Name]
# TEAM          : [Your Team Name, if applicable, optional]
# ORGANIZATION  : [Your Organization Name, if applicable, optional]
# CONTACT       : [Your Email / Team Distribution List / Preferred Contact Method]
# WEBSITE       : [Link to relevant website, project page, or documentation, optional]
# PROFILE       : [Optional: Link to Author's LinkedIn/GitHub profile]
# REPOSITORY    : [Link to the script's code repository (e.g., GitHub, GitLab), optional]
# LICENSE       : [Specify the license, e.g., MIT, GPLv3, Apache 2.0. Consider adding full text at end or linking.]
# CREATED ON    : [YYYY-MM-DD - The date the script was initially created.]
# LAST UPDATED  : [YYYY-MM-DD - The date of the last significant modification.]
# VERSION       : [Semantic Versioning recommended, e.g., 1.0.0]
# =========================================================================================

# =========================================================================================
# DESCRIPTION
# =========================================================================================
# [Provide a comprehensive explanation of the script's functionality. Describe its features,
# the problem it addresses in more detail, and its general workflow or operational logic.
# Use bullet points for clarity when outlining key steps or functions.]
#
# Example:
# This script automates the process of checking disk usage on multiple remote servers listed
# in a configuration file. It connects via SSH, runs 'df -h', parses the output, flags
# filesystems exceeding a defined threshold, and generates a consolidated CSV report.
# It leverages sshpass for non-interactive logins (ensure security implications are understood).
#
# Key Workflow / Functions:
# - Reads server list and credentials from a specified file (default: './servers.conf').
# - Parses command-line arguments for threshold percentage, output file, etc.
# - Iterates through each server in the list.
# - Establishes an SSH connection using provided credentials.
# - Executes 'df -h' command remotely.
# - Parses the output to extract filesystem usage percentages.
# - Compares usage against the threshold.
# - Logs connection errors or command failures.
# - Appends results (server, filesystem, usage, status) to a CSV file.
# - Provides summary output to stdout upon completion.
# =========================================================================================

# =========================================================================================
# DESIGN PHILOSOPHY
# =========================================================================================
# [Explain the core principles or rationale behind the script's design (optional but helpful).]
# - **[Modularity]:** [e.g., Uses functions for distinct tasks like connecting, fetching data, parsing, logging.]
# - **[Robustness]:** [e.g., Includes error handling for SSH connection failures, command errors, missing files.]
# - **[Readability]:** [e.g., Employs clear variable names, comments for complex logic, consistent formatting.]
# - **[Simplicity/Complexity]:** [e.g., Balances necessary features with ease of understanding and maintenance.]
# - **[Efficiency]:** [e.g., Minimizes remote commands, uses efficient text processing tools like awk/sed.]
# - **[Automation]:** [e.g., Designed for unattended execution (e.g., via cron), requires minimal user interaction.]
# =========================================================================================

# =========================================================================================
# PRIMARY AUDIENCE
# =========================================================================================
# [Specify the intended users or roles for this script.]
# - [e.g., System Administrators responsible for server monitoring.]
# - [e.g., DevOps Engineers managing infrastructure health.]
# - [e.g., IT Support Teams performing routine checks.]
# - [e.g., Developers needing automated environment setup.]
# - [e.g., End Users (if designed for general use)]
# =========================================================================================

# =========================================================================================
# USAGE
# =========================================================================================
# **Permissions:**
# - Script execution: `chmod +x [your_script_name.sh]`
# - File system access: [e.g., Read access to config file(s), Write access to output directory/log file.]
# - Network access: [e.g., Outbound connections on port 22 (SSH) to target servers.]
# - Elevated privileges: [e.g., Requires `sudo` or root privileges for specific commands like `mount`, `apt install`.]
#   [Explain *why* elevated privileges are needed, if applicable.]
#
# **Basic Syntax:**
# `./[your_script_name.sh] [options] [arguments]`
#
# **Options:**
#   -h, --help          Display this help message and exit.
#   -v, --verbose       Enable verbose output (more detailed logging to stdout/stderr).
#   -d, --debug         Enable Bash debug mode (`set -x`), prints every command before execution.
#   --dry-run           Simulate execution, showing intended actions without making changes.
#   -c, --config FILE   Specify the path to the configuration file (Default: './config.conf').
#   -o, --output FILE   Specify the path for the output report file (Default: './output/report.csv').
#   -t, --threshold INT Set the usage percentage threshold (Default: 85).
#   [Add other script-specific options with short and long forms if applicable]
#   [Example: -u, --user USER Specify the remote SSH user (Overrides config file)]
#
# **Arguments:**
#   [ARG_1]             [Description of the first required/optional positional argument. Specify if required.]
#                       [Example: SERVER_LIST_FILE - Path to a file containing server hostnames or IPs.]
#   [ARG_2]             [Description of the second argument...]
#                       [Example: TARGET_DIRECTORY - Directory on remote servers to check.]
#
# **Common Examples:**
# 1. Run with default settings, using './servers.conf' and threshold 85:
#    `./[your_script_name.sh] ./servers.conf`
#
# 2. Run with a specific config file, verbose output, and 90% threshold:
#    `./[your_script_name.sh] -v -c /etc/script/prod_servers.conf -t 90 ./prod_servers.conf`
#
# 3. Perform a dry run to see what would happen:
#    `./[your_script_name.sh] --dry-run ./servers.conf`
#
# 4. Get help:
#    `./[your_script_name.sh] --help`
#
# **Advanced Execution (Automation):**
# - Example cron job running daily at 2:15 AM, logging to a dedicated file:
#   `15 2 * * * /path/to/your_script_name.sh -c /etc/script/config.conf /path/to/server_list >> /var/log/script_name.log 2>&1`
# - Example systemd service integration: Create a unit file (e.g., `/etc/systemd/system/script_name.service`)
#   and a timer file. Refer to systemd documentation for specifics (`man systemd.service`, `man systemd.timer`).
# =========================================================================================

# =========================================================================================
# INSTALLATION / DEPLOYMENT
# =========================================================================================
# **Recommended Location:**
# - User scripts: `~/bin/` or `~/.local/bin/` (ensure these are in user's $PATH)
# - System-wide scripts (requiring root): `/usr/local/sbin/` or `/usr/local/bin/`
# - Project-specific scripts: Within the project directory structure.
#
# **Manual Setup:**
# 1. Place the script in the chosen location (e.g., `/usr/local/bin/`).
# 2. Set appropriate ownership: `sudo chown root:root /usr/local/bin/[your_script_name.sh]` (if system-wide)
# 3. Set executable permissions: `sudo chmod 755 /usr/local/bin/[your_script_name.sh]` (if system-wide)
#    or `chmod +x [your_script_name.sh]` (for user scripts).
# 4. Install required dependencies (see DEPENDENCIES section).
# 5. Create necessary configuration files (e.g., copy `config.example` to `config.conf` and edit).
# 6. Create necessary directories (e.g., `mkdir /var/log/script_name`, `chown user:group /var/log/script_name`).
# 7. Run the script initially with `--help` or `--dry-run` to test.
#
# **Integration (Optional):**
# - **Systemd Service:** Provide example unit files (`.service`, `.timer`) or link to them if complex.
# - **Cron Job:** Ensure the cron environment has the necessary PATH and variables. Use full paths.
# - **Configuration Management:** Integrate deployment via Ansible, Puppet, Chef, SaltStack, etc.
# =========================================================================================

# =========================================================================================
# DEPENDENCIES & ENVIRONMENT
# =========================================================================================
# **Required Interpreter:**
# - `/bin/bash`: The Bourne-Again SHell interpreter (Version >= X.Y recommended, if known features used).
#                Using `#!/bin/bash` enables Bash-specific features (bashisms).
#                Use `#!/bin/sh` for stricter POSIX sh compatibility if bashisms are avoided [6].
#
# **Required System Binaries/Tools:**
# - `coreutils`: Provides fundamental tools like `date`, `mkdir`, `chmod`, `cat`, `wc`, `head`, `sort`, `cut`, `basename`, `dirname`, `mktemp`.
# - `grep`: For pattern searching (specify version if advanced features like PCRE [-P] are used).
# - `awk`: For text processing (specify version if specific features are used).
# - `sed`: For stream editing.
# - `command`: Bash built-in for checking command existence.
# - `getopt`/`getopts`: For parsing command-line options (getopt is external, getopts is a Bash built-in).
# - [Add other tools with purpose and minimum version if critical]
# - `[tool1, e.g., sshpass]`: [Purpose: e.g., For non-interactive SSH password authentication (Security Warning: exposes password)] (Version >= X.Y if specific)
# - `[tool2, e.g., curl/wget]`: [Purpose: e.g., For downloading files or interacting with web APIs]
# - `[tool3, e.g., jq]`: [Purpose: e.g., For parsing JSON data]
# - `[tool4, e.g., rsync]`: [Purpose: e.g., For efficient file synchronization]
#
# **Setup Instructions (if dependencies are not standard):**
# - Example installation (Debian/Ubuntu):
#   `sudo apt update && sudo apt install -y sshpass jq curl`
# - Example installation (RHEL/CentOS/Fedora):
#   `sudo dnf update && sudo dnf install -y openssh-clients jq curl` (sshpass might be in EPEL)
# - Check availability: `command -v jq`
# - Check version: `jq --version`
#
# **Operating System Compatibility:**
# - Designed primarily for: [e.g., Linux distributions like Ubuntu 20.04+, CentOS 7+, Debian 10+]
# - Known compatibility issues: [e.g., May require adjustments for macOS (different sed/grep flags), BSD variants, or older Linux versions.]
# - Windows Subsystem for Linux (WSL): [e.g., Tested and working on WSL2.]
#
# **Environment Variables Used:**
# - `[VAR_NAME_1, e.g., EDITOR]`: [Purpose, e.g., Used to open config file for editing if specified.]
# - `[VAR_NAME_2, e.g., SSHPASS]`: [Purpose, e.g., Can be used by sshpass utility to read password.] (Security Warning)
# - `[VAR_NAME_3, e.g., CUSTOM_API_KEY]`: [Purpose, e.g., API key needed for interacting with Service X.]
# - `PATH`: Standard variable, ensure required binaries are locatable.
#
# **System Resource Requirements:**
# - Minimum: [Estimate baseline needs, e.g., 1 vCPU, 256MB RAM, 50MB Disk Space]
# - Recommended: [Estimate for typical workload, e.g., 1 vCPU, 512MB RAM, 200MB Disk Space + space for logs/output]
# - Peak Usage: [Mention if specific operations cause spikes, e.g., High network I/O during rsync, high CPU during data processing.]
# =========================================================================================

# =========================================================================================
# LOGGING MECHANISM
# =========================================================================================
# **Log Destination(s):**
# - Standard Output (stdout): [Normal operational messages, progress updates, final summary results.]
# - Standard Error (stderr): [Error messages, warnings, verbose debug output if enabled.]
# - Dedicated Log File: [Yes/No. Path: e.g., `/var/log/[script_name]/[script_name].log` or `./logs/[script_name]_[timestamp].log`]
#   [Specify ownership/permissions if relevant, e.g., `root:adm` 640]
# - System Log (syslog/journald): [Yes/No. If Yes, specify facility (e.g., `local0`) and tag (e.g., `[script_name]`).]
#   [Example command to view journald logs: `journalctl -t [script_name] -f`]
#
# **Log Format:**
# - [Describe the format used for log messages.]
# - Example File/Stdout Format: `[YYYY-MM-DD HH:MM:SS UTC] [LEVEL] [Function:Line] - Message`
# - Example Syslog Format: Uses standard syslog format, message prepended with `[LEVEL]: Message`.
#
# **Log Levels (if implemented):**
# - `DEBUG`: Very detailed information for troubleshooting (Enabled by `--verbose` or `--debug`).
# - `INFO`: General operational messages, start/stop, major steps completed.
# - `WARN`: Potential issues encountered, non-critical errors, recoverable problems.
# - `ERROR`: Significant errors that likely prevent task completion or cause partial failure.
# - `CRITICAL`: Severe errors causing script termination.
# - Control: [How is level controlled? e.g., Command-line flag (`--log-level LEVEL`), config file setting.]
#
# **Log Rotation (if using a dedicated file):**
# - Handled by script?: [Yes/No. If Yes, describe mechanism (e.g., size/date based).]
# - External Recommendation: Usually best handled by external tools like `logrotate`.
# - Example `logrotate` configuration (`/etc/logrotate.d/[script_name]`):
#   ```
#   /var/log/[script_name]/[script_name].log {
#       daily                   # Rotate logs daily
#       rotate 7                # Keep 7 days of backups
#       compress                # Compress rotated logs
#       delaycompress           # Don't compress the most recent backup immediately
#       missingok               # Don't error if log file is missing
#       notifempty              # Don't rotate if the log is empty
#       create 0640 root adm    # Create new log file with specific permissions/ownership
#       sharedscripts           # Run postrotate script once even if multiple logs match
#       postrotate
# Commands to run after rotation (e.g., signal a daemon to reopen log file)
# systemctl reload my-daemon.service > /dev/null 2>&1 || true
#       endscript
#   }
#   ```
# =========================================================================================

# =========================================================================================
# OUTPUTS
# =========================================================================================
# [Describe the primary outputs generated by the script.]
#
# **Standard Output (stdout):**
# - Normal Operation: [e.g., Prints status messages like "Connecting to server X...", "Processing file Y...", "Task Z complete."]
# - Data Output: [e.g., If the script's main purpose is data transformation, describe the format (CSV, JSON lines, plain text list).]
# - Summary: [e.g., Often ends with a summary: "Processed 10 servers, 2 errors, report generated at /path/to/report.csv".]
#
# **Standard Error (stderr):**
# - Errors: [e.g., Prints error messages like "ERROR: Connection to server X failed.", "ERROR: Config file not found."]
# - Warnings: [e.g., Prints warnings like "WARN: Server X response timed out, retrying...", "WARN: Using default threshold."]
# - Debug/Verbose Output: [e.g., If `-v` or `-d` is used, detailed step-by-step execution info may appear here.]
#
# **Generated/Modified Files:**
# - Log File: [Path as defined in LOGGING section. Contains detailed execution trace.]
# - Report/Data File: [e.g., `output/report_[TIMESTAMP].csv` - Contains results of the operation in CSV format (columns: Server, Check, Status, Details).]
# - Temporary Files: [e.g., Creates files in `/tmp/[script_name].XXXXXX/`. Mention if they are automatically cleaned up via `trap`.]
# - Configuration Files Modified: [e.g., Might update a status file `~/.config/[script_name]/last_run_status`.]
# - Other Outputs: [e.g., Downloads files to `./downloads/`, creates lock file `/var/run/[script_name].pid`.]
# =========================================================================================

# =========================================================================================
# ERROR HANDLING & CONSIDERATIONS
# =========================================================================================
# **Exit Codes:**
# - 0: Success - Script completed all tasks successfully.
# - 1: General Error - Unspecified failure or catch-all for uncaught errors.
# - 2: Dependency Error - Required command or tool not found or incompatible version.
# - 3: Configuration Error - Invalid or missing configuration file, bad syntax within config.
# - 4: Argument Error - Invalid or missing command-line arguments or options.
# - 5: Permission Denied - Insufficient privileges for file access, network operation, or command execution.
# - 6: File System Error - Cannot read/write file/directory, disk full, etc.
# - 7: Network Error - Cannot resolve hostname, connection refused/timed out, API error.
# - [Add other specific exit codes (e.g., 10: Remote command failed, 11: Threshold exceeded) and their meanings.]
#
# **Potential Issues & Troubleshooting:**
# - **Issue:** "Permission Denied" when accessing files/directories.
#   **Resolution:** Check script's user privileges (`whoami`). Check file/directory permissions (`ls -ld /path/to/resource`). Run with `sudo` if appropriate and necessary.
# - **Issue:** "Command Not Found: [tool_name]".
#   **Resolution:** Ensure the tool is installed (see DEPENDENCIES). Check the system's `$PATH` environment variable (`echo $PATH`). Use full path to the command if necessary.
# - **Issue:** SSH connection fails ("Connection refused", "Timed out", "Host key verification failed").
#   **Resolution:** Verify network connectivity (`ping`, `traceroute`). Check firewall rules on client and server. Ensure SSH daemon is running on the server. Check SSH keys/passwords. Handle host keys (`ssh-keyscan`, `StrictHostKeyChecking=no` - Security Warning).
# - **Issue:** Script fails silently in cron.
#   **Resolution:** Redirect stdout/stderr in cron command (`>> /var/log/script.log 2>&1`). Ensure cron environment has necessary `$PATH` or source profile (`. ~/.bash_profile`). Use full paths for all commands/files.
#
# **Important Considerations / Warnings:**
# - **[CRITICAL WARNING: Data Modification/Deletion Risk]**
#   [If the script modifies or deletes data (e.g., uses `rm`, `rsync --delete`, modifies databases/configs), state this CLEARLY.]
#   [Example: "This script uses `rm -rf` on directories specified in the config. **THERE IS NO UNDO.** Triple-check configuration. Always use `--dry-run` first. Ensure backups are available."]
# - **[Security Warning: Sensitive Data Handling]**
#   [If handling passwords, API keys, PII: Explain how. **Strongly advise against hardcoding.** Recommend environment variables, secure config files (strict permissions 600), secrets management tools (Vault, AWS Secrets Manager), or prompting user.]
#   [Example: "Uses `sshpass` which exposes passwords in process list (`ps aux`). Use SSH keys for better security."]
# - **[Idempotency]:** [Can the script be run multiple times with the same input and achieve the same final state without unintended side effects? Yes/No/Partially. Explain.]
# - **[Resource Usage]:** [Can this script consume significant CPU, memory, disk I/O, or network bandwidth? Advise monitoring during initial runs.]
# - **[Concurrency/Locking]:** [Is the script safe to run multiple instances simultaneously? Does it implement locking (e.g., `flock`, PID file) to prevent race conditions?]
# - **[Rate Limiting]:** [If interacting with APIs or services, are there rate limits? Does the script handle them (e.g., sleep, backoff)?]
# - **[Atomicity]:** [Are critical operations performed atomically? What happens if the script is interrupted mid-operation?]
# =========================================================================================

# =========================================================================================
# ASSUMPTIONS
# =========================================================================================
# [List any assumptions the script makes about its execution environment or input data.]
# - Assumes a Bash (v4+) environment with access to standard core utilities.
# - Assumes required dependencies (listed above) are installed and in the system `$PATH`.
# - Assumes necessary network connectivity (e.g., DNS resolution, firewall rules) is in place.
# - Assumes configuration files (`config.conf`, `servers.conf`) exist in the expected location or are specified via arguments, and are correctly formatted.
# - Assumes target systems are reachable via SSH and configured for the authentication method used (keys/password).
# - Assumes the script is executed with appropriate user privileges (e.g., root if modifying system files, user with SSH access).
# - Assumes input data (if any) conforms to the expected format.
# - [e.g., Assumes target servers have '/var/log' directory writable by the remote user.]
# =========================================================================================

# =========================================================================================
# PERFORMANCE OPTIMIZATION (Optional - Fill if relevant)
# =========================================================================================
# **Benchmarks:**
# - [Provide performance metrics if available/relevant.]
#   [Example: Processing 100 servers takes ~5 minutes on a system with X specs.]
#   [Example: Processing a 1GB log file takes ~30 seconds.]
# **Resource Consumption Profile:**
# - CPU: [e.g., Generally low, spikes during `awk`/`sed` processing.]
# - Memory: [e.g., Typically uses < 100MB RAM.]
# - Disk I/O: [e.g., High read activity when processing large files, moderate write for logs/reports.]
# - Network: [e.g., Dependent on number of SSH connections and data transferred.]
# **Optimization Notes:**
# - [Mention specific techniques used.]
#   [e.g., Minimized SSH connections by batching commands.]
#   [e.g., Used `awk` instead of multiple `grep`/`cut` calls for efficiency.]
#   [e.g., Implemented parallel processing using `xargs -P` or `parallel` (requires additional dependency).]
#   [e.g., Potential Bottleneck: Network latency when connecting to many remote servers.]
# =========================================================================================

# =========================================================================================
# TESTING & VALIDATION (Optional - Describe testing efforts)
# =========================================================================================
# **Test Strategy:**
# - [e.g., Manual testing, Automated unit tests (using Bats, shunit2), Integration tests.]
# **Key Test Cases Covered:**
# - [e.g., Handles missing configuration files gracefully.]
# - [e.g., Correctly parses valid command-line arguments.]
# - [e.g., Rejects invalid command-line arguments with helpful error messages.]
# - [e.g., Handles SSH connection failures (timeout, auth error) without crashing.]
# - [e.g., Correctly processes data/input under various conditions (empty, large, special characters).]
# - [e.g., `--dry-run` mode simulates actions accurately.]
# - [e.g., Exit codes correctly reflect success/failure conditions.]
# **Validation Environment:**
# - Tested OS: [e.g., Ubuntu 22.04 LTS, CentOS Stream 9, macOS Monterey]
# - Tested Bash Version(s): [e.g., 5.1.16]
# - Tested Dependencies: [e.g., jq 1.6, sshpass 1.09]
# **Automation:**
# - [e.g., Unit tests integrated into CI/CD pipeline (GitHub Actions, GitLab CI).]
# - [e.g., Static analysis performed using ShellCheck.]
# =========================================================================================

# =========================================================================================
# FUTURE ROADMAP / POTENTIAL IMPROVEMENTS
# =========================================================================================
# [List planned features, known limitations, or ideas for future enhancement.]
# - [Feature 1: Add support for reading server list from an external inventory source (e.g., Ansible inventory, API).]
# - [Feature 2: Implement output in JSON format in addition to CSV.]
# - [Improvement 1: Enhance error handling for specific remote command failures.]
# - [Improvement 2: Add support for SSH key-based authentication with passphrase handling.]
# - [Improvement 3: Implement parallel execution for faster processing of multiple servers.]
# - [Compatibility 1: Add specific checks/workarounds for macOS compatibility.]
# - [Refactoring 1: Break down the main processing loop into smaller, more testable functions.]
# - [Known Limitation: Does not currently support IPv6 addresses.]
# =========================================================================================

# =========================================================================================
# SECURITY CONSIDERATIONS
# =========================================================================================
# - **Privilege Level:** [Requires root/sudo? If so, for which specific operations? Justify. Strive for least privilege.]
#   [Example: Needs sudo only for installing dependencies if missing, otherwise runs as user.]
# - **Input Sanitization:** [How is input from command-line arguments, config files, or external sources validated/sanitized?]
#   [Example: Arguments checked for expected format (numbers, paths). File paths are validated. **Caution needed if user input constructs commands.**]
# - **Sensitive Data Handling:** [Passwords, API keys, Tokens. How are they stored/transmitted? **AVOID HARDCODING.**]
#   [Recommendations: Use environment variables, secure config files (chmod 600), OS keychain, dedicated secrets management tools (Vault), or interactive prompts.]
#   [Example: Reads SSH password from environment variable `SSHPASS` or prompts user if not set. Warns about `sshpass` insecurity.]
# - **Dependencies:** [Are the external tools/libraries trusted? Any known CVEs? Keep them updated.]
#   [Example: Relies on standard OS tools. `jq` is from trusted repo. `sshpass` version X known to be stable.]
# - **File Permissions:** [What permissions are set on created files/directories (logs, output, config, temp)? Use secure defaults.]
#   [Example: Logs created with 640 (owner/group read). Output files with 644. Temp files created with `mktemp` (secure by default). Config files should be 600 if sensitive.]
# - **External Command Execution:** [Does the script build and execute commands dynamically using user input? High risk of command injection if not handled carefully.]
#   [Example: Uses static commands mostly. If dynamic, ensure variables are quoted properly and input is strictly validated/escaped.]
# - **Network Exposure:** [Does it listen on ports? Connect to external services? Over what protocols (HTTP/HTTPS, SSH)?]
#   [Example: Makes outbound SSH connections to servers listed in config. Uses standard port 22.]
# - **Code Integrity:** [If distributing the script, recommend users verify integrity.]
#   [Example: Provide checksums (SHA256) for releases: `sha256sum [your_script_name.sh]`]
# - **Error Message Verbosity:** [Ensure error messages do not leak sensitive information (e.g., full paths, keys) to unauthorized users/logs.]
# =========================================================================================

# =========================================================================================
# DOCUMENTATION
# =========================================================================================
# - Primary documentation is within this script's header comments.
# - External documentation (if applicable):
#   - README: [Link to README.md in repository, if exists]
#   - Wiki: [Link to project Wiki, if exists]
#   - Man Page: [If a man page is provided: `man [script_name]`]
#   - Confluence/Internal Docs: [Link if relevant]
# =========================================================================================

# =========================================================================================
# SUPPORT & CONTACT
# =========================================================================================
# - Author/Maintainer: [Your Name / Team Name]
# - Contact: [Your Email / Team Distribution List / Slack Channel]
# - Bug Reports/Issues: [Link to GitHub Issues page, Jira project, or specific contact email.]
# - Feature Requests: [Process for submitting feature requests, e.g., GitHub Issues.]
# =========================================================================================

# =========================================================================================
# SCRIPT EXECUTION ENVIRONMENT & CONFIGURATION
# =========================================================================================

# --- Bash Strict Mode ---
# -e: Exit immediately if a command exits with a non-zero status.
# -u: Treat unset variables and parameters as an error when performing parameter expansion.
# -o pipefail: The return value of a pipeline is the status of the last command to exit with a non-zero status,
#              or zero if no command exited with a non-zero status.
# Tip: Consider commenting out '-e' if you have commands that might fail but you want to handle the error locally
#      using `if ! command; then ...; fi` or `command || handle_error`.
set -euo pipefail

# --- Debug Mode ---
# Uncomment the following line for debugging purposes:
# Prints each command and its arguments to stderr before it is executed.
# set -x

# --- Script Information ---
# Use BASH_SOURCE[0] instead of $0 for better portability and handling symlinks.
readonly SCRIPT_NAME="$(basename "${BASH_SOURCE[0]}")"
# Resolve the absolute path of the script's directory, handling symlinks.
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
readonly SCRIPT_DIR="${SOURCE_DIR}"
readonly SCRIPT_PID=$$

# --- Timestamp ---
readonly SCRIPT_RUN_TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# --- Global Runtime Variables ---
# These variables store the script's configuration and state.
# Defaults can be overridden by command-line arguments or configuration files.

# Configuration Defaults
VERBOSE=false                # Boolean flag for verbose output
DEBUG_MODE=false             # Boolean flag for debug mode (set -x)
DRY_RUN=false                # Boolean flag for dry run mode (simulate actions)
NO_COLOR=false               # Boolean flag to disable colored output
INTERACTIVE_MODE=false       # Boolean flag indicating if running in an interactive terminal
[[ -t 1 ]] && INTERACTIVE_MODE=true # Check if stdout is a terminal

# Default Paths (adjust as needed)
DEFAULT_CONFIG_FILE="${SCRIPT_DIR}/config.conf" # Default config file path
DEFAULT_OUTPUT_DIR="${SCRIPT_DIR}/output"       # Default directory for output files
DEFAULT_LOG_DIR="${SCRIPT_DIR}/logs"            # Default directory for log files
DEFAULT_LOG_FILE="${DEFAULT_LOG_DIR}/${SCRIPT_NAME%.sh}_${SCRIPT_RUN_TIMESTAMP}.log" # Default log file path
DEFAULT_TMP_DIR_BASE="/tmp"                     # Base directory for temporary files

# Script-specific Defaults (replace with your script's needs)
THRESHOLD_DEFAULT=85
REMOTE_USER_DEFAULT=$(whoami)
SERVER_LIST_DEFAULT=""       # Example: Path to a server list file

# Runtime variables that will be populated later
CONFIG_FILE="${DEFAULT_CONFIG_FILE}"
OUTPUT_DIR="${DEFAULT_OUTPUT_DIR}"
LOG_FILE="${DEFAULT_LOG_FILE}"
LOG_TO_FILE=true             # Control whether logging to file is enabled
LOG_LEVEL="INFO"             # Default log level (DEBUG, INFO, WARN, ERROR, CRITICAL)
TEMP_DIR=""                  # Will be set by mktemp if needed

# Script-specific runtime variables
THRESHOLD=${THRESHOLD_DEFAULT}
REMOTE_USER=${REMOTE_USER_DEFAULT}
SERVER_LIST=${SERVER_LIST_DEFAULT}
# Add more variables as needed for arguments and config

# --- Color Definitions (Optional) ---
# Define ANSI escape codes for colored output, checking if NO_COLOR is set or if not interactive.
if [[ "${NO_COLOR}" == false && "${INTERACTIVE_MODE}" == true ]]; then
    COLOR_RESET='\033[0m'
    COLOR_RED='\033[0;31m'
    COLOR_GREEN='\033[0;32m'
    COLOR_YELLOW='\033[0;33m'
    COLOR_BLUE='\033[0;34m'
    COLOR_CYAN='\033[0;36m'
    COLOR_BOLD='\033[1m'
else
    COLOR_RESET=""
    COLOR_RED=""
    COLOR_GREEN=""
    COLOR_YELLOW=""
    COLOR_BLUE=""
    COLOR_CYAN=""
    COLOR_BOLD=""
fi

# =========================================================================================
# FUNCTION DEFINITIONS
# =========================================================================================

# --- Logging Function ---
# Description: Handles formatted logging to stdout/stderr and optionally to a file.
# Usage: log_message LEVEL "Message string"
# Levels: DEBUG, INFO, WARN, ERROR, CRITICAL
log_message() {
    local level="$1"
    local message="$2"
    local timestamp
    timestamp=$(date +"%Y-%m-%d %H:%M:%S %Z") # Include Timezone
    local level_upper
    level_upper=$(echo "$level" | tr '[:lower:]' '[:upper:]')
    local log_prefix="[${timestamp}] [${level_upper}]"
    local log_line="${log_prefix} - ${message}"
    local color=""

    # Determine color based on level
    case "${level_upper}" in
        DEBUG) color="${COLOR_CYAN}" ;;
        INFO) color="${COLOR_GREEN}" ;;
        WARN) color="${COLOR_YELLOW}" ;;
        ERROR) color="${COLOR_RED}" ;;
        CRITICAL) color="${COLOR_BOLD}${COLOR_RED}" ;;
    esac

    # Map script log levels to numeric values for comparison
    declare -A log_levels=([DEBUG]=0 [INFO]=1 [WARN]=2 [ERROR]=3 [CRITICAL]=4)
    local current_log_level_num=${log_levels[${LOG_LEVEL^^}]}
    local message_level_num=${log_levels[${level_upper}]}

    # Check if the message level is severe enough to be logged based on LOG_LEVEL
    if [[ ${message_level_num} -ge ${current_log_level_num} ]]; then
        # Output to stderr for WARN, ERROR, CRITICAL; stdout otherwise
        if [[ "${level_upper}" == "WARN" || "${level_upper}" == "ERROR" || "${level_upper}" == "CRITICAL" ]]; then
            echo -e "${color}${log_line}${COLOR_RESET}" >&2
        else
            # Only print DEBUG if VERBOSE is true
            if [[ "${level_upper}" == "DEBUG" && "${VERBOSE}" == false ]]; then
                : # Do nothing for DEBUG messages if not verbose
            else
                echo -e "${color}${log_line}${COLOR_RESET}"
            fi
        fi

        # Append to log file if enabled
        if [[ "${LOG_TO_FILE}" == true ]]; then
            # Ensure log directory exists (attempt to create if missing)
            mkdir -p "$(dirname "${LOG_FILE}")" 2>/dev/null || true # Avoid error if creation fails here, check later
            if [[ -w "$(dirname "${LOG_FILE}")" ]]; then
                 # Strip color codes for file logging
                 echo "${log_prefix} - ${message}" >> "${LOG_FILE}"
            else
                 # Warning if log directory is not writable, but only warn once
                 if [[ -z ${LOG_DIR_WRITE_WARN_SENT+x} ]]; then # Check if variable is unset
                    echo -e "${COLOR_YELLOW}[${timestamp}] [WARN] - Cannot write to log directory $(dirname "${LOG_FILE}"). Logging to file disabled.${COLOR_RESET}" >&2
                    LOG_DIR_WRITE_WARN_SENT=true # Set variable to prevent repeating warning
                    LOG_TO_FILE=false            # Disable further file logging attempts
                 fi
            fi
        fi
    fi

    # Exit immediately for CRITICAL errors
    if [[ "${level_upper}" == "CRITICAL" ]]; then
        log_message "INFO" "Critical error encountered. Exiting script."
        # Consider calling cleanup function here if not using trap
        # cleanup
        exit 1 # Use a specific exit code for critical errors if desired
    fi
}

# --- Usage/Help Function ---
# Description: Displays help information based on header comments and exits.
# Style Note: Uses a 'here document' (cat << EOF) for easy multi-line text.
usage() {
    # Extract the Usage section from this script's header comments.
    # This uses sed to find the start/end markers and print lines between them.
    # It removes the leading '# ' characters.
    local usage_text
    usage_text=$(sed -n '/^# ===+ USAGE ===+$/,/^# ===+ .* ===+$/{ /# ===+ .* ===+$/!p; }' "${BASH_SOURCE[0]}" | sed 's/^# //; s/\[your_script_name.sh\]/'"${SCRIPT_NAME}"'/g')

    # Print extracted usage information to stderr (common practice for help/errors)
    cat << EOF >&2
${usage_text}

Default Configuration File: ${DEFAULT_CONFIG_FILE}
Default Output Directory: ${DEFAULT_OUTPUT_DIR}
Default Log File: ${DEFAULT_LOG_FILE} (Timestamped on execution)
EOF
    exit 1 # Exit with a non-zero status after showing help
}

# --- Dependency Check Function ---
# Description: Checks if a command-line utility is installed and executable.
#              Exits with error if the dependency is missing.
# Arguments: $1: Command name to check (e.g., "jq", "curl")
#            $2: (Optional) Package name to suggest for installation
check_dependency() {
    local cmd="$1"
    local install_suggestion="${2:-$cmd}" # Use command name if package name not provided

    if ! command -v "$cmd" &> /dev/null; then
        log_message "CRITICAL" "Required command '${cmd}' not found."
        log_message "ERROR" "Please install the '${install_suggestion}' package using your system's package manager (e.g., apt, dnf, brew)."
        # exit 1 is handled by CRITICAL log level
    fi
    log_message "DEBUG" "Dependency check passed for command: ${cmd}"
}

# --- Cleanup Function ---
# Description: Performs cleanup tasks before script exits (e.g., removing temp files).
#              Designed to be called via 'trap'.
# Note: Avoid complex logic or commands that might fail here. Keep it simple.
cleanup() {
    local exit_status=$? # Capture the script's exit status

    log_message "INFO" "Performing cleanup..."

    # Remove temporary directory if it was created
    if [[ -n "${TEMP_DIR:-}" && -d "${TEMP_DIR}" ]]; then
        log_message "DEBUG" "Removing temporary directory: ${TEMP_DIR}"
        rm -rf "${TEMP_DIR}" || log_message "WARN" "Failed to remove temporary directory: ${TEMP_DIR}"
    fi

    # Add other cleanup tasks here:
    # - Kill background processes? (Use pkill -P $$ ?)
    # - Remove lock files?
    # - Logout from services?

    log_message "INFO" "Cleanup finished with exit status: ${exit_status}"
    # Note: The script will exit with the original exit_status after trap completes
}

# --- Trap Setup ---
# Register the 'cleanup' function to run on specific signals and on script exit.
# EXIT: Normal script termination (including successful exit or exit due to 'set -e').
# INT: Interrupt signal (Ctrl+C).
# TERM: Termination signal (sent by `kill` command).
# HUP: Hangup signal.
trap cleanup EXIT INT TERM HUP

# --- Argument Parsing Function ---
# Description: Parses command-line options and arguments using getopts.
#              Updates global variables based on provided flags.
# Note: 'getopts' is a Bash built-in and simpler than external 'getopt',
#       but doesn't support long options (e.g., --verbose) directly without workarounds.
#       This example focuses on short options. Add long option parsing if needed.
parse_params() {
    # ':' at the beginning enables silent error reporting for missing args / invalid opts
    # List all expected option letters. Letters followed by ':' expect an argument.
    while getopts ":hvdt:c:o:u:" opt; do
        case $opt in
            h) usage ;; # Show help and exit
            v) VERBOSE=true ;; # Enable verbose mode
            d) DEBUG_MODE=true; set -x ;; # Enable debug mode (set -x)
            t) # Threshold expects an argument
               THRESHOLD="$OPTARG"
               # Basic validation example: Check if it's an integer
               if ! [[ "$OPTARG" =~ ^[0-9]+$ ]]; then
                   log_message "ERROR" "Invalid threshold value: '$OPTARG'. Must be an integer."
                   usage
               fi
               ;;
            c) CONFIG_FILE="$OPTARG" ;; # Specify config file
            o) OUTPUT_DIR="$OPTARG" ;; # Specify output directory
            u) REMOTE_USER="$OPTARG" ;; # Specify remote user
            \?) # Invalid option
                log_message "ERROR" "Invalid option: -${OPTARG}" >&2
                usage ;;
            :) # Option requires an argument, but none provided
                log_message "ERROR" "Option -${OPTARG} requires an argument." >&2
                usage ;;
        esac
    done

    # Shift processed options away, leaving positional arguments in $@
    shift $((OPTIND-1))

    # --- Handle Positional Arguments ---
    # Example: Assign the first remaining argument to SERVER_LIST
    if [[ $# -ge 1 ]]; then
        SERVER_LIST="$1"
        # Optionally shift it away if you expect more positional args
        # shift
    else
        # If a positional argument is required but missing
        log_message "ERROR" "Missing required argument: Server List File"
        usage
    fi

    # Example: Check for unexpected additional arguments
    # if [[ $# -gt 0 ]]; then
    #     log_message "ERROR" "Unexpected argument(s): $*"
    #     usage
    # fi

    log_message "DEBUG" "Arguments parsed. Verbose: ${VERBOSE}, Config: ${CONFIG_FILE}, Output: ${OUTPUT_DIR}, Threshold: ${THRESHOLD}, Server List: ${SERVER_LIST}"
}

# --- Configuration Loading Function ---
# Description: Loads configuration settings from a specified file.
#              Settings in the file override defaults but are overridden by command-line args.
# Format: Simple key=value pairs (e.g., THRESHOLD=90)
load_config() {
    if [[ -f "${CONFIG_FILE}" && -r "${CONFIG_FILE}" ]]; then
        log_message "INFO" "Loading configuration from: ${CONFIG_FILE}"
        # Read line by line to avoid 'source' security risks
        while IFS='=' read -r key value || [[ -n "$key" ]]; do
            # Trim leading/trailing whitespace from key and value
            key=$(echo "$key" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
            value=$(echo "$value" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

            # Ignore empty lines and comments (#)
            if [[ -z "$key" || "$key" =~ ^# ]]; then
                continue
            fi

            # Remove potential quotes around value
            value="${value#\"}"; value="${value%\"}"
            value="${value#\'}"; value="${value%\'}"

            # Assign value to corresponding global variable if it exists
            # Use case statement for explicit mapping to prevent arbitrary code execution
            case "$key" in
                THRESHOLD)
                    # Only update if not already set by command-line args
                    # Check if THRESHOLD is still its default value
                    if [[ ${THRESHOLD} -eq ${THRESHOLD_DEFAULT} ]]; then
                        THRESHOLD="$value"
                        log_message "DEBUG" "Config loaded: THRESHOLD=${THRESHOLD}"
                    fi
                    ;;
                REMOTE_USER)
                    if [[ "${REMOTE_USER}" == "${REMOTE_USER_DEFAULT}" ]]; then
                        REMOTE_USER="$value"
                        log_message "DEBUG" "Config loaded: REMOTE_USER=${REMOTE_USER}"
                    fi
                    ;;
                OUTPUT_DIR)
                    if [[ "${OUTPUT_DIR}" == "${DEFAULT_OUTPUT_DIR}" ]]; then
                        OUTPUT_DIR="$value"
                        log_message "DEBUG" "Config loaded: OUTPUT_DIR=${OUTPUT_DIR}"
                    fi
                    ;;
                 LOG_FILE)
                    if [[ "${LOG_FILE}" == "${DEFAULT_LOG_FILE}" ]]; then
                        LOG_FILE="$value"
                        log_message "DEBUG" "Config loaded: LOG_FILE=${LOG_FILE}"
                    fi
                    ;;
                 LOG_TO_FILE)
                     # Assume default was true, respect config file setting
                     if [[ "$value" =~ ^(false|no|0)$ ]]; then
                        LOG_TO_FILE=false
                     else
                        LOG_TO_FILE=true
                     fi
                     log_message "DEBUG" "Config loaded: LOG_TO_FILE=${LOG_TO_FILE}"
                     ;;
                LOG_LEVEL)
                    # Validate log level from config
                    if [[ "$value" =~ ^(DEBUG|INFO|WARN|ERROR|CRITICAL)$ ]]; then
                       # Assume default was INFO, respect config file setting
                       LOG_LEVEL="$value"
                       log_message "DEBUG" "Config loaded: LOG_LEVEL=${LOG_LEVEL}"
                    else
                        log_message "WARN" "Invalid LOG_LEVEL in config file: '${value}'. Using default '${LOG_LEVEL}'."
                    fi
                    ;;
                # Add more configuration keys here
                *)
                    log_message "WARN" "Ignoring unknown configuration key in ${CONFIG_FILE}: '${key}'" ;;
            esac
        done < "${CONFIG_FILE}"
    elif [[ "${CONFIG_FILE}" != "${DEFAULT_CONFIG_FILE}" ]]; then
        # Error only if a specific config file was requested but not found/readable
        log_message "ERROR" "Configuration file specified ('${CONFIG_FILE}') not found or not readable."
        exit 3 # Specific exit code for config errors
    else
        log_message "INFO" "Default configuration file ('${DEFAULT_CONFIG_FILE}') not found. Using default settings and command-line arguments."
    fi
}

# --- Input Validation Function ---
# Description: Performs checks on finalized configuration and inputs before execution.
validate_inputs() {
    log_message "INFO" "Validating inputs and configuration..."

    # Validate required arguments (e.g., SERVER_LIST)
    if [[ -z "${SERVER_LIST}" ]]; then
        log_message "CRITICAL" "Server list file argument is required."
        # exit 1 handled by CRITICAL
    elif [[ ! -f "${SERVER_LIST}" || ! -r "${SERVER_LIST}" ]]; then
        log_message "CRITICAL" "Server list file '${SERVER_LIST}' not found or not readable."
        # exit 1 handled by CRITICAL
    fi

    # Validate paths
    if ! mkdir -p "${OUTPUT_DIR}"; then
         log_message "CRITICAL" "Output directory '${OUTPUT_DIR}' could not be created."
    elif [[ ! -w "${OUTPUT_DIR}" ]]; then
        log_message "CRITICAL" "Output directory '${OUTPUT_DIR}' is not writable."
    fi

    # Ensure log directory is writable if logging to file
    if [[ "${LOG_TO_FILE}" == true ]]; then
         if ! mkdir -p "$(dirname "${LOG_FILE}")"; then
             log_message "WARN" "Log directory '$(dirname "${LOG_FILE}")' could not be created. Disabling file logging."
             LOG_TO_FILE=false
         elif [[ ! -w "$(dirname "${LOG_FILE}")" ]]; then
              log_message "WARN" "Log directory '$(dirname "${LOG_FILE}")' is not writable. Disabling file logging."
              LOG_TO_FILE=false
         fi
    fi

    # Validate numerical values
     if ! [[ "${THRESHOLD}" =~ ^[0-9]+$ ]] || [[ ${THRESHOLD} -lt 0 || ${THRESHOLD} -gt 100 ]]; then
        log_message "CRITICAL" "Invalid threshold value: '${THRESHOLD}'. Must be an integer between 0 and 100."
    fi

    log_message "INFO" "Input validation passed."
}

# --- Preparation Function ---
# Description: Sets up the environment before the main logic runs.
#              (e.g., creates temporary directories, checks external services)
prepare_environment() {
    log_message "INFO" "Preparing execution environment..."

    # Create a secure temporary directory if needed by the script
    # TEMP_DIR=$(mktemp -d "${DEFAULT_TMP_DIR_BASE}/${SCRIPT_NAME}.XXXXXX")
    # log_message "DEBUG" "Created temporary directory: ${TEMP_DIR}"
    # Ensure TEMP_DIR is included in the cleanup() function

    # Check connectivity to essential external services?
    # Example: ping -c 1 some.api.server &> /dev/null || log_message "CRITICAL" "Cannot reach API server."

    # Create Output/Log directories (validation already checked writability)
    mkdir -p "${OUTPUT_DIR}"
    if [[ "${LOG_TO_FILE}" == true ]]; then
        mkdir -p "$(dirname "${LOG_FILE}")"
        # Touch the log file to ensure it exists early (optional)
        touch "${LOG_FILE}" || log_message "WARN" "Could not touch log file: ${LOG_FILE}"
    fi

    log_message "INFO" "Environment preparation complete."
}

# --- Main Logic Function ---
# Description: Contains the core functionality of the script.
#              It's called after setup, parsing, and validation.
main() {
    log_message "INFO" "Starting main script execution..."
    log_message "INFO" "Using Threshold: ${THRESHOLD}%, Remote User: ${REMOTE_USER}, Output Dir: ${OUTPUT_DIR}"

    # -----------------------------------------------------
    # TODO: Implement the core functionality of your script here.
    # -----------------------------------------------------
    # Example Steps:
    # 1. Read data from input files (e.g., SERVER_LIST)
    #    while IFS= read -r server || [[ -n "$server" ]]; do
    #        log_message "INFO" "Processing server: $server"
    #        # Check if line is empty or comment
    #        if [[ -z "$server" || "$server" =~ ^# ]]; then continue; fi
    #
    #        # 2. Perform actions (e.g., SSH, run commands, process data)
    #        ssh_command="ssh -l ${REMOTE_USER} ${server} 'df -h /'"
    #        log_message "DEBUG" "Executing: ${ssh_command}"
    #        ssh_output=$(eval "${ssh_command}") # Use eval with caution, consider arrays or functions
    #        ssh_exit_code=$?
    #
    #        if [[ ${ssh_exit_code} -ne 0 ]]; then
    #            log_message "ERROR" "SSH command failed for server ${server} with exit code ${ssh_exit_code}."
    #            # continue to next server or handle error differently
    #            continue
    #        fi
    #
    #        # 3. Parse results and generate output
    #        # ... parsing logic ...
    #        local usage_percent # ... extract value ...
    #        if [[ ${usage_percent} -ge ${THRESHOLD} ]]; then
    #             log_message "WARN" "Server ${server} filesystem usage (${usage_percent}%) exceeds threshold (${THRESHOLD}%)."
    #             echo "${server},ALERT,${usage_percent}" >> "${OUTPUT_DIR}/report.csv"
    #        else
    #             echo "${server},OK,${usage_percent}" >> "${OUTPUT_DIR}/report.csv"
    #        fi
    #
    #    done < "${SERVER_LIST}"


    # --- Placeholder Command Example with Error Checking ---
    log_message "INFO" "Running example command..."
    ls -l "${OUTPUT_DIR}" || { log_message "ERROR" "Failed to list output directory: ${OUTPUT_DIR}"; exit 6; } # Exit code for FS error


    # --- Dry Run Check Example ---
    if [[ "${DRY_RUN}" == true ]]; then
        log_message "INFO" "[DRY RUN] Would have performed critical action X."
    else
        log_message "INFO" "Performing critical action X..."
        # actual_command_for_action_X || { log_message "ERROR" "Critical action X failed."; exit 1; }
    fi


    log_message "INFO" "Main execution logic finished."
}


# =========================================================================================
# SCRIPT EXECUTION FLOW
# =========================================================================================

# 1. Parse Command Line Arguments
parse_params "$@" # Pass all arguments received by the script

# 2. Load Configuration File
load_config # Uses CONFIG_FILE variable set by defaults or parse_params

# 3. Validate Inputs and Configuration
validate_inputs

# 4. Check Dependencies
log_message "INFO" "Checking required dependencies..."
# check_dependency "jq" "jq - JSON processor"
# check_dependency "curl" "curl - Data transfer utility"
# check_dependency "sshpass" "sshpass - Non-interactive SSH password provider (SECURITY RISK)"
# Add checks for all critical external commands used in main()

# 5. Prepare Environment
prepare_environment

# 6. Execute Main Logic
main

# 7. Exit Successfully
#    The 'trap cleanup EXIT' will run automatically.
log_message "INFO" "Script completed successfully."
exit 0 # Explicitly exit with success code

# =========================================================================================
# LICENSE TEXT (Example: MIT License)
# =========================================================================================
# MIT License
#
# Copyright (c) [Year] [Author/Team Name]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =========================================================================================
# --- End of Script ---

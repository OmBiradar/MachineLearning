import sys
import subprocess
def generate_requirements():
    # Get Python version
    python_version = sys.version.split()[0]

    # Get installed packages
    try:
        packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8').split('\n')
    except subprocess.CalledProcessError:
        print("Error: Failed to retrieve installed packages.")
        return

    # Write to requirements.txt
    with open('requirements.txt', 'w') as f:
        f.write(f"# Python version: {python_version}\n")
        for package in packages:
            f.write(package + '\n')

    print("requirements.txt generated successfully.")

if __name__ == "__main__":
    generate_requirements()

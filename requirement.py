import subprocess

def create_requirements_txt():
    # List of packages to include in requirements.txt
    packages = [
        'pandas==1.3.0',
        'numpy==1.21.0',
        'scikit-learn==0.24.2',
        'matplotlib==3.4.2',
        'seaborn==0.11.1'
    ]

    # Write packages to requirements.txt
    with open('requirements.txt', 'w') as f:
        for package in packages:
            subprocess.check_call(['pip', 'install', package])
            f.write(package + '\n')

    print("requirements.txt generated successfully.")

if __name__ == "__main__":
    create_requirements_txt()

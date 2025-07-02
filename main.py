import subprocess


def run_step(description, command):
    print(f"Start: {description}")
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        print(f"{description} 失敗")
        exit(1)

    print(f"End: {description}")


def main():
    config_path = f"configs/v1/config.json"

    steps = [
        ("scripts/fetch_raw_data.py", f"python scripts/fetch_raw_data.py --config {config_path}"),
    ]

    for desc, cmd in steps:
        run_step(desc, cmd)


if __name__ == "__main__":
    main()

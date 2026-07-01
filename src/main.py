#!/usr/bin/env python3

from config import load_config

APP_NAME = "HTO"


def main():
    config = load_config()

    print("=" * 50)
    print(f"{config['general']['app_name']} - Hiddify Torrent Offline")
    print(f"Version: {config['general']['version']}")
    print("Author: whtfoxx")
    print("=" * 50)

    print("\nConfiguration loaded successfully.")
    print(f"Telegram enabled: {config['telegram']['enabled']}")
    print(f"Log level: {config['logging']['level']}")

    print("\nHTO is ready.")


if __name__ == "__main__":
    main()

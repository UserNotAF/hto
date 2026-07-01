#!/usr/bin/env python3

from config import load_config
from logger import setup_logger
import logging


def print_banner(config):

    print()
    print("=" * 55)
    print(f"{config['general']['app_name']} - Hiddify Torrent Offline")
    print(f"Version : {config['general']['version']}")
    print("Author  : whtfoxx")
    print("=" * 55)
    print()


def main():

    setup_logger()

    logging.info("Loading configuration...")

    config = load_config()

    print_banner(config)

    logging.info("Configuration loaded.")

    logging.info("HTO started successfully.")

    print("Status : READY")


if __name__ == "__main__":
    main()

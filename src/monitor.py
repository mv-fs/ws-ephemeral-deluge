"""
############################
# Author: Dhruvin Shah
# Date: 18th Sep 2023
############################

A worker that keep track of qBitTorrent connection
"""

import logging

import config
from lib.qbit import QbitManager

# Lets assume we have proper connection with the qBitTorrent
HEARTBEAT = True


def monitor() -> bool:
    """Monitor qBitTorrent instance is running as expected."""
    global HEARTBEAT
    try:
        QbitManager(
            host=config.TORRENT_CLIENT_HOST,
            port=config.TORRENT_CLIENT_PORT,
            username=config.TORRENT_CLIENT_USERNAME,
            password=config.TORRENT_CLIENT_PASSWORD,
        )
    except Exception:
        logging.error("Something wrong with Qbit, it's not accessible")
        HEARTBEAT = False
    else:
        logging.debug("Hearbeat detected")
        HEARTBEAT = True

    return HEARTBEAT

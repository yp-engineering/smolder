#! /usr/bin/env python
import logging
import socket
import random
from retrying import retry

FORMAT = '%(asctime)-15s %(name)s [%(levelname)s]: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.ERROR, datefmt="%Y-%m-%d %H:%M:%S")
LOG = logging.getLogger('smolder')

OUTPUT_WIDTH = 90
TEST_LINE_FORMAT = "{0:.<" + str(OUTPUT_WIDTH - 10) + "s} {1:4s}"


@retry(wait_exponential_multiplier=500, wait_exponential_max=30000, stop_max_attempt_number=7)
def tcp_test(host, port):
    """Attempts to make a TCP socket connection on the specified host and
    port. Returns true if successful. Else returns false.

    """
    LOG.debug("TCP test called")
    try:
        my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_sock.settimeout(1)
        my_sock.connect((host, port))
        print "Connecting to {0} on port {1}....................[PASS]".format(host, port)
        my_sock.shutdown(2)
        my_sock.close()
    except socket.error:
        my_sock.close()
        LOG.debug("    Waiting for {0}:{1} to accept a connection".format(host, port))
        raise
    except Exception as error:
        LOG.debug("TCP test failed: {0}".format(error.message))
        raise



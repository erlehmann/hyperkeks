"""Setup the hyperkeks application"""
import logging

import pylons.test

from hyperkeks.config.environment import load_environment
from hyperkeks.model.meta import Session, metadata

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup hyperkeks here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    metadata.create_all(bind=Session.bind)

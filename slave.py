#!/usr/bin/python
# coding: utf-8

'''
Source:
https://home-assistant.io/developers/multiple_instances/
'''

import homeassistant.remote as remote
import homeassistant.bootstrap as bootstrap
import os


HASS_HOSTNAME = os.environ.get('HASS_HOSTNAME', 'example.com')
HASS_PORT = os.environ.get('HASS_PORT', 8123)
HASS_PASSWORD = os.environ.get('HASS_PASSWORD', 'password')

# Location of the Master API: host, password, port.
# Password and port are optional.
remote_api = remote.API(HASS_HOSTNAME, HASS_PASSWORD, HASS_PORT)

# Initialize slave
hass = remote.HomeAssistant(remote_api)

# To add an interface to the slave on localhost:8123
bootstrap.setup_component(hass, 'frontend')

hass.start()
hass.block_till_stopped()

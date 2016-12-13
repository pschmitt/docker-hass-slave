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
HASS_PORT = int(os.environ.get('HASS_PORT', 8123))
HASS_PASSWORD = os.environ.get('HASS_PASSWORD', 'password')
HASS_USE_SSL = bool(os.environ.get('HASS_USE_SSL', False))

# Location of the Master API: host, password, port.
# Password and port are optional.
remote_api = remote.API(
    host=HASS_HOSTNAME,
    api_password=HASS_PASSWORD,
    port=HASS_PORT,
    use_ssl=HASS_USE_SSL
)

# Initialize slave
hass = remote.HomeAssistant(remote_api)

# To add an interface to the slave on localhost:8123
bootstrap.setup_component(hass, 'frontend')

hass.start()
hass.block_till_stopped()

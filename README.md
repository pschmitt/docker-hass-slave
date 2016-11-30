# home-assistant slave

Usage:

```
docker run -it --rm -p 8123:8123 \
    -e HASS_HOSTNAME=home.example.com \
    -e HASS_PASSWORD=mySecretAPIpassword \
    -e HASS_PORT=8123
    pschmitt/hass-slave
```

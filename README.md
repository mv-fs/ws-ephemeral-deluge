# WS-EPHEMERAL

This repo is a fork of [ws-ephemeral](dhruvinsh/ws-ephemeral) with the goal of making it usable as a scheduled task for desktop and also change the qBittorrent integration to Deluge.
Another change is that this verison will not delete the existing port but only grab it. This way you can use this script as a scheduled task while having the original reseting the ports independently on your server.

## Docker Setup

> [!important]
> DOCKER is not being supported actively in this repo, all the code is from the original repo and should not be expected to work.

### Environment Variables

| Variable             | Comment                                                                          |
| -------------------- | -------------------------------------------------------------------------------- |
| WS_USERNAME          | WS username                                                                      |
| WS_PASSWORD          | WS password                                                                      |
| WS_TOTP              | WS totp token for 2fa                                                            |
| WS_DEBUG             | Enable Debug logging                                                             |
| WS_COOKIE_PATH       | Persistent location for the cookie. (v3.x.x only)                                |
| TORRENT_CLIENT_USERNAME        | torrent client username                                                                    |
| TORRENT_CLIENT_PASSWORD        | torrent client password                                                                    |
| TORRENT_CLIENT_HOST            | torrent client web address like, <<https://torrent> client.xyz.com> or <http://192.168.1.10>               |
| TORRENT_CLIENT_PORT            | torrent client web port number like, 443 or 8080                                           |
| torrent client_PRIVATE_TRACKER | get torrent client ready for private tracker by disabling dht, pex and lsd (true or false) |
| ONESHOT              | Run and setup the code only one time so that job can be schedule externally      |
| REQUEST_TIMEOUT      | configurable http api timeout for slow network/busy websites                     |

## Privacy

I assure you that nothing is being collected or logged. Your credentials are
safe and set via environment variable only. Still If you have further questions
or concerns, please open an issue here.

## Roadmap

- [ ] Change qBit to Deluge
- [ ] Remove Port deletion step

## License

[GPL3](LICENSE.md)

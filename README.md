# chkdns

![chkdns](https://github.com/chelnak/chkdns/actions/workflows/ci.yaml/badge.svg) [![PyPI version](https://badge.fury.io/py/chkdns.svg)](https://badge.fury.io/py/chkdns)

Harness the power of [whatsmydns](https://whatsmydns.net) from the command-line.

![chkdns](media/cli.png)

## Installation and Configuration

`chkdns` is available on [pypi.org](https://pypi.org)!

```bash
pip install chkdns
```

Once the app is installed you can run it from your terminal with the `chkdns` command.

```bash
chkdns --host github.com
```

Alternatively you can run with docker:

```bash
docker run -rm -it ghcr.io/chelnak/chkdns:latest --host github.com
```

## Contributing

If you would like to contribute to `azure-keyvault-browser` head over to the [contributing guide](CONTRIBUTING.md) to find out more!

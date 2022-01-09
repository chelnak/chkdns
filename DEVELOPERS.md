# Developing

Welcome to the developers guide for `chkdns`!

## Install dependencies

Install dependencies with poetry:

```bash
poetry install
```

## Building

To keep local builds consistent with ci, use make to build and lint:

```bash
make build
```

## Install pre commit hooks

The project uses [pre-commit](https://pre-commit.com/) for commit time checking. You can find the configuration [here](.pre-commit-config.json).

```bash
pre-commit install
```

## Updating the server list

Sometimes the list of servers used by `chkdns` can become stale resulting in an `Invalid server` response for certain requests. When this happens it is usually time to update the server list to match what is being used by [whatsmydns.net](https://www.whatsmydns.net/).

Run `make scrap_servers` to generate a new list then update the `SERVERS` variable in [this file](./src/chkdns/whatsmydns/servers.py#95).

## Releasing stuff

Releasing is a semi manual but well oiled method. Tags are used to trigger the release steps in the ci process.

Running the following make command will tag and push the latest commit triggering a release.

```bash
make tag version="v0.0.5"
```

> Note: Releases can only be generated from the main branch.

## Runing locally

You can either build a new package using `make build` and install it or run the package directly:

```bash
poetry run chkdns
```

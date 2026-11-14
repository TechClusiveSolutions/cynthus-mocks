# cynthus-mocks

## Description

Stand-in services for the Cynthus platform, for development and tests. Five small containers (`analysis`, `auth`,
`chat`, `portal-api` and `portal-web`) take the place of the real services of those names. Each one answers
`GET /` with an empty JSON object and does nothing else yet, so a client has something to connect to before the real
service exists.

## Prerequisites

- Docker with the Compose plugin.
- The Docker network `cynthus_net`, shared with the other Cynthus stacks: `docker network create cynthus_net`.
- Network access to GitHub, for the base image (`ghcr.io/techclusivesolutions/cynthus-base`).

## Installation

```sh
git clone https://github.com/TechClusiveSolutions/cynthus-mocks.git
cd cynthus-mocks
docker network create cynthus_net
# create .env (see Minimal configuration)
docker compose up -d --build
docker compose ps
```

`docker compose ps` shows the five `cynthus-mock-*` containers when they are running.

## Minimal configuration

Create `.env` next to `docker-compose.yml`. It is git-ignored; never commit it.

- `API_PORT`: the port the API mocks listen on inside the container.
- `WEB_PORT`: the port the web mock listens on inside the container.
- `TIME_ZONE`: for example `UTC`.

## Gotchas

- The mocks do not publish a port to the host. Reach them from another container on `cynthus_net`, by container name.
- The mocks are named `cynthus-mock-<service>` so they can sit beside the real services, but run a mock and the real
  service of the same name on the same network only if you mean to.
- A mock returns `{}` for `GET /` only. A client that needs more must wait until the mock grows or use the real
  service.

## More documentation

- [`CHANGELOG.md`](CHANGELOG.md): what changed in each release.
- [Engineering standards](https://github.com/TechClusiveSolutions/cynthus/blob/dev/docs/engineering-standards.md):
  branches, tests, lint and review.

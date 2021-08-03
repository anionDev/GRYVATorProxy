# GRYVATorProxy

## Purpose

GRYVATorProxy is a docker-image for simply running a tor-proxy in a docker-container.

## Usage

### Volumes

Using volumes is not required. There are 2 optional volumes:

- `/etc/tor`
- `/var/lib/tor`

### Environment-variables

There are currently no environment-variables available.

### Example

See `docker-compose.example.yml` for an example how to use it.

## Build

The image can be built using the following command:

``` sh
docker image build --no-cache --pull --force-rm --progress plain --build-arg EnvironmentStage=Development --tag gryvatorproxy:latest .
```

## Test

The built image can be tested using the following command:

``` sh
docker-compose -f docker-compose.example.yml -p gryvatorproxy up
```

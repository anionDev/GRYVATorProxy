# GRYVATorProxy

## Purpose

GRYVATorProxy is a docker-image for simply running a tor-proxy in a docker-container.

## Usage

When you first simply run the image using the `docker-compose.example.yml`-file then the required `torrc`-file will not be found but it generates the file `./Test/etc_tor/tor/torrc.sample` for you.
Renaming this file to `./Test/etc_tor/tor/torrc` will make this image workable. Of course you can also directly provide a `torrc`-file without creating a `torrc.sample`.

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

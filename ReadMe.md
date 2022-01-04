# GRYVATorProxy

## Purpose

Represents a [Tor](https://www.torproject.org/)-Node.

## Version

The Tor-version in the latest image is v0.4.6.9.

## Usage

### Volumes

Using volumes is recommended to persist and preserve data. The available folders for shared volumes are:

- `/Workspace/userhome/etc_tor`
- `/Workspace/userhome/var_lib_tor`
- `/Workspace/var/log/tor`

### Environment-variables

There are currently no environment-variables available.

### Example

See `docker-compose.example.yml` for an example how to use it.

### Build image

The image can be built using the following command:

``` sh
docker image build --force-rm --progress plain --build-arg EnvironmentStage=Development --tag gryvatorproxy:latest .
```

The image can also be built using the following command which uses no cache:

``` sh
docker image build --no-cache --pull --force-rm --progress plain --build-arg EnvironmentStage=Development --tag gryvatorproxy:latest .
```

The environment-stage can have the one of the following values:

- `Development`
- `QualityManagement`
- `Productive`

### Test image

The built image can be tested using the following command:

``` sh
docker-compose -f docker-compose.example.yml -p GRYVATorProxy up --remove-orphans --force-recreate
```

When you first simply run the image using the `docker-compose.example.yml`-file then the required `torrc`-file will not be found but it generates the file `./Test/etc_tor/tor/torrc.sample` for you.
Renaming this file to `./Test/etc_tor/tor/torrc` will make this image workable. Of course you can also directly provide a `torrc`-file without creating a `torrc.sample`.

## Development

### Branching-system

This repository applies the [GitFlowSimplified](https://projects.aniondev.de/CommonUtilities/Templates/ProjectTemplates/-/blob/main/Templates/Conventions/BranchingSystem/GitFlowSimplified.md)-branching-system.

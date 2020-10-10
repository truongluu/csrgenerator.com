# csrgenerator.com

[![Build Status](https://travis-ci.org/DavidWittman/csrgenerator.com.svg?branch=master)](https://travis-ci.org/DavidWittman/csrgenerator.com) [![Docker Hub](https://img.shields.io/docker/automated/wittman/csrgenerator.com.svg)](https://hub.docker.com/r/wittman/csrgenerator.com/)

This is the public repository for https://csrgenerator.com. It's a pretty simple Flask webapp which generates a Certificate Signing Request for creating SSL certificates. Sure, you can do it with OpenSSL via the command-line, but not everyone is as smart as you are.

## Running with Docker

```bash
$ docker run -d -p 8080:80 --name csrgenerator truongluu/csrgenerator.com
```

## Response json data for /generate route

```bash
$ curl 'http://localhost:5555/generate' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Accept: application/json, */*; q=0.01' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Origin: http://localhost:5555' \
  --data-raw 'C=US&ST=Texas&L=San+Antonio&O=Vnb&OU=IT&CN=luuxuantruong.info&keySize=2048' \
  --compressed
```

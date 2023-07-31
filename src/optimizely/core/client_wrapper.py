# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(self) -> None:
        pass

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "fern-optimizely",
            "X-Fern-SDK-Version": "0.0.10",
        }
        return headers


class SyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, httpx_client: httpx.Client):
        super().__init__()
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, httpx_client: httpx.AsyncClient):
        super().__init__()
        self.httpx_client = httpx_client

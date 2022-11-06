import grpc # noqa
from typing import List
from v2client import exceptions
from dataclasses import dataclass
from v2client.v2ray import V2RayBase
from api.v2ray.app.stats.command import command_pb2 as stats_command_pb2, command_pb2_grpc as stats_command_pb2_grpc


@dataclass
class UsageResponse:
    download: int
    upload: int


@dataclass
class QueryResponse:
    name: str
    value: int


@dataclass
class QueryListResponse:
    stats: List[QueryResponse]


@dataclass
class SysStatsResponse:
    num_goroutine: int
    num_gc: int
    alloc: int
    total_alloc: int
    sys: int
    mallocs: int
    frees: int
    live_objects: int
    pause_total_ns: int
    uptime: int


class StatsAPI(V2RayBase):

    def get_user_usage(self, email: str, reset: bool = False) -> UsageResponse:
        """
        Get the usage of a user.
        :param email: The email of the user.
        :param reset: Whether to reset the stats after querying.
        :return: A UsageResponse object.
        """
        stub = stats_command_pb2_grpc.StatsServiceStub(self.channel)
        try:
            download = stub.GetStats(
                stats_command_pb2.GetStatsRequest(name=f"user>>>{email}>>>traffic>>>downlink", reset=reset)
            )
            upload = stub.GetStats(
                stats_command_pb2.GetStatsRequest(name=f"user>>>{email}>>>traffic>>>uplink", reset=reset)
            )
            return UsageResponse(download.stat.value, upload.stat.value)
        except grpc.RpcError as e:
            exceptions.auto_raise(e)

    def query_stats(self, pattern: str, reset: bool = False) -> QueryListResponse:
        """
        Query stats.
        :param pattern: The pattern to query.
        :param reset: Whether to reset the stats after querying.
        :return: A dict of stats.
        """
        stub = stats_command_pb2_grpc.StatsServiceStub(self.channel)
        query = stub.QueryStats(stats_command_pb2.QueryStatsRequest(pattern=pattern, reset=reset))
        return QueryListResponse([QueryResponse(stat.name, stat.value) for stat in query.stat])

    def get_sys_stats(self) -> SysStatsResponse:
        """
        Get system stats.
        :return: A SysStatsResponse object.
        """
        stub = stats_command_pb2_grpc.StatsServiceStub(self.channel)
        request = stub.GetSysStats(stats_command_pb2.SysStatsRequest())
        return SysStatsResponse(
            request.NumGoroutine,
            request.NumGC,
            request.Alloc,
            request.TotalAlloc,
            request.Sys,
            request.Mallocs,
            request.Frees,
            request.LiveObjects,
            request.PauseTotalNs,
            request.Uptime
        )

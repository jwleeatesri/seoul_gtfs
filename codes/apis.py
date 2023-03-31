import requests
import os

import pandas as pd

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


def read_base_data(base_file: Path) -> pd.DataFrame:
    """
    나중엔 셀레니움으로 대체?
    현 파일 장소: https://data.seoul.go.kr/dataList/OA-15262/F/1/datasetView.do
    source/bus_routes.xlsx
    """
    df = pd.read_excel(str(base_file))
    df.columns = ["route_name", "route_id"]
    return df


def get_bus_route_list(base_data: pd.DataFrame) -> pd.DataFrame:
    """
    returns: busRouteAbrv, busRouteNm, routeType, stStationNm, edStationNm,
    getBusRouteList는 이후 함수에서도 자주 호출됨으로 한 번 호출하고 뽕 뽑자.
    """
    keys = [
        "busRouteAbrv",
        "busRouteNm",
        "length",
        "routeType",
        "stStationNm",
        "edStationNm",
        "term",
        "firstBusTm",
        "lastBusTm",
        "corpNm",
    ]

    def bus_route_list_helper(strSrch: str) -> pd.Series:
        """
        apply 메서드용 헬퍼 함수. api 호출함
        """
        res = requests.get(
            url="http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList",
            params={
                "ServiceKey": os.getenv("DATA_KEY"),
                "strSrch": strSrch,
                "resultType": "json",
            },
        )
        if res.status_code != 200:
            raise ConnectionError("API Problem")
        if (res_dict := res.json()["msgBody"]["itemList"]) is None:
            print(f"[ERROR] {strSrch}")  # 나중에 에러 로깅 구현
            return pd.Series(["" for _ in keys])
        else:
            # res_dict = res.json()["msgBody"]["itemList"][0]
            return pd.Series([res_dict.get(key) for key in keys])

    df = base_data.copy()
    df[keys] = df["route_name"].apply(bus_route_list_helper)
    return df


def get_route_path_list(base_data: pd.DataFrame) -> pd.DataFrame:
    """
    getRoutePathList API 호출
    """
    keys = [
        "no",
        "gpsX",
        "gpsY",
    ]

    def route_path_list_helper(route_id: str) -> pd.DataFrame | None:
        """
        get route path list를 진짜 호출하는 함수
        """
        res = requests.get(
            url="http://ws.bus.go.kr/api/rest/busRouteInfo/getRoutePath",
            params={
                "ServiceKey": os.getenv("DATA_KEY"),
                "busRouteId": route_id,
                "resultType": "json",
            },
        )
        if res.status_code != 200:
            raise ConnectionError("API Problem")
        if (res_dict := res.json()["msgBody"]["itemList"]) is None:
            print(f"[ERROR] {route_id}-routePathList")
            return None
        else:
            return pd.DataFrame(res_dict)[keys]


# def get_station_by_route(df: pd.DataFrame) -> pd.DataFrame:
#     """
#     get stations
#     """
#     keys = [

#     ]

if __name__ == "__main__":
    pass

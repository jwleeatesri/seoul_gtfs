import pandas as pd

from pathlib import Path


def build_agency(bus_file: Path):
    """
    take the bus file from seoul topis, and parse it
    link: https://topis.seoul.go.kr/refRoom/openRefRoom_3_1.do
    remove the first row
    """
    bus = pd.read_excel(str(bus_file))
    bus.columns = [
        "agency",
        "route_no",
        "type",
        "start",
        "end",
        "num_buses_total",
        "num_buses_active",
        "num_buses_wait",
        "distance",
        "hour_active",
        "num_runs",
        "min_run",
        "max_run",
        "first_time",
        "end_time",
    ]
    with open("../gtfs/agency.txt", "w", encoding="utf-8") as f:
        f.write("agency_id,agency_name,agency_url,agency_timezone,agency_lang\n")

    with open("../gtfs/agency.txt", "a", encoding="utf-8") as g:
        for idx, agency in enumerate(bus["agency"].unique()):
            g.write(f"agency{idx+1:03},{agency},,KST,KO\n")
    return True

import pandas as pd
import os
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
    with open(str(gtfs_dir / "agency.txt"), "w", encoding="utf-8") as f:
        f.write("agency_id,agency_name,agency_url,agency_timezone,agency_lang\n")

    with open(str(gtfs_dir / "agency.txt"), "a", encoding="utf-8") as g:
        for idx, agency in enumerate(bus["agency"].unique()):
            g.write(f"agency{idx+1:03},{agency},,KST,KO\n")
    return True


def build_stops(stations_file: Path):
    """
    take the bus stops file from
    """
    stops = pd.read_excel(str(stations_file))
    stops.columns = [
        "node_id",
        "ars_id",
        "station_name",
        "x",
        "y",
    ]
    with open(gtfs_dir / "stops.txt", "w", encoding="utf-8") as f:
        f.write(
            "stop_id,stop_code,stop_name,stop_lat,stop_lon,location_type,parent_station\n"
        )

    with open(gtfs_dir / "stops.txt", "a", encoding="utf-8") as g:
        for row in stops.itertuples(index=False):
            g.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n")
    return True


def main():
    agencies_built = build_agency(source_dir / "agency.xlsx")
    if agencies_built:
        print("Agency.txt file built!")
    else:
        print("Something went wrong in building agency.txt")
    stops_built = build_stops(source_dir / "stops.xlsx")
    if stops_built:
        print("Stops.txt file built!")
    else:
        print("Stops.txt build failed")


if __name__ == "__main__":
    # used paths
    code_dir = Path(__file__).parent
    source_dir = code_dir.parent / "source"
    gtfs_dir = code_dir.parent / "gtfs"

    main()

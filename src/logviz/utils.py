import argparse
import os

from typing import Any
from termcolor import cprint

from logviz.config import (
    SUPPORTED
)

def parse_args(args: list[str]) -> dict[str, Any]:
    """
    Parses arguements passed in when the program is run
    """

    parser = argparse.ArgumentParser(
        prog="logviz",
        description="A utility that processes reports from plain text formats such as csv and returns summary visualizations of the file",
    )
    _ = parser.add_argument(
        "-f",
        "--files", 
        required=True,
        nargs="*",
        type=str,
        help="path of the data file to visualize"
        )
    _ = parser.add_argument(
        "-t",
        "--timeline",
        nargs=3,
        type=str,
        help="Generates a timeline from the file based on a count of unique values of the specified column. Syntax: -t {required: time column} {required: time bucket size (minutes)} {required: column to plot over time}"
    )
    _ = parser.add_argument(
        "-b",
        "--bar",
        nargs=2,
        type=str,
        help="Generates a histogram from the data based on specified values 'entity column' and 'data column'. Syntax: -b (--bar) {x-axis column data} {y-axis column data}"
        )
    _ = parser.add_argument(
        "-o",
        "--output_directory", 
        required=False,
        default="./plots",
        type=str,
        help="path of the directory to save the plots in. Default: ./plots"
        )
    return get_context(args=parser.parse_args())


def get_context(args: argparse.Namespace): 
    """
    Converts parser.parse_args Namespace to a dictionary for processing later
    """

    timeline= dict()
    files = list()
    bar = dict()
    for item in args.files:
        if os.path.isdir(item):
            for file in os.listdir(item):
                files.append(f"{item}/{file}")
        else:
            files.append(item)
    if args.timeline:
        timeline: dict[str, str]= {
            "time_col": args.timeline[0],
            "interval": args.timeline[1],
            "data_col": args.timeline[2],
        }
    if args.bar:
        bar = {
            "x": args.bar[0],
            "y": args.bar[1]
        }
    return {
        "files": files,
        "timeline": timeline,
        "bar": bar,
        "output_directory": args.output_directory
    }

def check_validity(file: str) -> bool:
    object_type: str = file.split(sep=".")[-1]
    if os.path.isdir(file):
        cprint(f"[!] Object is a directory. Skipping...", color="yellow")
        return False
    if  object_type not in SUPPORTED:
        cprint(f"[!] Object type: {object_type} is not supported. Skipping...", color="yellow")
        return False
    return True

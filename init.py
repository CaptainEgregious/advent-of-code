# Advent of code manager
# Robin Taylor - 2023/11/21

import datetime
import os
import pathlib
import sys
import logging
import requests
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Globals and Constants
AUTHOR = "Robin Taylor"
MAX_RECONNECT_ATTEMPT = 2
BASE_URL = "https://adventofcode.com"
USER_SESSION_ID = (
    ""  # Chrome session cookie, cba to think of a better way to do this atm, but should
)
USER_AGENT = "adventofcode_working_directories_creator"


class AdventManager:
    def __init__(self) -> None:
        self.year: int
        self.month: int
        self.day: int
        self._get_dates()
        pass

    def _get_dates(self) -> None:
        today = datetime.date.today()
        self.year = today.year
        self.month = today.month
        self.day = today.day
        return

    def _setup_code_templates(self, year: int, day: int) -> None:
        code = pathlib.Path(str(year), str(day), "code.py")
        code.parent.mkdir(parents=True, exist_ok=True)
        with code.open("w", encoding="utf-8") as c:
            c.write(
                f'# Advent of Code | Year {year} | Day {str(day)} \n # Author {AUTHOR}\n\nwith open((__file__.rstrip("code.py")+"input.txt"), \'r\') as input_file:\n    input = input_file.read()\n\n\n\nprint("Part One : "+ str(None))\n\n\n\nprint("Part Two : "+ str(None))'
            )
        pathlib.Path(str(year), str(day), "test.py").touch()
        return

    def _collect_challenges(self, year: int, day: int) -> None:
        error_count = 0
        done = False
        while not done:
            try:
                logger.info(f"looking for {BASE_URL}/{year}/day/{day}/input")
                with requests.get(
                    f"{BASE_URL}/{year}/day/{day}/input",
                    cookies={"session": USER_SESSION_ID},
                    headers={"User-Agent": USER_AGENT},
                ) as response:
                    if response.ok:
                        data = response.text
                        input = pathlib.Path(str(year), str(day), "input.txt")
                        input.parent.mkdir(parents=True, exist_ok=True)
                        with input.open("w", encoding="utf-8") as f:
                            f.write(data.rstrip("\n"))
                    else:
                        logger.error(f"Server Respeonse for {year} {day} not valid")
                        logger.error(response)
                        logger.error(response.text)
                done = True
            except requests.exceptions.RequestException:
                error_count += 1
                if error_count > MAX_RECONNECT_ATTEMPT:
                    logger.error("Too many retries, exiting")
                    done = True
                elif error_count == 0:
                    logger.info("Probable Timeout, retrying")
            except Exception as e:
                logger.error(f"Unhandled Exception -  {str(e)}")
                done = True
        return

    def _collecting_existing_file(self, day, year) -> bool:
        if year < self.year:
            return True
        if self.month < 12:
            return False
        if day <= self.day:
            return True
        return False

    def _create_directories_and_files(self, year: int = 2023) -> None:
        logger.info(f"Setting up directories for year {self.year}")
        for i in range(1, 26):
            self._setup_code_templates(year=year, day=i)
            if self._collecting_existing_file(year=year, day=i):
                self._collect_challenges(year=year, day=i)
        return

    def run(self, args) -> None:
        logger.info(f"got today as {args.today}")
        if args.today:
            logger.info("Getting todays challenge")
            self.get_today()
        elif args.year is not None:
            logger.info(f"getting all challenges that exist for {args.year}")
            if args.year is not type(int):
                logger.error("Please provide a year in an integer format")
            self.setup_year(year=args.year)
        else:
            logger.info("No Options provided, collecting this year")
            self.setup_year()
        return

    def setup_year(self, year: int = 2022) -> None:
        self._create_directories_and_files(year=year)
        # Implement Getting problem statements if I can be bothered
        return

    def get_today(self) -> None:
        today = pathlib.Path(str(self.year), str(self.day))
        self._collect_challenges(year=int(self.year), day=self.day)
        return


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int, help="Desired year")
    parser.add_argument("-d", "--day", type=int, help="Desired day")
    parser.add_argument(
        "-t", "--today", action="store_true", help="Collect todays challenge"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    AM = AdventManager()
    AM.run(args)

import typing
import os
import re

import github


ORG_NAME = "unlimited-industries"


def increase_progress_bar(description: str):
    first_part_description, _, percentage = description.rsplit(maxsplit=2)
    percentage = min(round(float(percentage[:-1]) + 0.1, 1), 100)
    number_of_ready_divisons = int(percentage / 10)
    progress_bar = "▐"
    progress_bar += "█" * (number_of_ready_divisons)
    progress_bar += "▒" * (10 - number_of_ready_divisons)

    return f"{first_part_description} {progress_bar} {percentage:.1f}%"


def main() -> typing.NoReturn:
    token = os.getenv("GITHUB_TOKEN")
    organization = github.Github(token).get_organization(ORG_NAME)

    current_description = organization.description
    new_description = increase_progress_bar(current_description)
    print(new_description)
    organization.edit(description=new_description)


if __name__ == "__main__":
    main()

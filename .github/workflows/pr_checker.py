import yaml
from glob import glob
import os
import itertools
import argparse
from typing import Dict, Set
from functools import cache
from termcolor import colored, cprint

here = os.path.dirname(__file__)
root = os.path.abspath(f'{here}/../../')

parser = argparse.ArgumentParser(
    prog='pyhc website checker program',
    description='Check that all yaml files are valid',
    epilog='Enjoy the program! :)')

parser.add_argument('-d', '--dry-run', action='store_true', help='Dry run')


def ensure_all_yaml_files_are_valid(dry_run: bool = False):
    for yaml_file in glob(f"{root}/**/*.yml", recursive=True):
        try:
            with open(yaml_file, "r") as f:
                yaml.safe_load(f)
        except Exception as e:
            if dry_run:
                print(f"Invalid yaml file: {yaml_file}")
            else:
                raise e


@cache
def load_taxonomy():
    with open(f"{root}/_data/taxonomy.yml", "r") as f:
        t = yaml.safe_load(f)
        return set(itertools.chain.from_iterable(map(lambda x: x["keywords"], t)))


def check_project_keywords_respect_taxonomy(project: Dict, dry_run: bool = False) -> bool:
    allowed_keywords: set = load_taxonomy()
    if "keywords" in project:
        project_keywords = set(project["keywords"])
        unlisted_keywords = project_keywords.difference(allowed_keywords)
        if len(project_keywords) == 0:
            print(colored(f"Warning project {project['name']} has no keywords"), "yellow")
        if len(unlisted_keywords) > 0:
            print(f"Unlisted keywords for project {project['name']}: {unlisted_keywords}")
            return False
    else:
        print(f"Project {project['name']} has no keywords")
        return False
    return True


@cache
def functionally_related_keywords() -> Set[str]:
    with open(f"{root}/_data/taxonomy.yml", "r") as f:
        t = yaml.safe_load(f)
        return set(next(filter(lambda x: x["category"] == "Functionality", t))["keywords"])


def check_project_has_mandatory_fields(project: Dict, dry_run: bool = False) -> bool:
    mandatory_fields = {
        "name", "description", "code", "contact", "keywords", "community", "documentation", "testing",
        "software_maturity",
        "python3", "license"}

    if len(mandatory_fields.difference(set(project.keys()))) > 0:
        print(
            f"Project {project['name']} misses mandatory fields: {mandatory_fields.difference(set(project.keys()))}")
        return False
    return True


def check_project_has_grades(project: Dict, dry_run: bool = False) -> bool:
    grades = (["https://img.shields.io/badge/Requires%20improvement-red.svg", "Requires improvement"],
              ["https://img.shields.io/badge/Partially%20met-orange.svg", "Partially met"],
              ["https://img.shields.io/badge/Good-brightgreen.svg", "Good"])
    fields_with_grades = {"community", "documentation", "testing", "software_maturity", "python3", "license"}
    for field in fields_with_grades:
        if field in project and project[field] not in grades:
            print(f"Project {project['name']} deos not respect grades for field {field}, got {project[field]}")
            return False
    return True


def main():
    dry_run = parser.parse_args().dry_run
    ensure_all_yaml_files_are_valid(dry_run=dry_run)
    any_failed = False
    for projects_file in (f"{root}/_data/projects.yml", f"{root}/_data/projects_core.yml"):
        with open(projects_file, "r") as f:
            projects = yaml.safe_load(f)
            for project in projects:
                print("-" * 80)
                print(f"Checking project {project['name']} in file {projects_file}")
                passes = all((
                    check_project_has_mandatory_fields(project),
                    check_project_keywords_respect_taxonomy(project),
                    check_project_has_grades(project)
                ))
                if not passes:
                    print(colored(f"Project {project['name']} failed checks", "red"))
                else:
                    print(colored(f"Project {project['name']} passed checks", "green"))
                any_failed = any_failed or not passes
    if any_failed:
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()

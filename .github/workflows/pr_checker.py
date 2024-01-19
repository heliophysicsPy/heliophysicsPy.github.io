import yaml
from glob import glob
import os
import itertools
import argparse

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


def load_taxonomy():
    with open(f"{root}/_data/taxonomy.yml", "r") as f:
        t = yaml.safe_load(f)
        return set(itertools.chain.from_iterable(map(lambda x: x["keywords"], t)))


def check_keywords_respect_taxonomy(projects_file: str, dry_run: bool = False):
    allowed_keywords: set = load_taxonomy()
    with open(projects_file, "r") as f:
        projects = yaml.safe_load(f)
        for project in projects:
            if "keywords" in project:
                project_keywords = set(project["keywords"])
                unlisted_keywords = project_keywords.difference(allowed_keywords)
                if len(unlisted_keywords) > 0:
                    if dry_run:
                        print(f"Unlisted keywords for project {project['name']}: {unlisted_keywords}")
                    else:
                        raise Exception(f"Unlisted keywords for project {project['name']}: {unlisted_keywords}")
            else:
                print(f"Project {project['name']} has no keywords")


if __name__ == "__main__":
    dry_run = parser.parse_args().dry_run
    ensure_all_yaml_files_are_valid(dry_run=dry_run)
    check_keywords_respect_taxonomy(f"{root}/_data/projects_core.yml", dry_run=dry_run)
    check_keywords_respect_taxonomy(f"{root}/_data/projects.yml", dry_run=dry_run)
    check_keywords_respect_taxonomy(f"{root}/_data/projects_unevaluated.yml", dry_run=dry_run)

#!/bin/python3
import os
import argparse
import subprocess as subp

from utils import term_colors

DOCKERHUB_REPO_BASE = "arterys/inference-sdk-base"
CUDA_VERSIONS = ["9.2", "10.0", "10.1", "10.2"]

def strip_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def build_images():
    # Build CPU image
    release_tag = os.getenv('GITHUB_REF', '')
    if release_tag == '':
        raise RuntimeError('Tag not specified')
    release_tag = strip_prefix(release_tag, 'refs/tags/v')

    cmd = f'docker build -f Dockerfile.cpu -t {DOCKERHUB_REPO_BASE}:{release_tag}-cpu .'
    print(term_colors.OKBLUE + "Running: ", cmd, term_colors.ENDC)
    result = run_cmd(cmd, 'base')
    check_output(result)

    # Build GPU images
    for version in CUDA_VERSIONS:
        cmd = f'docker build -f Dockerfile.gpu --build-arg CUDA_VERSION={version} -t {DOCKERHUB_REPO_BASE}:{release_tag}-cuda-{version} .'
        print(term_colors.OKBLUE + "Running: ", cmd, term_colors.ENDC)
        result = run_cmd(cmd, 'base')
        check_output(result)

def run_cmd(cmd, cwd=None):
    return subp.run(cmd.split(), cwd=cwd, stdout=subp.PIPE, stderr=subp.PIPE, encoding='utf-8')

def check_output(result, fail=True):
    if result.returncode != 0:
        print("OUTPUT")
        print(result.stdout)
        print("ERRORS")
        print(result.stderr)
        if fail:
            raise RuntimeError("Execution failed")


if __name__ == '__main__':
    build_images()

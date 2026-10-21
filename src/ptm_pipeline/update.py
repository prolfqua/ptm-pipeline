"""Refresh a project's copies of the pipeline files from the installed tool."""

from pathlib import Path

from rich.console import Console

from .init import copy_template_files

console = Console()


def refresh_project(directory: Path) -> None:
    """Replace the project's copies of the pipeline files; ptm_config.yaml is kept."""
    copied = copy_template_files(directory)
    console.print(f"[bold]Refreshed in {directory}:[/bold] {', '.join(copied)}")

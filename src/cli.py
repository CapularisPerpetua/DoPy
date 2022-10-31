"""
Main app entry point.
CLI Implementation for DoPy.
Uses typer.
And rich.
"""
import typer
# import rich
import parser
from priority import Priority
from typing import Optional

app = typer.Typer()


@app.command()
def new(description: str = 
        typer.Argument("New to-do.",
                       metavar="\"Description of task.\"",
                       help="Quote-bounded string description."),
        priority: str =
        typer.Option('N/A', help="Priority of new task; must be a valid priority from config.")):
    parsed_desc = parser.parse_description(description)
    print(parsed_desc)
    parsed_text = parser.parse_from_txt(description)
    print(parsed_text)
    print(parser.to_txt(parsed_text))


@app.command()
def delete(target):
    """Delete a target task.

    Args:
        target (_type_): _description_

    Returns:
        _type_: _description_
    """
    return None


if __name__ == '__main__':
    app()

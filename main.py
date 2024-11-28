import typer

from ai_client import AIClient
from diff import get_git_diff
from prompt import get_prompt
from utils import print_response

app = typer.Typer()

@app.command()
def generate_message(
    api: str = typer.Option("gpt", "--api", "-a", help="Choose AI API: 'gpt' or 'claude'"),
    language: str = typer.Option("en", "--lang", "-l", help="Enter language preference"),
    max_tokens: int = typer.Option(500, "--max-tokens", "-mt", help="Maximum number of tokens in the response. Lower values reduce API costs. Recommended range: 100-1000."),
                     ):
    """
    Generate a commit message based on git diff.
    """
    typer.echo("Fetching git diff...")
    diff = get_git_diff()
    
    if not diff:
        typer.echo("No changes detected. Please make sure you have staged changes.")
        raise typer.Exit()

    prompt = get_prompt(language=language)

    typer.echo(f"Using {api} API to generate commit message...")
    client = AIClient(api_type=api, max_tokens=max_tokens)
    response = client.generate_commit_message(diff, prompt)

    print_response(response)


if __name__ == "__main__":
    app()
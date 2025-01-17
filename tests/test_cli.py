from click.testing import CliRunner
from dsacli.cli import cli

class TestCli:
    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--name", "Alice"])
        assert result.exit_code == 0
        assert result.output == "Hello, Alice!\n"
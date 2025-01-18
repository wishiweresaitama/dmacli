from click.testing import CliRunner
from dmacli.cli import cli

class TestHelp:
    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])
        assert result.exit_code == 0
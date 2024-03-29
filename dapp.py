import logging
import subprocess

from cartesi import DApp, Rollup, RollupData

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
dapp = DApp()

def tell_fortune() -> str:
    output = subprocess.run("/usr/games/fortune", capture_output=True)
    return output.stdout.decode("utf-8")

@dapp.advance()
def handle_advance(rollup: Rollup, data: RollupData) -> bool:
    fortune = tell_fortune()
    rollup.notice("0x" + fortune.encode('utf-8').hex())
    return True


@dapp.inspect()
def handle_inspect(rollup: Rollup, data: RollupData) -> bool:
    fortune = tell_fortune()
    rollup.report("0x" + fortune.encode('utf-8').hex())
    return True

if __name__ == '__main__':
    dapp.run()
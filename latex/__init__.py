import pathlib as pl

ROOT_PATH = pl.Path(__file__).parent


def makefilepath(module, file):
    return pl.Path(module.__file__).parent.joinpath('generated').joinpath(file)

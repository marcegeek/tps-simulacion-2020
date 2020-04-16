import pathlib as pl

ROOT_PATH = pl.Path(__file__).parent


def _makedirs(module_dir):
    # asegurar existencia de directorios, module_dir ya existe
    gen_dir = module_dir.joinpath('generated')
    gen_dir.mkdir(exist_ok=True)
    return gen_dir


def makefilepath(module, file):
    module_dir = pl.Path(module.__file__).parent
    return _makedirs(module_dir).joinpath(file)

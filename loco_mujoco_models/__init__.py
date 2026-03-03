from importlib.resources import files


def get_model_path(*relative_parts: str) -> str:
    """
    Return an absolute path to a model file inside this package.
    Example: get_model_path("atlas", "atlas.xml")
    """
    return str(files(__name__).joinpath(*relative_parts))


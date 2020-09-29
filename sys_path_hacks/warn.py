import warnings

def warn_deprecated_import(import_prefix, unprefixed_import_path):
    desired_import_path = import_prefix + "." + unprefixed_import_path
    warnings.warn(
        "Importing {unprefixed_import_path} instead of {desired_import_path} is deprecated".format(
            unprefixed_import_path=unprefixed_import_path,
            desired_import_path=desired_import_path,
        ),
        stacklevel=3,
    )

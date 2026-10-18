
from src.scan_repo import take_files

def test_find_only_allowed_extensions(tmp_path):
    # preparar los archivos para pruebas
    (tmp_path / "index.php").write_text("<?php")
    (tmp_path / "index.php.bk").write_text("<?php")
    (tmp_path / "README.md").write_text("# Prueba")
    (tmp_path / "image.png").write_text("imagen")

    # ejecutar la función
    files = take_files(
        tmp_path,
        [".php", ".py", ".js", ".md"],
        [],
        []
    )

    found_names = {path.name for path in files}

    assert found_names == {"index.php", "README.md"}


def test_excluded_directories(tmp_path):
    # prepara los archivos para pruebas
    (tmp_path / "index.php").write_text("<?php")
    (tmp_path / "vendor").mkdir()
    (tmp_path / "vendor" / "dependency.php").write_text("<?php die; ?>")

    # ejecutar la función
    files = take_files(
        tmp_path,
        [".php", ".py", ".js", ".md"],
        [],
        ["vendor"]
    )

    found_names = {path.name for path in files}

    assert found_names == {"index.php"}


def test_excluded_files(tmp_path):
    # prepara los archivos para pruebas
    (tmp_path / "index.php").write_text("<?php")
    (tmp_path / ".gitignore").write_text("test")

    # ejecutar la función
    files = take_files(
        tmp_path,
        [".php", ".py", ".js", ".md"],
        [".gitignore"],
        []
    )

    found_names = {path.name for path in files}

    assert found_names == {"index.php"}


def test_uppercase_extensions(tmp_path):
    # prepara los archivos para pruebas
    (tmp_path / "SCRIPT.PHP").write_text("<?php")

    # ejecutar la función
    files = take_files(
        tmp_path,
        [".php", ".py", ".js", ".md"],
        [],
        []
    )

    found_names = {path.name for path in files}

    assert found_names == {"SCRIPT.PHP"}


def test_no_allowed_files(tmp_path):
    # prepara los archivos para pruebas
    (tmp_path / "document.pdf").write_text("pdf")
    (tmp_path / "image.png").write_text("imagen")

    # ejecutar la función
    files = take_files(
        tmp_path,
        [".php", ".py", ".js", ".md"],
        [],
        []
    )

    found_names = {path.name for path in files}

    assert not found_names



#!/bin/bash

# asegurar existencia de directorio cache de figuras
mkdir -p tikzcache

# permitir cargar clases, paquetes, etc. desde el directorio raiz de archivos LaTeX del proyecto
export TEXINPUTS=.//:../..//:

# compilar con LuaLaTeX porque PDFLaTeX tiene limitaciones de memoria
if ! lualatex -shell-escape main.tex; then
    exit $?
fi
if ! bibtex main.aux; then
    exit $?
fi
if ! lualatex -shell-escape main.tex; then
    exit $?
fi
if ! lualatex -shell-escape main.tex; then
    exit $?
fi

# obtener variable OUTPUT_FILE para renombrar y mover el PDF compilado
source output-info.sh
mkdir -p build
mv main.pdf "build/$OUTPUT_FILE"

#!/bin/bash
# Este script verifica que Python este instalado.

echo "Verificando la version de Python..."
python --version || { echo "Por favor instala Python 3.6 o superior."; exit 1; }

echo "No se requieren dependencias adicionales para este proyecto."
echo "¡Todo está listo para ejecutar el programa!"
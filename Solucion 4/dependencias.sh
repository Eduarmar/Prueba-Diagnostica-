#!/bin/bash
# Script para verificar Python y preparar el entorno

echo "Verificando instalación de Python..."
python --version || { echo "Por favor instala Python 3.6 o superior."; exit 1; }

echo "No se requieren dependencias adicionales para este proyecto."
echo "¡Todo listo para ejecutar el programa!"
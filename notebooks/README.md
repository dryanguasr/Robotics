# Cuadernos de control cinemático

Los cuadernos de este directorio documentan paso a paso la obtención de la cinemática directa, la matriz Jacobiana y un control cinemático por lazo cerrado para manipuladores planares sencillos.

## Estructura

- `control/control_pr.ipynb`: Robot con primera junta prismática y segunda rotacional.
- `control/control_rp.ipynb`: Robot con primera junta rotacional y segunda prismática.
- `control/control_rr.ipynb`: Robot con dos juntas rotacionales.
- `control/utils.py`: Rutinas compartidas para generar trayectorias de referencia, vectores de tiempo y gráficas de seguimiento.

Cada cuaderno sigue la misma estructura: configuración, modelo cinemático, control, simulación y animación. Esto permite reutilizar funciones y comparar comportamientos entre arquitecturas.

## Uso del módulo `utils` en Google Colab

Para ejecutar los cuadernos en Colab manteniendo las utilidades compartidas:

1. Clona este repositorio (o descarga el ZIP) dentro de tu sesión de Colab. Un ejemplo mínimo usando `git` es:
   ```python
   !git clone https://github.com/dryanguasr/Robotics.git
   %cd Robotics
   ```
   Si solo subes los cuadernos de manera individual, asegúrate de subir también el archivo `notebooks/control/utils.py` o arrastra la carpeta completa `notebooks/control/` al panel de archivos de Colab.
2. Añade la carpeta del proyecto al `sys.path` de Python para que Colab encuentre el módulo:
   ```python
   import sys
   from pathlib import Path

   project_root = Path.cwd()
   if str(project_root) not in sys.path:
       sys.path.append(str(project_root))
   ```
3. Importa las utilidades en el cuaderno de Colab:
   ```python
   from notebooks.control.utils import time_vector, circular_trajectory, plot_tracking
   ```
4. Ejecuta el cuaderno normalmente. Los bloques de verificación (`assert`) incluidos en cada notebook confirmarán que la simulación produce errores máximos aceptables antes de graficar.

Con estos pasos Colab localizará `utils.py` sin necesidad de modificar rutas dentro de los cuadernos.

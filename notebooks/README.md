# Cuadernos de control cinemático

Los cuadernos de este directorio documentan paso a paso la obtención de la cinemática directa, la matriz Jacobiana y un control cinemático por lazo cerrado para manipuladores planares y espaciales sencillos.

## Estructura

- `control/control_pr.ipynb`: Robot con primera junta prismática y segunda rotacional.
- `control/control_rp.ipynb`: Robot con primera junta rotacional y segunda prismática.
- `control/control_rr.ipynb`: Robot con dos juntas rotacionales en el plano.
- `control/control_rrr.ipynb`: Robot planar de tres juntas rotacionales con seguimiento de pose (x, y, θ).
- `control/control_4dof.ipynb`: Manipulador espacial de cuatro grados de libertad con control de (x, y, z, pitch).
- `control/utils.py`: Rutinas compartidas para generar trayectorias de referencia, vectores de tiempo y gráficas de seguimiento.

Cada cuaderno sigue la misma estructura: configuración, modelo cinemático, control, simulación, validación de errores máximos y animación de la trayectoria circular asociada.

> **Nota:** Los cuadernos originales usados como punto de partida (`Control Cinemático PR.ipynb`, `Control Cinemático RP.ipynb` y `Frames Tests.ipynb`) se conservaron en la raíz del repositorio para referencia histórica.

## Uso del módulo `utils` en Google Colab

Para ejecutar los cuadernos en Colab manteniendo las utilidades compartidas:

1. Clona este repositorio (o descarga el ZIP) dentro de tu sesión de Colab. Un ejemplo mínimo usando `git` es:
   ```python
   !git clone https://github.com/dryanguasr/Robotics.git
   %cd Robotics
   ```
   Si solo subes los cuadernos de manera individual, asegúrate de subir también el archivo `notebooks/control/utils.py` o arrastra la carpeta completa `notebooks/control/` al panel de archivos de Colab.
2. Añade la carpeta del proyecto (o específicamente `notebooks/control/`) al `sys.path` de Python para que Colab encuentre el módulo:
   ```python
   import sys
   from pathlib import Path

   control_path = Path.cwd() / 'notebooks' / 'control'
   if str(control_path) not in sys.path:
       sys.path.append(str(control_path))
   ```
3. Importa las utilidades en el cuaderno de Colab:
   ```python
   from utils import time_vector, circular_task_reference, plot_tracking
   ```
4. Ejecuta el cuaderno normalmente. Los bloques de verificación (`assert`) incluidos en cada notebook confirman que la simulación produce errores máximos aceptables antes de graficar.

Con estos pasos Colab localizará `utils.py` sin necesidad de modificar rutas dentro de los cuadernos.

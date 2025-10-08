# Cuadernos de control cinemático

Los cuadernos de este directorio documentan paso a paso la obtención de la cinemática directa, la matriz Jacobiana y un control cinemático por lazo cerrado para manipuladores planares sencillos.

- `control/control_pr.ipynb`: Robot con primera junta prismática y segunda rotacional.
- `control/control_rp.ipynb`: Robot con primera junta rotacional y segunda prismática.
- `control/control_rr.ipynb`: Robot con dos juntas rotacionales.

Cada cuaderno sigue la misma estructura: configuración, modelo cinemático, control, simulación y animación. Esto permite reutilizar funciones y comparar comportamientos entre arquitecturas.

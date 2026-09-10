# Addendum IX · CZUR ET24 Pro Linux · `define.py`, hora de red y ruta real de licencia

**Fecha:** 2026-09-09  
**Estado:** auditoría estática incremental / síntesis abierta  
**Ámbito:** paquete oficial CZUR Scanner Linux 1.0.20250413

[ES · Castellano](#es) · [EN · English](#en)

## ES

### Hallazgo 1 · `define.py` sí contiene una función de red

El módulo interno `define.py`, importado por `user_support.py`, importa `requests` y define `CommonMethods.get_network_time()`.

La función ejecuta explícitamente:

```text
requests.get("http://worldtimeapi.org/api/timezone/Asia/Shanghai.txt", timeout=5)
```

Después busca en la respuesta una marca `datetime:` y reintenta hasta 10 veces, con espera de 1 segundo tras excepción.

Esto demuestra **capacidad de salida HTTP concreta** dentro de `czur_create` y un destino explícito relacionado con sincronización horaria de Asia/Shanghai.

### Hallazgo 2 · la ruta de licencia observada no llama a `get_network_time()`

Se recorrieron las referencias a `CommonMethods` dentro del bytecode desensamblado de `user_support.py`.

Las llamadas observadas son:

- `CommonMethods.is_in_enum(...)`;
- `CommonMethods.get_first_ethernet_mac()`.

No aparece una llamada a `CommonMethods.get_network_time()` en `user_support.py`.

Por tanto:

```text
NETWORK_FUNCTION_PRESENT = CONFIRMADO
NETWORK_FUNCTION_CALLED_FROM_USER_SUPPORT = NO OBSERVADO
```

La presencia de la función no demuestra que se ejecute durante licenciamiento.

### Hallazgo 3 · el socket UDP observado se usa para `ioctl`, no para transmitir

`CommonMethods.get_first_ethernet_mac()` crea un socket:

```text
socket.socket(AF_INET, SOCK_DGRAM)
```

pero el descriptor se utiliza inmediatamente con `fcntl.ioctl(..., 35111, ...)` para obtener la dirección MAC de una interfaz de red.

En el cuerpo auditado no aparecen `connect`, `send` o `recv` asociados a ese socket. Su función observada es local: obtener información de interfaz mediante `ioctl`.

`user_support.get_udev_uuid()` sí llama a `get_first_ethernet_mac()` junto a comandos locales `df`/`udevadm` para construir identificadores de máquina/licencia.

### Interpretación

Hasta esta profundidad de la ruta Python de licencia:

```text
DATOS DE LICENCIA / MACHINE ID       = CONFIRMADO
MAC / UUID / SERIAL LOCAL            = CONFIRMADO
FUNCIÓN HTTP DE HORA EN define.py    = CONFIRMADO
LLAMADA A ESA FUNCIÓN DESDE LICENCIA = NO OBSERVADA
SOCKET PARA MAC VÍA IOCTL            = CONFIRMADO LOCAL
ENVÍO DE DATOS DE LICENCIA A RED     = NO DEMOSTRADO
```

Esto reduce la hipótesis de que el propio flujo `main.py -> user_support.py -> data_support.py` envíe directamente datos de licencia, aunque todavía no excluye otras rutas del ejecutable o de la aplicación principal.

`CAPABILITY != INVOCATION != TRAFFIC != IMPROPER TRANSMISSION`.

## EN

### Finding 1 · `define.py` does contain a network function

The internal `define.py` module, imported by `user_support.py`, imports `requests` and defines `CommonMethods.get_network_time()`.

The function explicitly executes:

```text
requests.get("http://worldtimeapi.org/api/timezone/Asia/Shanghai.txt", timeout=5)
```

It then searches the response for a `datetime:` marker and retries up to 10 times, waiting 1 second after an exception.

This demonstrates **concrete outbound HTTP capability** inside `czur_create` and an explicit endpoint related to Asia/Shanghai time synchronisation.

### Finding 2 · the observed licensing path does not call `get_network_time()`

References to `CommonMethods` inside the disassembled `user_support.py` bytecode were traced.

Observed calls are:

- `CommonMethods.is_in_enum(...)`;
- `CommonMethods.get_first_ethernet_mac()`.

No call to `CommonMethods.get_network_time()` appears in `user_support.py`.

Therefore:

```text
NETWORK_FUNCTION_PRESENT = CONFIRMED
NETWORK_FUNCTION_CALLED_FROM_USER_SUPPORT = NOT OBSERVED
```

The presence of the function does not demonstrate that it executes during licensing.

### Finding 3 · the observed UDP socket is used for `ioctl`, not transmission

`CommonMethods.get_first_ethernet_mac()` creates a socket:

```text
socket.socket(AF_INET, SOCK_DGRAM)
```

but the descriptor is immediately used with `fcntl.ioctl(..., 35111, ...)` to retrieve the MAC address of a network interface.

No `connect`, `send` or `recv` calls associated with that socket appear in the audited body. Its observed function is local: retrieving interface information through `ioctl`.

`user_support.get_udev_uuid()` does call `get_first_ethernet_mac()` together with local `df`/`udevadm` commands to construct machine/license identifiers.

### Interpretation

At this depth of the Python licensing path:

```text
LICENSE / MACHINE ID DATA            = CONFIRMED
LOCAL MAC / UUID / SERIAL            = CONFIRMED
HTTP TIME FUNCTION IN define.py      = CONFIRMED
CALL TO THAT FUNCTION FROM LICENSE   = NOT OBSERVED
SOCKET FOR MAC VIA IOCTL             = CONFIRMED LOCAL
LICENSE DATA SENT TO NETWORK         = NOT DEMONSTRATED
```

This reduces the hypothesis that the `main.py -> user_support.py -> data_support.py` flow itself directly sends license data, while still not excluding other routes in the executable or the main application.

`CAPABILITY != INVOCATION != TRAFFIC != IMPROPER TRANSMISSION`.

# Addendum IX · CZUR ET24 Pro Linux · `define.py`, hora de red y ruta real de licencia

**Fecha:** 2026-09-09  
**Estado:** auditoría estática incremental / síntesis abierta  
**Ámbito:** paquete oficial CZUR Scanner Linux 1.0.20250413

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

### Finding 1 · `define.py` contains a concrete network function

The internal module `define.py`, imported by `user_support.py`, imports `requests` and defines `CommonMethods.get_network_time()`.

It explicitly performs:

```text
requests.get("http://worldtimeapi.org/api/timezone/Asia/Shanghai.txt", timeout=5)
```

and parses a `datetime:` value, retrying on failure.

This confirms a concrete HTTP capability and endpoint inside `czur_create`.

### Finding 2 · the observed licensing path does not call it

The disassembled `user_support.py` references to `CommonMethods` were traced. Observed calls are `is_in_enum(...)` and `get_first_ethernet_mac()`; no call to `get_network_time()` was observed.

### Finding 3 · the UDP socket is used locally for `ioctl`

`get_first_ethernet_mac()` creates an `AF_INET/SOCK_DGRAM` socket and uses its file descriptor with `fcntl.ioctl(..., 35111, ...)` to retrieve interface MAC data. No associated `connect`, `send`, or `recv` call was observed in that body.

### Current classification

```text
LICENSE / MACHINE DATA HANDLING      = CONFIRMED
LOCAL MAC / UUID / SERIAL HANDLING   = CONFIRMED
HTTP TIME FUNCTION IN define.py      = CONFIRMED
CALL FROM LICENSING PATH             = NOT OBSERVED
LICENSE DATA NETWORK EGRESS          = NOT DEMONSTRATED
MALWARE                              = NOT DEMONSTRATED
```

Next static targets remain the proprietary application modules that may invoke Alibaba Cloud / OSS / KMS or reporting paths.
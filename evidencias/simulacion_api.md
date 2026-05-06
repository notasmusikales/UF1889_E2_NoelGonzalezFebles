# Simulación 
### Objetivo

Simular los datos que podrían enviarse desde Odoo hacia otro sistema mediante una API.

### Endpoint simulado

```text
POST /api/clientes/seguimientos
```
```json
[
    {
    "nombre_completo": "OpenWood",
    "correo_electronico": "ErikNFrench@armyspy.com",
    "numero_seguimientos": 3,
    "actividades": [
      "Reunión",
    ]
  },
]
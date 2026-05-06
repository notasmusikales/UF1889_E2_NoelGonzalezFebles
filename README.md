# UF1889
## Identificar modelos de clientes
- Clientes -> res.partner (almacena clientes)
- Seguimientos -> mail.activity (almacena actividades/seguimientos)

### Modelo de clientes
res.partner

Campos útiles:
- `name`
- `email`
- `phone`
- `is_company`
- `customer_rank`
- `active`

### Modelo de seguimientos
`mail.activity`

Campos útiles:
- `res_model`
- `res_id`
- `activity_type_id`
- `summary`
- `date_deadline`
- `usser_id`
- `create_date`

### Relación entre modelos

- En `mail.activity`, el registro apunta a un modelo y a un identificador.
- Cuando el `res_model = 'res_partner'`, y `res_id` coincide con el id del cliente, esa peertenece a ese cliente.

### Decisión final

Para esta práctica se considera "cliente" a los registros del modelo `res.partner` con `customer_rank > 0`, y "seguimiento" a los registros del modelo `mail.activity` asociados al cliente `rs_model = 'res.partner'` y `res_id=<id del cliente>` 
# Función que calcula el campo calculado
```python
    @api.depends('activity_ids')
    def _compute_activity_followup_count(self):
        activity_data = self.env['mail.activity'].read_group(
            [
                ('res_model', '=', 'res.partner'),
                ('res_id', 'in', self.ids),
            ],
            ['res_id'],
            ['res_id']
        )

        mapped_data = {data['res_id']: data['res_id_count'] for data in activity_data}

        for partner in self:
            partner.activity_followup_count = mapped_data.get(partner.id, 0)
```
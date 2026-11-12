# Temperature Sensor (HACS template)

HACS **template** category repository: distributes reusable Jinja2
macros for Home Assistant templates — not an integration, not a sensor
entity. HACS installs `temperature_sensor.jinja` into
`config/custom_templates/` automatically.

## Macros

| Macro | Description |
|---|---|
| `outdoor_temperature_fahrenheit(entity_id='sensor.temperature_sensor')` | Reads the given entity (defaults to the suggested id below) and converts it to °F directly. |
| `celsius_to_fahrenheit(celsius)` | Converts a raw °C value to °F, rounded to 1 decimal. |
| `format_temperature(value, unit='°C')` | Formats a number with a unit suffix. |
| `comfort_label(celsius)` | Returns a comfort label: Cold/Cool/Comfortable/Warm/Hot. |

## Suggested entity name

Name your real sensor **`sensor.temperature_sensor`** to use
`outdoor_temperature_fahrenheit()` with no argument. Any other id still
works, just pass it explicitly.

## Usage

In any Home Assistant template (automation, template sensor, script):

```jinja
{% from 'temperature_sensor.jinja' import outdoor_temperature_fahrenheit, celsius_to_fahrenheit, comfort_label %}
{{ outdoor_temperature_fahrenheit() }}°F
{{ celsius_to_fahrenheit(states('sensor.outdoor_temperature')) }}°F
{{ comfort_label(states('sensor.outdoor_temperature')) }}
```

After HACS installs/updates the file it calls `reload_custom_templates`
automatically — no restart needed. For manual install (no HACS), copy
`temperature_sensor.jinja` into `config/custom_templates/` yourself and
call `homeassistant.reload_custom_templates` once.

## Dashboard note

This repo creates no entity, so no statistics-graph/history card can
show anything for it — macros can only be used inside a template-aware
card (e.g. Markdown) to render a live computed value, no stored history.

## Publishing requirements (HACS "template" category)

- `temperature_sensor.jinja` at repo root (not in a subfolder).
- `hacs.json` with `"filename"` matching that file exactly.
- At least one GitHub release/tag.
- Repo description + topic set for discoverability.

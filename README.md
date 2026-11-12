# Temperature Sensor (Home Assistant Template Sensor)

Template sensor — derives a temperature value from an existing
entity/attribute via Jinja2. No Python, no `custom_components`, no HACS.

## Install

1. Edit [`packages/temperature_sensor.yaml`](packages/temperature_sensor.yaml):
   replace `sensor.SOURCE_ENTITY` with your real source entity (another
   sensor, a weather entity attribute, an MQTT topic sensor, etc.).
2. Include it in `configuration.yaml`:
   - If using [packages](https://www.home-assistant.io/docs/configuration/packages/):
     drop the file in your `packages/` folder — picked up automatically.
   - Otherwise: `template: !include packages/temperature_sensor.yaml`
     (only works if you don't already have another top-level `template:`
     key — merge the `sensor:` list into it if you do).
3. Restart Home Assistant, or reload without restarting: Developer
   Tools → YAML → **Reload All** (or just the "Template Entities" entry).

This creates `sensor.temperature_sensor`.

## Statistics graph visibility

- **Near-default, zero config:** the auto-generated "Overview" dashboard
  already shows a mini history graph for the new sensor automatically.
- **Full statistics-graph card (mean/min/max):** add it manually —
  dashboard → Edit → Add Card → Manual (YAML) → paste
  [`dashboards/example_card.yaml`](dashboards/example_card.yaml).

## Structure

```
packages/temperature_sensor.yaml   # the template sensor definition
dashboards/example_card.yaml       # optional statistics-graph card
```

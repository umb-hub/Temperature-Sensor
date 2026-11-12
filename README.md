# Temperature Sensor (Home Assistant custom integration template)

HACS-ready template for a Home Assistant custom integration. Rename
`temperature_sensor` (folder, domain, class names) to your integration's
real name once decided.

## Structure

```
custom_components/temperature_sensor/
  __init__.py        # setup/unload entry points
  manifest.json       # domain, version, requirements
  config_flow.py       # UI setup flow
  const.py            # domain + option keys
  sensor.py            # SensorEntity platform
  strings.json / translations/en.json
tests/                  # pytest-homeassistant-custom-component tests
dashboards/             # example Lovelace cards
.github/workflows/      # hassfest + HACS validation CI
hacs.json
```

## Statistics graph after install

Home Assistant integrations cannot auto-inject Lovelace cards (no
supported API for that) — add the card manually once after setup:

1. Settings → Devices & Services → add this integration, note the entity id
   it creates (Settings → Devices & Services → Temperature Sensor → Entities).
2. Open your dashboard → Edit → Add Card → Manual (YAML) → paste
   [`dashboards/example_card.yaml`](dashboards/example_card.yaml), replacing
   the entity id with yours.

The card uses the built-in `statistics-graph` type, so it shows
mean/min/max history as soon as the sensor has recorded data.

## Development

```bash
pip install -r requirements_test.txt
pytest tests/
```

CI runs `hassfest` (manifest/structure validation) and the HACS action on
every push.

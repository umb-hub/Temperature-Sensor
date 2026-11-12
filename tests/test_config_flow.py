"""Tests for the config flow."""
from unittest.mock import AsyncMock

from homeassistant import config_entries, data_entry_flow
from homeassistant.core import HomeAssistant

from custom_components.temperature_sensor.const import DOMAIN


async def test_user_flow_creates_entry(hass: HomeAssistant) -> None:
    """A valid host creates a config entry."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"host": "192.168.1.10"}
    )
    assert result["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result["title"] == "192.168.1.10"

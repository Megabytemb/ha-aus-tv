"""Sensor platform for aus_tv."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
)

from .const import DOMAIN, NAME
from .coordinator import AusTVUpdateCoordinator

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="channelCount",
        name="Channel count",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_devices: AddEntitiesCallback
):
    """Set up the sensor platform."""
    coordinator: AusTVUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_devices(
        TVGuideSensor(
            config_entry=entry,
            entity_description=entity_description,
            coordinator=coordinator,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class TVGuideSensor(CoordinatorEntity[AusTVUpdateCoordinator], SensorEntity):
    """aus_tv Sensor class."""

    def __init__(
        self,
        config_entry: ConfigEntry,
        entity_description,
        coordinator: AusTVUpdateCoordinator,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._config_entry = config_entry
        self._name = NAME
        self._attr_unique_id = f"{config_entry.entry_id}-sensor"
        self.coordinator: AusTVUpdateCoordinator = coordinator

    @property
    def native_value(self) -> str:
        """Return the native value of the sensor."""
        return len(self.coordinator.data)

"""DataUpdateCoordinator for the Aus TV integration."""
from datetime import timedelta
import logging

import aiohttp

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)

from .const import API_URL, DOMAIN

_LOGGER = logging.getLogger(__name__)


class AusTVUpdateCoordinator(DataUpdateCoordinator):
    """Aus TV Data coordinator."""

    config_entry: ConfigEntry

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialise a custom coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=60),
        )
        self.session: aiohttp.ClientSession = async_get_clientsession(hass)
        self.raw_data = {}

    async def _async_update_data(self):
        """Fetch data from API endpoint."""
        async with self.session.get(API_URL) as resp:
            self.raw_data = await resp.json()

        channels = {}

        raw_channels = self.raw_data[0].get("channels")
        for channel in raw_channels:
            if "adPlacement" in channel:
                continue
            if "fixedAd" in channel:
                continue

            channels[channel["number"]] = channel

        _LOGGER.debug(channels)
        return channels

"""Config flow to configure the Aus TV integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant import config_entries
from homeassistant.config_entries import (
    CONN_CLASS_CLOUD_POLL,
)
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class FacebookMessengerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Aus TV."""

    VERSION = 1
    DOMAIN = DOMAIN
    CONNECTION_CLASS = CONN_CLASS_CLOUD_POLL

    @property
    def logger(self):
        """Return logger."""
        return _LOGGER

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle initial user step."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        # if user_input is not None:
        return self.async_create_entry(
            title="Aus TV",
            data={},
        )

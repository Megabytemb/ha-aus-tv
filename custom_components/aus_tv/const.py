"""Constants for aus_tv."""

################################
# Do not change! Will be set by release workflow
INTEGRATION_VERSION = "main"  # git tag will be used
MIN_REQUIRED_HA_VERSION = "0.0.0"  # set min required version in hacs.json
################################

NAME = "Australia TV Guide"
DOMAIN = "aus_tv"
ATTRIBUTION = "Data provided by YourTV.com.au"

API_URL = """https://www.yourtv.com.au/api/now-next/?format=json&timezone=Australia%2FSydney&region=73"""

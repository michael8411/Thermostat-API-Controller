# py-nest-controller

Typed async Python SDK for the Google Smart Device Management (SDM) API,
focused on the Nest Thermostat E. See `docs/ARCHITECTURE.md` for the design.

## Setup

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Register for Device Access and create a project:
   https://developers.google.com/nest/device-access/get-started

   - In Google Cloud, enable the Smart Device Management API and create an
     OAuth 2.0 Client ID (type: Web application) with the authorized redirect
     URI `https://www.google.com`.
   - In the Device Access Console, create a project using that OAuth client ID.
     Note the Device Access project ID (a UUID). It is not the Google Cloud
     project ID.

4. Create your env file and fill in the client ID, client secret, and Device
   Access project ID:

   ```bash
   copy .env.example .env
   ```

5. Run the one time authorization (after implementing `auth/onboarding.py` and
   `auth/cli.py`):

   ```bash
   uv run nest-auth url
   ```

   Open the printed URL, approve access, and copy the `code` value from the
   address bar of the page you land on. Then:

   ```bash
   uv run nest-auth exchange PASTE_CODE_HERE
   ```

   Put the printed refresh token into `NEST_REFRESH_TOKEN` in `.env`.

6. Check the toolchain:

   ```bash
   uv run ruff check
   ```

   ```bash
   uv run ruff format --check
   ```

   ```bash
   uv run mypy
   ```

   ```bash
   uv run pytest
   ```

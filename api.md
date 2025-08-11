# AlbotAPISDK

Methods:

- <code title="get /">client.<a href="./src/albot_api_sdk/_client.py">get_root</a>() -> object</code>

# Oauth2

Types:

```python
from albot_api_sdk.types import PlainAPIResponse, URLAPIResponse
```

Methods:

- <code title="post /oauth2/callback">client.oauth2.<a href="./src/albot_api_sdk/resources/oauth2.py">callback</a>(\*\*<a href="src/albot_api_sdk/types/oauth2_callback_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="post /oauth2/logout">client.oauth2.<a href="./src/albot_api_sdk/resources/oauth2.py">logout</a>() -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="get /oauth2/login">client.oauth2.<a href="./src/albot_api_sdk/resources/oauth2.py">redirect</a>(\*\*<a href="src/albot_api_sdk/types/oauth2_redirect_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/url_api_response.py">URLAPIResponse</a></code>

# Shards

Types:

```python
from albot_api_sdk.types import (
    ShardListResponse,
    ShardAssignResponse,
    ShardGetConnectionCommandsResponse,
)
```

Methods:

- <code title="get /shards">client.shards.<a href="./src/albot_api_sdk/resources/shards.py">list</a>(\*\*<a href="src/albot_api_sdk/types/shard_list_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/shard_list_response.py">ShardListResponse</a></code>
- <code title="get /shards/assign">client.shards.<a href="./src/albot_api_sdk/resources/shards.py">assign</a>() -> <a href="./src/albot_api_sdk/types/shard_assign_response.py">ShardAssignResponse</a></code>
- <code title="get /shards/{shard_id}/connection_commands">client.shards.<a href="./src/albot_api_sdk/resources/shards.py">get_connection_commands</a>(shard_id, \*\*<a href="src/albot_api_sdk/types/shard_get_connection_commands_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/shard_get_connection_commands_response.py">ShardGetConnectionCommandsResponse</a></code>
- <code title="post /shards/{shard_id}/metrics">client.shards.<a href="./src/albot_api_sdk/resources/shards.py">post_metrics</a>(shard_id, \*\*<a href="src/albot_api_sdk/types/shard_post_metrics_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="post /shards/{shard_id}/release">client.shards.<a href="./src/albot_api_sdk/resources/shards.py">release</a>(shard_id) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

# Guilds

Types:

```python
from albot_api_sdk.types import ListSubscriptions, GuildCreateConnectionStatesResponse
```

Methods:

- <code title="post /guilds/{guild_id}">client.guilds.<a href="./src/albot_api_sdk/resources/guilds/guilds.py">create</a>(guild_id) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="delete /guilds/{guild_id}">client.guilds.<a href="./src/albot_api_sdk/resources/guilds/guilds.py">delete</a>(guild_id) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="post /guilds/{guild_id}/connection_states">client.guilds.<a href="./src/albot_api_sdk/resources/guilds/guilds.py">create_connection_states</a>(guild_id, \*\*<a href="src/albot_api_sdk/types/guild_create_connection_states_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/guild_create_connection_states_response.py">GuildCreateConnectionStatesResponse</a></code>
- <code title="post /guilds/{guild_id}/quick_reports">client.guilds.<a href="./src/albot_api_sdk/resources/guilds/guilds.py">create_quick_report</a>(guild_id, \*\*<a href="src/albot_api_sdk/types/guild_create_quick_report_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="get /guilds/{guild_id}/subscriptions">client.guilds.<a href="./src/albot_api_sdk/resources/guilds/guilds.py">list_subscriptions</a>(guild_id) -> <a href="./src/albot_api_sdk/types/list_subscriptions.py">ListSubscriptions</a></code>

## Dict

Types:

```python
from albot_api_sdk.types.guilds import DictRetrieveResponse
```

Methods:

- <code title="get /guilds/{guild_id}/dict">client.guilds.dict.<a href="./src/albot_api_sdk/resources/guilds/dict.py">retrieve</a>(guild_id) -> <a href="./src/albot_api_sdk/types/guilds/dict_retrieve_response.py">DictRetrieveResponse</a></code>
- <code title="delete /guilds/{guild_id}/dict">client.guilds.dict.<a href="./src/albot_api_sdk/resources/guilds/dict.py">delete</a>(guild_id) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="put /guilds/{guild_id}/dict">client.guilds.dict.<a href="./src/albot_api_sdk/resources/guilds/dict.py">replace</a>(guild_id, \*\*<a href="src/albot_api_sdk/types/guilds/dict_replace_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

## Settings

Types:

```python
from albot_api_sdk.types.guilds import SettingRetrieveResponse
```

Methods:

- <code title="get /guilds/{guild_id}/settings">client.guilds.settings.<a href="./src/albot_api_sdk/resources/guilds/settings.py">retrieve</a>(guild_id) -> <a href="./src/albot_api_sdk/types/guilds/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
- <code title="post /guilds/{guild_id}/settings">client.guilds.settings.<a href="./src/albot_api_sdk/resources/guilds/settings.py">update</a>(guild_id, \*\*<a href="src/albot_api_sdk/types/guilds/setting_update_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="delete /guilds/{guild_id}/settings">client.guilds.settings.<a href="./src/albot_api_sdk/resources/guilds/settings.py">delete</a>(guild_id) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

## CharacterUsage

Types:

```python
from albot_api_sdk.types.guilds import (
    CharacterUsage,
    CharacterUsages,
    CharacterUsageRetrieveResponse,
)
```

Methods:

- <code title="get /guilds/{guild_id}/character_usage">client.guilds.character_usage.<a href="./src/albot_api_sdk/resources/guilds/character_usage.py">retrieve</a>(guild_id) -> <a href="./src/albot_api_sdk/types/guilds/character_usage_retrieve_response.py">CharacterUsageRetrieveResponse</a></code>
- <code title="post /guilds/{guild_id}/character_usage">client.guilds.character_usage.<a href="./src/albot_api_sdk/resources/guilds/character_usage.py">update</a>(guild_id, \*\*<a href="src/albot_api_sdk/types/guilds/character_usage_update_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

## TrustedRoles

Types:

```python
from albot_api_sdk.types.guilds import TrustedRoleListResponse
```

Methods:

- <code title="put /guilds/{guild_id}/trusted_roles">client.guilds.trusted_roles.<a href="./src/albot_api_sdk/resources/guilds/trusted_roles.py">update</a>(guild_id, \*\*<a href="src/albot_api_sdk/types/guilds/trusted_role_update_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="get /guilds/{guild_id}/trusted_roles">client.guilds.trusted_roles.<a href="./src/albot_api_sdk/resources/guilds/trusted_roles.py">list</a>(guild_id) -> <a href="./src/albot_api_sdk/types/guilds/trusted_role_list_response.py">TrustedRoleListResponse</a></code>

## ConnectionCommand

Types:

```python
from albot_api_sdk.types.guilds import ConnectionCommand, ConnectionCommandRetrieveResponse
```

Methods:

- <code title="get /guilds/{guild_id}/connection_command">client.guilds.connection_command.<a href="./src/albot_api_sdk/resources/guilds/connection_command.py">retrieve</a>(guild_id) -> <a href="./src/albot_api_sdk/types/guilds/connection_command_retrieve_response.py">ConnectionCommandRetrieveResponse</a></code>
- <code title="put /guilds/{guild_id}/connection_command">client.guilds.connection_command.<a href="./src/albot_api_sdk/resources/guilds/connection_command.py">update</a>(guild_id, \*\*<a href="src/albot_api_sdk/types/guilds/connection_command_update_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

## MessageLinkExpandPreference

Types:

```python
from albot_api_sdk.types.guilds import (
    MessageLinkExpandPreference,
    MessageLinkExpandPreferenceRetrieveResponse,
)
```

Methods:

- <code title="get /guilds/{guild_id}/message_link_expand_preference">client.guilds.message_link_expand_preference.<a href="./src/albot_api_sdk/resources/guilds/message_link_expand_preference.py">retrieve</a>(guild_id) -> <a href="./src/albot_api_sdk/types/guilds/message_link_expand_preference_retrieve_response.py">MessageLinkExpandPreferenceRetrieveResponse</a></code>
- <code title="post /guilds/{guild_id}/message_link_expand_preference">client.guilds.message_link_expand_preference.<a href="./src/albot_api_sdk/resources/guilds/message_link_expand_preference.py">update</a>(guild_id, \*\*<a href="src/albot_api_sdk/types/guilds/message_link_expand_preference_update_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

# Users

## Me

Types:

```python
from albot_api_sdk.types.users import MeRetrieveInfoResponse
```

Methods:

- <code title="post /users/me/checkout-session">client.users.me.<a href="./src/albot_api_sdk/resources/users/me/me.py">create_checkout_session</a>(\*\*<a href="src/albot_api_sdk/types/users/me_create_checkout_session_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/url_api_response.py">URLAPIResponse</a></code>
- <code title="get /users/me/info">client.users.me.<a href="./src/albot_api_sdk/resources/users/me/me.py">retrieve_info</a>() -> <a href="./src/albot_api_sdk/types/users/me_retrieve_info_response.py">MeRetrieveInfoResponse</a></code>

### Subscriptions

Types:

```python
from albot_api_sdk.types.users.me import SubscriptionActivate, SubscriptionRenew
```

Methods:

- <code title="get /users/me/subscriptions">client.users.me.subscriptions.<a href="./src/albot_api_sdk/resources/users/me/subscriptions.py">list</a>() -> <a href="./src/albot_api_sdk/types/list_subscriptions.py">ListSubscriptions</a></code>
- <code title="post /users/me/subscriptions/{sub_id}/activate">client.users.me.subscriptions.<a href="./src/albot_api_sdk/resources/users/me/subscriptions.py">activate</a>(sub_id, \*\*<a href="src/albot_api_sdk/types/users/me/subscription_activate_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="post /users/me/subscriptions/{sub_id}/cancel">client.users.me.subscriptions.<a href="./src/albot_api_sdk/resources/users/me/subscriptions.py">cancel</a>(sub_id) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="post /users/me/subscriptions/{sub_id}/renew">client.users.me.subscriptions.<a href="./src/albot_api_sdk/resources/users/me/subscriptions.py">renew</a>(sub_id, \*\*<a href="src/albot_api_sdk/types/users/me/subscription_renew_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

### Guilds

Types:

```python
from albot_api_sdk.types.users.me import PartialGuild, GuildListResponse, GuildRetrieveInfoResponse
```

Methods:

- <code title="get /users/me/guilds">client.users.me.guilds.<a href="./src/albot_api_sdk/resources/users/me/guilds.py">list</a>(\*\*<a href="src/albot_api_sdk/types/users/me/guild_list_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/users/me/guild_list_response.py">GuildListResponse</a></code>
- <code title="get /users/me/guilds/{guild_id}/info">client.users.me.guilds.<a href="./src/albot_api_sdk/resources/users/me/guilds.py">retrieve_info</a>(guild_id) -> <a href="./src/albot_api_sdk/types/users/me/guild_retrieve_info_response.py">GuildRetrieveInfoResponse</a></code>

## Subscriptions

Methods:

- <code title="get /users/{user_id}/subscriptions">client.users.subscriptions.<a href="./src/albot_api_sdk/resources/users/subscriptions.py">list</a>(user_id) -> <a href="./src/albot_api_sdk/types/list_subscriptions.py">ListSubscriptions</a></code>
- <code title="post /users/{user_id}/subscriptions/{sub_id}/activate">client.users.subscriptions.<a href="./src/albot_api_sdk/resources/users/subscriptions.py">activate</a>(sub_id, \*, user_id, \*\*<a href="src/albot_api_sdk/types/users/subscription_activate_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="post /users/{user_id}/subscriptions/{sub_id}/cancel">client.users.subscriptions.<a href="./src/albot_api_sdk/resources/users/subscriptions.py">cancel</a>(sub_id, \*, user_id) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>
- <code title="post /users/{user_id}/subscriptions/{sub_id}/renew">client.users.subscriptions.<a href="./src/albot_api_sdk/resources/users/subscriptions.py">renew</a>(sub_id, \*, user_id, \*\*<a href="src/albot_api_sdk/types/users/subscription_renew_params.py">params</a>) -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

# Metrics

Types:

```python
from albot_api_sdk.types import MetricRetrieveResponse
```

Methods:

- <code title="get /metrics">client.metrics.<a href="./src/albot_api_sdk/resources/metrics.py">retrieve</a>() -> <a href="./src/albot_api_sdk/types/metric_retrieve_response.py">MetricRetrieveResponse</a></code>

# Webhooks

Methods:

- <code title="post /webhooks/stripe">client.webhooks.<a href="./src/albot_api_sdk/resources/webhooks.py">create_stripe</a>() -> <a href="./src/albot_api_sdk/types/plain_api_response.py">PlainAPIResponse</a></code>

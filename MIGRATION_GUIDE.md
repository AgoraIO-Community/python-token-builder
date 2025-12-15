# Migration Guide: Version 1 to Version 2

This guide helps you migrate from the legacy Version 1 token builders to the new Version 2 API.

## Overview

Version 2 introduces a service-based architecture with granular privilege control, replacing the simpler channel-based approach of Version 1.

### Key Benefits of Version 2

- **Granular Privilege Control**: Set different expiration times for each privilege
- **Multi-Service Tokens**: Combine RTC, RTM, and Chat in a single token
- **Enhanced Security**: More flexible control over user permissions
- **Better Performance**: Optimized token format (version 007)
- **Modern API**: Snake_case naming and clearer parameter names

## Breaking Changes

### 1. Import Names

**Version 1:**
```python
from agora_token_builder import RtcTokenBuilder, RtmTokenBuilder
```

**Version 2:**
```python
from agora_token_builder import RtcTokenBuilder2, RtmTokenBuilder2, ChatTokenBuilder
```

### 2. Method Names

Version 2 uses snake_case instead of camelCase:

| Version 1 | Version 2 |
|-----------|-----------|
| `buildTokenWithUid()` | `build_token_with_uid()` |
| `buildTokenWithAccount()` | `build_token_with_user_account()` |
| `buildToken()` | `build_token()` |

### 3. Parameter Names

| Version 1 | Version 2 |
|-----------|-----------|
| `appId` | `app_id` |
| `appCertificate` | `app_certificate` |
| `channelName` | `channel_name` |
| `userAccount` | `account` or `user_id` |
| `privilegeExpiredTs` | `privilege_expire` |

### 4. Time Format

**Version 1** uses absolute Unix timestamps:
```python
import time
expiration_timestamp = int(time.time()) + 3600  # 1 hour from now
```

**Version 2** uses relative time in seconds:
```python
token_expire = 3600  # Expires in 3600 seconds (1 hour)
privilege_expire = 3600
```

## Migration Examples

### RTC Token Migration

#### Before (Version 1):
```python
from agora_token_builder import RtcTokenBuilder, Role_Publisher
import time

app_id = "your_app_id"
app_certificate = "your_certificate"
channel_name = "test_channel"
uid = 12345
role = Role_Publisher
expiration_timestamp = int(time.time()) + 3600

token = RtcTokenBuilder.buildTokenWithUid(
    app_id,
    app_certificate,
    channel_name,
    uid,
    role,
    expiration_timestamp
)
```

#### After (Version 2):
```python
from agora_token_builder import RtcTokenBuilder2, Role_Publisher

app_id = "your_app_id"
app_certificate = "your_certificate"
channel_name = "test_channel"
uid = 12345
role = Role_Publisher
token_expire = 3600
privilege_expire = 3600

token = RtcTokenBuilder2.build_token_with_uid(
    app_id,
    app_certificate,
    channel_name,
    uid,
    role,
    token_expire,
    privilege_expire
)
```

### RTM Token Migration

#### Before (Version 1):
```python
from agora_token_builder import RtmTokenBuilder, Role_Rtm_User
import time

app_id = "your_app_id"
app_certificate = "your_certificate"
user_account = "test_user"
role = Role_Rtm_User
expiration_timestamp = int(time.time()) + 3600

token = RtmTokenBuilder.buildToken(
    app_id,
    app_certificate,
    user_account,
    role,
    expiration_timestamp
)
```

#### After (Version 2):
```python
from agora_token_builder import RtmTokenBuilder2

app_id = "your_app_id"
app_certificate = "your_certificate"
user_id = "test_user"
expire = 3600

token = RtmTokenBuilder2.build_token(
    app_id,
    app_certificate,
    user_id,
    expire
)
```

## Advanced Features in Version 2

### Granular Privilege Control

Version 2 allows you to set different expiration times for each privilege:

```python
from agora_token_builder import RtcTokenBuilder2

token = RtcTokenBuilder2.build_token_with_uid_and_privilege(
    app_id="your_app_id",
    app_certificate="your_certificate",
    channel_name="test_channel",
    uid=12345,
    token_expire=3600,
    join_channel_privilege_expire=3600,      # Can join for 1 hour
    pub_audio_privilege_expire=7200,         # Can publish audio for 2 hours
    pub_video_privilege_expire=7200,         # Can publish video for 2 hours
    pub_data_stream_privilege_expire=3600    # Can publish data for 1 hour
)
```

### Combined RTC + RTM Tokens

Version 2 makes it easy to create tokens for multiple services:

```python
from agora_token_builder import RtcTokenBuilder2, Role_Publisher

# Simple combined token
token = RtcTokenBuilder2.build_token_with_rtm(
    app_id="your_app_id",
    app_certificate="your_certificate",
    channel_name="test_channel",
    account="user_account",
    role=Role_Publisher,
    token_expire=3600,
    privilege_expire=3600
)

# Advanced combined token with separate RTM user
token = RtcTokenBuilder2.build_token_with_rtm2(
    app_id="your_app_id",
    app_certificate="your_certificate",
    channel_name="test_channel",
    rtc_account="user_account",
    rtc_role=Role_Publisher,
    rtc_token_expire=3600,
    join_channel_privilege_expire=3600,
    pub_audio_privilege_expire=7200,
    pub_video_privilege_expire=7200,
    pub_data_stream_privilege_expire=3600,
    rtm_user_id="different_user",  # Can be different from RTC account
    rtm_token_expire=3600
)
```

### Multi-Service Tokens with AccessToken2

For maximum flexibility, use AccessToken2 directly:

```python
from agora_token_builder import AccessToken, ServiceRtc, ServiceRtm, ServiceChat

token = AccessToken(
    app_id="your_app_id",
    app_certificate="your_certificate",
    expire=3600
)

# Add RTC service
rtc_service = ServiceRtc(channel_name="test_channel", uid="12345")
rtc_service.add_privilege(ServiceRtc.kPrivilegeJoinChannel, 3600)
rtc_service.add_privilege(ServiceRtc.kPrivilegePublishAudioStream, 7200)
token.add_service(rtc_service)

# Add RTM service
rtm_service = ServiceRtm(user_id="user_123")
rtm_service.add_privilege(ServiceRtm.kPrivilegeLogin, 3600)
token.add_service(rtm_service)

# Add Chat service
chat_service = ServiceChat(user_id="user_123")
chat_service.add_privilege(ServiceChat.kPrivilegeUser, 3600)
token.add_service(chat_service)

result = token.build()
```

## Migration Checklist

- [ ] Update import statements to use Version 2 classes
- [ ] Change method names from camelCase to snake_case
- [ ] Update parameter names to snake_case
- [ ] Convert timestamp calculations from absolute to relative time
- [ ] Remove `import time` if only used for token expiration
- [ ] Update role constant imports if needed
- [ ] Test token generation with your Agora application
- [ ] Update error handling if relying on specific exceptions
- [ ] Review and update any token validation logic

## Backward Compatibility

Both Version 1 and Version 2 APIs are available in the same package:

```python
# Version 1 (legacy) - still works
from agora_token_builder import RtcTokenBuilder, RtmTokenBuilder

# Version 2 (recommended)
from agora_token_builder import RtcTokenBuilder2, RtmTokenBuilder2, ChatTokenBuilder
```

You can migrate incrementally, running both versions side by side during the transition.

## Token Compatibility

**Important**: Version 1 and Version 2 generate different token formats:
- Version 1 generates version **006** tokens
- Version 2 generates version **007** tokens

Both token formats are accepted by Agora services, but they are **not interchangeable**. Once you migrate your token generation to Version 2, all clients will receive version 007 tokens.

## Need Help?

- Check the [examples/](./examples/) directory for working code samples
- Review the [README.md](./README.md) for full API documentation
- Visit [Agora Documentation](https://docs.agora.io/) for service-specific guides
- See [Token Authentication Overview](https://docs.agora.io/en/video-calling/get-started/authentication-workflow)

## Best Practices

1. **Use Version 2 for new projects**: Start with the latest API
2. **Set appropriate expiration times**: Balance security and user experience
3. **Use granular privileges**: Only grant permissions users need
4. **Validate tokens server-side**: Never expose credentials to clients
5. **Implement token refresh**: Request new tokens before expiration
6. **Monitor token usage**: Track generation and validation for security

## Common Pitfalls

### ❌ Mixing time formats
```python
# Wrong: Mixing timestamp with seconds
import time
token = RtcTokenBuilder2.build_token_with_uid(
    app_id, app_certificate, channel_name, uid, role,
    token_expire=int(time.time()) + 3600,  # ❌ Should be 3600, not timestamp
    privilege_expire=3600
)
```

```python
# Correct: Use relative seconds
token = RtcTokenBuilder2.build_token_with_uid(
    app_id, app_certificate, channel_name, uid, role,
    token_expire=3600,  # ✅ 3600 seconds from now
    privilege_expire=3600
)
```

### ❌ Using wrong parameter names
```python
# Wrong: Using Version 1 parameter names
token = RtcTokenBuilder2.build_token_with_uid(
    appId=app_id,  # ❌ Should be app_id
    appCertificate=app_certificate,  # ❌ Should be app_certificate
    channelName=channel_name,  # ❌ Should be channel_name
    # ...
)
```

```python
# Correct: Use snake_case
token = RtcTokenBuilder2.build_token_with_uid(
    app_id=app_id,  # ✅
    app_certificate=app_certificate,  # ✅
    channel_name=channel_name,  # ✅
    # ...
)
```

### ❌ Forgetting to update imports
```python
# Wrong: Old import with new method
from agora_token_builder import RtcTokenBuilder  # ❌ Version 1 class
token = RtcTokenBuilder.build_token_with_uid(...)  # ❌ Version 2 method doesn't exist
```

```python
# Correct: Use Version 2 import
from agora_token_builder import RtcTokenBuilder2  # ✅
token = RtcTokenBuilder2.build_token_with_uid(...)  # ✅
```

## Summary

Version 2 offers significant improvements in flexibility, security, and developer experience. While the migration requires updating method names and time formats, the enhanced capabilities make it worthwhile for production applications.

Start with simple tokens using the builder methods, then explore advanced features like granular privileges and multi-service tokens as your needs grow.

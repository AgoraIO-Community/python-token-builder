# Agora Token Generator


# Description 
Token generator for building a token server with Python & the Agora RTM/RTC

## Installation
------------

```pip install agora-token-server```

## Usage
------------

###### RTC Live Video Calling & Chat SDK
```from agora_token_builder import RtcTokenBuilder```

```python
token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, uid, role, privilegeExpiredTs)
```

###### RTM Real-Time Messaging & Chat SDK
```from agora_token_builder import RtmTokenBuilder```


```python
token = RtmTokenBuilder.buildToken(appID, appCertificate, userAccount, role, privilegeExpiredTs)
```


## Settings

```appID```
<br>
The App ID issued to you by Agora. Apply for a new App ID from the gora Dashboard if it is missing from your kit. See Get an App ID.

```appCertificate```
<br>
	Certificate of the application that you registered in the Agora Dashboard. See Get an App Certificate.

```channelName```
<br>
Unique channel name for the AgoraRTC session in the string format

```uid```
<br>
User ID. A 32-bit unsigned integer with a value ranging from 1 to (232-1). optionalUid must be unique.

```userAccount```
The user account.

```role```
<br>
Role_Publisher = 1: A broadcaster (host) in a live-broadcast profile. Role_Subscriber = 2: (Default) A audience in a live-broadcast profile.

```privilegeExpireTs```
<br>
Represented by the number of seconds elapsed since 1/1/1970. If, for example, you want to access the Agora Service within 10 minutes after the token is generated, set expireTimestamp as the current


## License

© 2021 Agora.io

This repository is licensed under the MIT license. See LICENSE for details.

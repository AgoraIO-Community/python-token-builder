# Version 1 token builders (legacy)
from agora_token_builder.RtcTokenBuilder import RtcTokenBuilder, Role_Publisher as Role_Publisher
from agora_token_builder.RtmTokenBuilder import RtmTokenBuilder, Role_Rtm_User

# Version 2 token builders (AccessToken2 based)
from agora_token_builder.RtcTokenBuilder2 import RtcTokenBuilder as RtcTokenBuilder2
from agora_token_builder.RtcTokenBuilder2 import Role_Publisher, Role_Subscriber
from agora_token_builder.RtmTokenBuilder2 import RtmTokenBuilder as RtmTokenBuilder2
from agora_token_builder.ChatTokenBuilder2 import ChatTokenBuilder

# AccessToken2 classes for advanced usage
from agora_token_builder.AccessToken2 import (
    AccessToken,
    ServiceRtc,
    ServiceRtm,
    ServiceChat,
    ServiceFpa,
    ServiceApaas
)
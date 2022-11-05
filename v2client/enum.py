from dataclasses import dataclass


@dataclass
class ProxyTypes:
    VLESS = "vless"
    VMESS = "vmess"


@dataclass
class VMessSecurityTypes:
    UNKNOWN = "UNKNOWN"
    LEGACY = "LEGACY"
    AUTO = "AUTO"
    AES128_GCM = "AES128_GCM"
    CHACHA20_POLY1305 = "CHACHA20_POLY1305"
    NONE = "NONE"


@dataclass
class VLESSFlowTypes:
    XTLS_RPRX_DIRECT = "xtls-rprx-direct"
    XTLS_RPRX_ORIGIN = "xtls-rprx-origin"
    XTLS_RPRX_SPLICE = "xtls-rprx-splice"


@dataclass
class VLESSEncryptionTypes:
    NONE = "none"
    XSALSA20_POLY1305 = "xsalsa20-poly1305"
    CHACHA20_POLY1305 = "chacha20-poly1305"
    CHACHA20_IETF_POLY1305 = "chacha20-ietf-poly1305"

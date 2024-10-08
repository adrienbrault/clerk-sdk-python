"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .emailaddress import EmailAddress, EmailAddressTypedDict
from .phonenumber import PhoneNumber, PhoneNumberTypedDict
from .samlaccount import SAMLAccount, SAMLAccountTypedDict
from .schemas_passkey import SchemasPasskey, SchemasPasskeyTypedDict
from .web3wallet import Web3Wallet, Web3WalletTypedDict
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UserObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    USER = "user"

class PublicMetadataTypedDict(TypedDict):
    pass
    

class PublicMetadata(BaseModel):
    pass
    

class PrivateMetadataTypedDict(TypedDict):
    pass
    

class PrivateMetadata(BaseModel):
    pass
    

class UnsafeMetadataTypedDict(TypedDict):
    pass
    

class UnsafeMetadata(BaseModel):
    pass
    

class ExternalAccountsTypedDict(TypedDict):
    pass
    

class ExternalAccounts(BaseModel):
    pass
    

class UserTypedDict(TypedDict):
    id: NotRequired[str]
    object: NotRequired[UserObject]
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    external_id: NotRequired[Nullable[str]]
    primary_email_address_id: NotRequired[Nullable[str]]
    primary_phone_number_id: NotRequired[Nullable[str]]
    primary_web3_wallet_id: NotRequired[Nullable[str]]
    username: NotRequired[Nullable[str]]
    first_name: NotRequired[Nullable[str]]
    last_name: NotRequired[Nullable[str]]
    profile_image_url: NotRequired[str]
    image_url: NotRequired[str]
    has_image: NotRequired[bool]
    public_metadata: NotRequired[PublicMetadataTypedDict]
    private_metadata: NotRequired[Nullable[PrivateMetadataTypedDict]]
    unsafe_metadata: NotRequired[UnsafeMetadataTypedDict]
    email_addresses: NotRequired[List[EmailAddressTypedDict]]
    phone_numbers: NotRequired[List[PhoneNumberTypedDict]]
    web3_wallets: NotRequired[List[Web3WalletTypedDict]]
    passkeys: NotRequired[List[SchemasPasskeyTypedDict]]
    password_enabled: NotRequired[bool]
    two_factor_enabled: NotRequired[bool]
    totp_enabled: NotRequired[bool]
    backup_code_enabled: NotRequired[bool]
    mfa_enabled_at: NotRequired[Nullable[int]]
    r"""Unix timestamp of when MFA was last enabled for this user. It should be noted that this field is not nullified if MFA is disabled.

    """
    mfa_disabled_at: NotRequired[Nullable[int]]
    r"""Unix timestamp of when MFA was last disabled for this user. It should be noted that this field is not nullified if MFA is enabled again.

    """
    external_accounts: NotRequired[List[ExternalAccountsTypedDict]]
    saml_accounts: NotRequired[List[SAMLAccountTypedDict]]
    last_sign_in_at: NotRequired[Nullable[int]]
    r"""Unix timestamp of last sign-in.

    """
    banned: NotRequired[bool]
    r"""Flag to denote whether user is banned or not.

    """
    locked: NotRequired[bool]
    r"""Flag to denote whether user is currently locked, i.e. restricted from signing in or not.

    """
    lockout_expires_in_seconds: NotRequired[Nullable[int]]
    r"""The number of seconds remaining until the lockout period expires for a locked user. A null value for a locked user indicates that lockout never expires.

    """
    verification_attempts_remaining: NotRequired[Nullable[int]]
    r"""The number of verification attempts remaining until the user is locked. Null if account lockout is not enabled. Note: if a user is locked explicitly via the Backend API, they may still have verification attempts remaining.

    """
    updated_at: NotRequired[int]
    r"""Unix timestamp of last update.

    """
    created_at: NotRequired[int]
    r"""Unix timestamp of creation.

    """
    delete_self_enabled: NotRequired[bool]
    r"""If enabled, user can delete themselves via FAPI.

    """
    create_organization_enabled: NotRequired[bool]
    r"""If enabled, user can create organizations via FAPI.

    """
    last_active_at: NotRequired[Nullable[int]]
    r"""Unix timestamp of the latest session activity, with day precision.

    """
    

class User(BaseModel):
    id: Optional[str] = None
    object: Optional[UserObject] = None
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    external_id: OptionalNullable[str] = UNSET
    primary_email_address_id: OptionalNullable[str] = UNSET
    primary_phone_number_id: OptionalNullable[str] = UNSET
    primary_web3_wallet_id: OptionalNullable[str] = UNSET
    username: OptionalNullable[str] = UNSET
    first_name: OptionalNullable[str] = UNSET
    last_name: OptionalNullable[str] = UNSET
    profile_image_url: Annotated[Optional[str], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.")] = None
    image_url: Optional[str] = None
    has_image: Optional[bool] = None
    public_metadata: Optional[PublicMetadata] = None
    private_metadata: OptionalNullable[PrivateMetadata] = UNSET
    unsafe_metadata: Optional[UnsafeMetadata] = None
    email_addresses: Optional[List[EmailAddress]] = None
    phone_numbers: Optional[List[PhoneNumber]] = None
    web3_wallets: Optional[List[Web3Wallet]] = None
    passkeys: Optional[List[SchemasPasskey]] = None
    password_enabled: Optional[bool] = None
    two_factor_enabled: Optional[bool] = None
    totp_enabled: Optional[bool] = None
    backup_code_enabled: Optional[bool] = None
    mfa_enabled_at: OptionalNullable[int] = UNSET
    r"""Unix timestamp of when MFA was last enabled for this user. It should be noted that this field is not nullified if MFA is disabled.

    """
    mfa_disabled_at: OptionalNullable[int] = UNSET
    r"""Unix timestamp of when MFA was last disabled for this user. It should be noted that this field is not nullified if MFA is enabled again.

    """
    external_accounts: Optional[List[ExternalAccounts]] = None
    saml_accounts: Optional[List[SAMLAccount]] = None
    last_sign_in_at: OptionalNullable[int] = UNSET
    r"""Unix timestamp of last sign-in.

    """
    banned: Optional[bool] = None
    r"""Flag to denote whether user is banned or not.

    """
    locked: Optional[bool] = None
    r"""Flag to denote whether user is currently locked, i.e. restricted from signing in or not.

    """
    lockout_expires_in_seconds: OptionalNullable[int] = UNSET
    r"""The number of seconds remaining until the lockout period expires for a locked user. A null value for a locked user indicates that lockout never expires.

    """
    verification_attempts_remaining: OptionalNullable[int] = UNSET
    r"""The number of verification attempts remaining until the user is locked. Null if account lockout is not enabled. Note: if a user is locked explicitly via the Backend API, they may still have verification attempts remaining.

    """
    updated_at: Optional[int] = None
    r"""Unix timestamp of last update.

    """
    created_at: Optional[int] = None
    r"""Unix timestamp of creation.

    """
    delete_self_enabled: Optional[bool] = None
    r"""If enabled, user can delete themselves via FAPI.

    """
    create_organization_enabled: Optional[bool] = None
    r"""If enabled, user can create organizations via FAPI.

    """
    last_active_at: OptionalNullable[int] = UNSET
    r"""Unix timestamp of the latest session activity, with day precision.

    """
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "object", "external_id", "primary_email_address_id", "primary_phone_number_id", "primary_web3_wallet_id", "username", "first_name", "last_name", "profile_image_url", "image_url", "has_image", "public_metadata", "private_metadata", "unsafe_metadata", "email_addresses", "phone_numbers", "web3_wallets", "passkeys", "password_enabled", "two_factor_enabled", "totp_enabled", "backup_code_enabled", "mfa_enabled_at", "mfa_disabled_at", "external_accounts", "saml_accounts", "last_sign_in_at", "banned", "locked", "lockout_expires_in_seconds", "verification_attempts_remaining", "updated_at", "created_at", "delete_self_enabled", "create_organization_enabled", "last_active_at"]
        nullable_fields = ["external_id", "primary_email_address_id", "primary_phone_number_id", "primary_web3_wallet_id", "username", "first_name", "last_name", "private_metadata", "mfa_enabled_at", "mfa_disabled_at", "last_sign_in_at", "lockout_expires_in_seconds", "verification_attempts_remaining", "last_active_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

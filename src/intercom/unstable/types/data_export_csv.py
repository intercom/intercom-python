# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel


class DataExportCsv(UncheckedBaseModel):
    """
    A CSV output file
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user_id of the user who was sent the message.
    """

    user_external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The external_user_id of the user who was sent the message
    """

    company_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company ID of the user in relation to the message that was sent. Will return -1 if no company is present.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The users email who was sent the message.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full name of the user receiving the message
    """

    ruleset_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the message.
    """

    content_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The specific content that was received. In an A/B test each version has its own Content ID.
    """

    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email, Chat, Post etc.
    """

    content_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the content you see in your Intercom workspace.
    """

    ruleset_version_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    As you edit content we record new versions. This ID can help you determine which version of a piece of content that was received.
    """

    receipt_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID for this receipt. Will be included with any related stats in other files to identify this specific delivery of a message.
    """

    received_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp for when the receipt was recorded.
    """

    series_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the series that this content is part of. Will return -1 if not part of a series.
    """

    series_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the series that this content is part of.
    """

    node_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the series node that this ruleset is associated with. Each block in a series has a corresponding node_id.
    """

    first_reply: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time a user replied to this message if the content was able to receive replies.
    """

    first_completion: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time a user completed this message if the content was able to be completed e.g. Tours, Surveys.
    """

    first_series_completion: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time the series this message was a part of was completed by the user.
    """

    first_series_disengagement: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time the series this message was a part of was disengaged by the user.
    """

    first_series_exit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time the series this message was a part of was exited by the user.
    """

    first_goal_success: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time the user met this messages associated goal if one exists.
    """

    first_open: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time the user opened this message.
    """

    first_click: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time the series the user clicked on a link within this message.
    """

    first_dismisall: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time the series the user dismissed this message.
    """

    first_unsubscribe: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time the user unsubscribed from this message.
    """

    first_hard_bounce: typing.Optional[int] = pydantic.Field(default=None)
    """
    The first time this message hard bounced for this user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

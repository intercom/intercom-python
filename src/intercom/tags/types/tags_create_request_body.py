# This file was auto-generated by Fern from our API Definition.

import typing

from ...types.create_or_update_tag_request import CreateOrUpdateTagRequest
from ...types.tag_company_request import TagCompanyRequest
from ...types.tag_multiple_users_request import TagMultipleUsersRequest
from ...types.untag_company_request import UntagCompanyRequest

TagsCreateRequestBody = typing.Union[
    CreateOrUpdateTagRequest, TagCompanyRequest, UntagCompanyRequest, TagMultipleUsersRequest
]

# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from .article_translated_content import ArticleTranslatedContent
from .update_article_request_state import UpdateArticleRequestState


class UpdateArticleRequestBody(UncheckedBaseModel):
    """
    You can Update an Article
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the article.For multilingual articles, this will be the title of the default language's content.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the article. For multilingual articles, this will be the description of the default language's content.
    """

    body: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content of the article. For multilingual articles, this will be the body of the default language's content.
    """

    author_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the author of the article. For multilingual articles, this will be the id of the author of the default language's content. Must be a teammate on the help center's workspace.
    """

    state: typing.Optional[UpdateArticleRequestState] = pydantic.Field(default=None)
    """
    Whether the article will be `published` or will be a `draft`. Defaults to draft. For multilingual articles, this will be the state of the default language's content.
    """

    parent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the article's parent collection or section. An article without this field stands alone.
    """

    parent_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of parent, which can either be a `collection` or `section`.
    """

    translated_content: typing.Optional[ArticleTranslatedContent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

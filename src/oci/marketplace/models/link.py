# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Link(object):
    """
    The model for links.
    """

    #: A constant which can be used with the rel property of a Link.
    #: This constant has a value of "SELF"
    REL_SELF = "SELF"

    #: A constant which can be used with the rel property of a Link.
    #: This constant has a value of "CANONICAL"
    REL_CANONICAL = "CANONICAL"

    #: A constant which can be used with the rel property of a Link.
    #: This constant has a value of "NEXT"
    REL_NEXT = "NEXT"

    #: A constant which can be used with the rel property of a Link.
    #: This constant has a value of "TEMPLATE"
    REL_TEMPLATE = "TEMPLATE"

    #: A constant which can be used with the rel property of a Link.
    #: This constant has a value of "PREV"
    REL_PREV = "PREV"

    def __init__(self, **kwargs):
        """
        Initializes a new Link object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rel:
            The value to assign to the rel property of this Link.
            Allowed values for this property are: "SELF", "CANONICAL", "NEXT", "TEMPLATE", "PREV", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rel: str

        :param href:
            The value to assign to the href property of this Link.
        :type href: str

        """
        self.swagger_types = {
            'rel': 'str',
            'href': 'str'
        }

        self.attribute_map = {
            'rel': 'rel',
            'href': 'href'
        }

        self._rel = None
        self._href = None

    @property
    def rel(self):
        """
        Gets the rel of this Link.
        Reference links to the previous page, next page, and other pages.

        Allowed values for this property are: "SELF", "CANONICAL", "NEXT", "TEMPLATE", "PREV", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rel of this Link.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """
        Sets the rel of this Link.
        Reference links to the previous page, next page, and other pages.


        :param rel: The rel of this Link.
        :type: str
        """
        allowed_values = ["SELF", "CANONICAL", "NEXT", "TEMPLATE", "PREV"]
        if not value_allowed_none_or_none_sentinel(rel, allowed_values):
            rel = 'UNKNOWN_ENUM_VALUE'
        self._rel = rel

    @property
    def href(self):
        """
        Gets the href of this Link.
        The anchor tag.


        :return: The href of this Link.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this Link.
        The anchor tag.


        :param href: The href of this Link.
        :type: str
        """
        self._href = href

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

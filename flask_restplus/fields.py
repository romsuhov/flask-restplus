# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.restful import fields as base_fields
from .model import ApiModel


class DescriptionMixin(object):
    def __init__(self, *args, **kwargs):
        self.description = kwargs.pop('description', None)
        super(DescriptionMixin, self).__init__(*args, **kwargs)


class DetailsMixin(DescriptionMixin):
    def __init__(self, *args, **kwargs):
        self.required = kwargs.pop('required', None)
        super(DetailsMixin, self).__init__(*args, **kwargs)


class MinMaxMixin(object):
    def __init__(self, *args, **kwargs):
        self.minimum = kwargs.pop('min', None)
        self.maximum = kwargs.pop('max', None)
        super(MinMaxMixin, self).__init__(*args, **kwargs)


class String(DetailsMixin, base_fields.String):
    def __init__(self, *args, **kwargs):
        self.enum = kwargs.pop('enum', None)
        super(String, self).__init__(*args, **kwargs)


class Integer(DetailsMixin, MinMaxMixin, base_fields.Integer):
    pass


class Float(DetailsMixin, MinMaxMixin, base_fields.Float):
    pass


class Arbitrary(DetailsMixin, MinMaxMixin, base_fields.Arbitrary):
    pass


class Boolean(DetailsMixin, base_fields.Boolean):
    pass


class DateTime(DetailsMixin, base_fields.DateTime):
    pass


class Raw(DetailsMixin, base_fields.Raw):
    pass


class Nested(DescriptionMixin, base_fields.Nested):
    pass

class Dict(dict):
    pass

class List(DetailsMixin, base_fields.List):
    def __init__(self, cls_or_instance, **kwargs):
        if isinstance(cls_or_instance, ApiModel):
            model = Dict(cls_or_instance)
            model.__apidoc__ = cls_or_instance.__apidoc__
            cls_or_instance = Nested(model)
            cls_or_instance.__apidoc__ = model.__apidoc__
        super(List, self).__init__(cls_or_instance, **kwargs)
    pass


class Url(DetailsMixin, base_fields.Url):
    pass


class Fixed(DetailsMixin, MinMaxMixin, base_fields.Fixed):
    pass


class FormattedString(DetailsMixin, base_fields.FormattedString):
    pass

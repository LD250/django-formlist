from django.core.exceptions import ImproperlyConfigured


class FormsList(object):

    forms_list = []

    def __init__(self, **kwargs):
        if not self.forms_list:
            raise ImproperlyConfigured("Provide 'forms_list' prorerty for %s" % self.__class__.__name__)
        if not isinstance(self.forms_list, list):
            raise ImproperlyConfigured("Property 'forms_list' should return a list of form classes (%s)" % self.__class__.__name__)

        self.forms = [form_class(**kwargs.get(form_class.__name__, {})) for form_class in self.forms_list]
        self.invalid_forms = []

    def is_valid(self):
        self.invalid_forms = []
        for form in self.forms:
            if not form.is_valid():
                self.invalid_forms.append(form)
        return not self.invalid_forms

    def save(self):
        for form in self.forms:
            form.save()

    @property
    def errors(self):
        errors = {}
        for form in self.forms:
            errors.update(form.errors)
        return errors

    @property
    def fields(self):
        fields = {}
        for form in self.forms:
            fields.update(form.fields)
        return fields


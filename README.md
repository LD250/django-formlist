# django-formlist

Use form list as one form in FormView

I wrote this before i found a better solution.
Please check [bmispelon/django-multiform](https://github.com/bmispelon/django-multiform) first

Next time I will need additional features, i will consider moving to bmispelon/django-multiform

# Usage:

1 Define a FormsList object.
  ```python
    from django import forms
    from formlist import FormsList
    
    class CollorSettingsForm(forms.Form)
      foo = forms.CharField()
    
    class UserSettingsForm(forms.Form)
      foo = forms.CharField()
      
    class OtherSettingsForm(forms.Form)
      foo = forms.CharField()
  
    class SettingsList(FormsList):
      forms_list = [
        CollorSettingsForm,
        UserSettingsForm,
        OtherSettingsForm
      ]
  ```

2 Use it in FormView
  ```python
  from django.views.generic.edit import FormView
  from formlist import FormListViewMixin
  
  class SettingsListView(FormListViewMixin, FormView):
    form_class = forms.SettingsList
    template_name = 'settings_list.html'
  ```

3 Use it inside tempalte
  ```html
	<form action="/" method="post" enctype="multipart/form-data">
	  {% set color_form = form.forms[0] %}
	  {% set user_form = form.forms[1] %}
	  {% set other_form = form.forms[1] %}
	  <div class="form_content">
		  <p>{{ _('Configure color') }}</p>
			<div>
				{{ color_form.foo }}
			</div>
			.....
		</div>
	</form>
  ```

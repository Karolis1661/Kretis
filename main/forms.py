from django import forms
from main.models import ClientRequest, WebRequest, EshopRequest, DesignRequest


class UserRequest(forms.ModelForm):
    check = forms.BooleanField(required=True)

    class Meta:
        model = ClientRequest
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'text', 'check']
        widgets = {
                'first_name': forms.TextInput(attrs={'placeholder': 'Įveskite savo vardą'}),
                'last_name': forms.TextInput(attrs={'placeholder': 'Įveskite savo pavardę'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Įveskite savo el.paštą'}),
                'phone_number': forms.TextInput(attrs={'placeholder': 'Įveskite savo tel. numerį'}),
                'text': forms.Textarea(attrs={'placeholder': 'Jūsų žinutė'})
        }


class WebForm(forms.ModelForm):
    check = forms.BooleanField(required=True)

    class Meta:
        model = WebRequest
        fields = ['web_locked_uisd', 'web_locked_tvs', 'web_locked_sti', 'web_locked_iz',
                  'web_locked_uz', 'web_locked_seo', 'web_locked_gai',
                  'web_optional_fpi', 'web_optional_pk', 'web_optional_pf', 'web_optional_d',
                  'web_optional_lc', 'web_optional_st', 'web_pages_select', 'web_firm',
                  'web_website', 'first_name', 'last_name', 'email', 'phone_number', 'text',
                  'check']

        labels = {'web_locked_uisd': 'Unikalus internetinės svetainės dizainas',
                  'web_locked_tvs': 'Unikali turinio valdymo sistema',
                  'web_locked_sti': 'Socialinių tinklų integracija',
                  'web_locked_iz': 'Interaktyvūs žemėlapiai',
                  'web_locked_uz': 'Užklausos forma',
                  'web_locked_seo': 'SEO optimizavimas',
                  'web_locked_gai': 'Google Analytics integracija',
                  'web_optional_fpi': 'Facebook pixel integracija',
                  'web_optional_pk': 'Produktų katalogas',
                  'web_optional_pf': 'Produktų filtravimas',
                  'web_optional_d': 'Daugiakalbystė',
                  'web_optional_lc': 'Live chat',
                  'web_optional_st': 'Svetainės talpinimas'}

        widgets = {
            'web_locked_uisd': forms.CheckboxInput(attrs={'value': '100', 'class': 'price web-checked', 'checked': 'true'}),
            'web_locked_tvs': forms.CheckboxInput(attrs={'value': '100', 'class': 'price web-checked', 'checked': 'true'}),
            'web_locked_sti': forms.CheckboxInput(attrs={'value': '100', 'class': 'price web-checked', 'checked': 'true'}),
            'web_locked_iz': forms.CheckboxInput(attrs={'value': '100', 'class': 'price web-checked', 'checked': 'true'}),
            'web_locked_uz': forms.CheckboxInput(attrs={'value': '100', 'class': 'price web-checked', 'checked': 'true'}),
            'web_locked_seo': forms.CheckboxInput(attrs={'value': '100', 'class': 'price web-checked', 'checked': 'true'}),
            'web_locked_gai': forms.CheckboxInput(attrs={'value': '100', 'class': 'price web-checked', 'checked': 'true'}),
            'web_optional_fpi': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            'web_optional_pk': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            'web_optional_pf': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            'web_optional_d': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            'web_optional_lc': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            'web_optional_st': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            'web_pages_select': forms.Select(attrs={'class': 'select'}),
            'first_name': forms.TextInput(attrs={'class': 'h-left calc-form-fname',
                                                 'placeholder': 'Įveskite savo vardą'}),
            'last_name': forms.TextInput(attrs={'class': 'h-right calc-form-lname',
                                                'placeholder': 'Įveskite savo pavardę'}),
            'email': forms.EmailInput(attrs={'class': 'h-left calc-form-email',
                                             'placeholder': 'Įveskite savo el.paštą'}),
            'phone_number': forms.TextInput(attrs={'class': 'h-right calc-form-phone',
                                                   'placeholder': 'Įveskite savo tel. numerį'}),
            'text': forms.Textarea(attrs={'class': 'calc-msg-body',
                                          'placeholder': 'Jūsų klausimai, pastabos ir papildoma informacija...',
                                          'cols': '', 'rows': ''}),

            'web_firm': forms.TextInput(attrs={'class': 'h-left calc-form-firm',
                                               'placeholder': 'Jūsų įmonės pavadinimas (nebūtina)'}),
            'web_website': forms.TextInput(attrs={'class': 'h-right calc-form-website',
                                                  'placeholder': 'Jūsų internetinės svetainės adresas (nebūtina)'}),


        }


class EshopForm(forms.ModelForm):
    eshop_check = forms.BooleanField(required=True)

    class Meta:
        model = EshopRequest
        fields = ['eshop_first_name', 'eshop_last_name', 'eshop_email', 'eshop_phone_number',
                  'eshop_text', 'eshop_firm', 'eshop_website', 'eshop_locked_uisd',
                  'eshop_tvs_choices', 'eshop_locked_tvs', 'eshop_locked_sti', 'eshop_locked_iz',
                  'eshop_locked_uz', 'eshop_locked_seo', 'eshop_locked_gai', 'eshop_locked_fpi',
                  'eshop_locked_pk', 'eshop_locked_pf', 'eshop_optional_d', 'eshop_optional_lc',
                  'eshop_optional_st', 'eshop_check']

        labels = {'eshop_locked_uisd': 'Unikalus internetinės svetainės dizainas',
                  'eshop_locked_tvs': 'Unikali turinio valdymo sistema',
                  'eshop_locked_sti': 'Socialinių tinklų integracija',
                  'eshop_locked_iz': 'Interaktyvūs žemėlapiai',
                  'eshop_locked_uz': 'Užklausos forma',
                  'eshop_locked_seo': 'SEO optimizavimas',
                  'eshop_locked_gai': 'Google Analytics integracija',
                  'eshop_locked_fpi': 'Facebook pixel integracija',
                  'eshop_locked_pk': 'Produktų katalogas',
                  'eshop_locked_pf': 'Produktų filtravimas',
                  'eshop_optional_d': 'Daugiakalbystė',
                  'eshop_optional_lc': 'Live chat',
                  'eshop_optional_st': 'Svetainės talpinimas'}

        widgets = {
            'eshop_first_name': forms.TextInput(attrs={'class': 'h-left calc-form-fname',
                                                 'placeholder': 'Įveskite savo vardą'}),
            'eshop_last_name': forms.TextInput(attrs={'class': 'h-right calc-form-lname',
                                                'placeholder': 'Įveskite savo pavardę'}),
            'eshop_email': forms.EmailInput(attrs={'class': 'h-left calc-form-email',
                                             'placeholder': 'Įveskite savo el.paštą'}),
            'eshop_phone_number': forms.TextInput(attrs={'class': 'h-right calc-form-phone',
                                                   'placeholder': 'Įveskite savo tel. numerį'}),
            'eshop_text': forms.Textarea(attrs={'class': 'calc-msg-body',
                                          'placeholder': 'Jūsų klausimai, pastabos ir papildoma informacija...',
                                          'cols': '', 'rows': ''}),
            'eshop_firm': forms.TextInput(attrs={'class': 'h-left calc-form-firm',
                                               'placeholder': 'Jūsų įmonės pavadinimas (nebūtina)'}),
            'eshop_website': forms.TextInput(attrs={'class': 'h-right calc-form-website',
                                                  'placeholder': 'Jūsų internetinės svetainės adresas (nebūtina)'}),
            'eshop_locked_uisd': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_tvs_choices': forms.Select(attrs={'class': 'select'}),
            'eshop_locked_tvs': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_locked_sti': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_locked_iz': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_locked_uz': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_locked_seo': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_locked_gai': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_locked_fpi': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_locked_pk': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_locked_pf': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price eshop-checked', 'checked': 'true'}),
            'eshop_optional_d': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            'eshop_optional_lc': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            'eshop_optional_st': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
        }


class DesignForm(forms.ModelForm):
    design_check = forms.BooleanField(required=True)

    class Meta:
        model = DesignRequest

        fields = ['design_first_name', 'design_last_name', 'design_email', 'design_phone_number',
                  'design_text', 'design_firm', 'design_website', 'design_website_type',
                  'design_website_pages', 'design_locked_paitn', 'design_locked_kait', 'design_locked_sia',
                  'design_locked_ssk', 'design_locked_dke', 'design_locked_dmie', 'design_locked_dpe',
                  'design_locked_pk', 'design_testing_cycle', 'design_optional_tidt', 'design_check']

        labels = {'design_locked_paitn': 'Poreikių analizė ir tikslų nustatymas',
                  'design_locked_kait': 'Konkurentų analizė ir tyrimas',
                  'design_locked_sia': 'Surinktos informacijos architektūra',
                  'design_locked_ssk': 'Svetainės struktūros kūrimas',
                  'design_locked_dke': 'Dizainas kompiuterio ekranui',
                  'design_locked_dmie': 'Dizainas mobilaus įrenginio ekranui',
                  'design_locked_dpe': 'Dizainas planšetės ekranui',
                  'design_locked_pk': 'Prototipo kūrimas',
                  'design_optional_tidt': 'Testavimas ir dizaino tobulinimas'}

        widgets = {
            'design_first_name': forms.TextInput(attrs={'class': 'h-left calc-form-fname',
                                                       'placeholder': 'Įveskite savo vardą'}),
            'design_last_name': forms.TextInput(attrs={'class': 'h-right calc-form-lname',
                                                      'placeholder': 'Įveskite savo pavardę'}),
            'design_email': forms.EmailInput(attrs={'class': 'h-left calc-form-email',
                                                   'placeholder': 'Įveskite savo el.paštą'}),
            'design_phone_number': forms.TextInput(attrs={'class': 'h-right calc-form-phone',
                                                         'placeholder': 'Įveskite savo tel. numerį'}),
            'design_text': forms.Textarea(attrs={'class': 'calc-msg-body',
                                                'placeholder': 'Jūsų klausimai, pastabos ir papildoma informacija...',
                                                'cols': '', 'rows': ''}),
            'design_firm': forms.TextInput(attrs={'class': 'h-left calc-form-firm',
                                                 'placeholder': 'Jūsų įmonės pavadinimas (nebūtina)'}),
            'design_website': forms.TextInput(attrs={'class': 'h-right calc-form-website',
                                                    'placeholder': 'Jūsų internetinės svetainės adresas (nebūtina)'}),
            'design_website_type': forms.Select(attrs={'class': 'select'}),
            'design_website_pages': forms.Select(attrs={'class': 'select'}),
            'design_locked_paitn': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price design-checked', 'checked': 'true'}),
            'design_locked_kait': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price design-checked', 'checked': 'true'}),
            'design_locked_sia': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price design-checked', 'checked': 'true'}),
            'design_locked_ssk': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price design-checked', 'checked': 'true'}),
            'design_locked_dpe': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price design-checked', 'checked': 'true'}),
            'design_locked_dke': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price design-checked', 'checked': 'true'}),
            'design_locked_dmie': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price design-checked', 'checked': 'true'}),
            'design_locked_pk': forms.CheckboxInput(
                attrs={'value': '100', 'class': 'price design-checked', 'checked': 'true'}),
            'design_testing_cycle': forms.Select(attrs={'class': 'select'}),
            'design_optional_tidt': forms.CheckboxInput(attrs={'value': '100', 'class': 'price'}),
            }
from django.db import models


SELECT_OPTIONS = [
    ('Preliminarus puslapių skaičius'),
    ('Preliminarus puslapių skaičius - 5'),
    ('Preliminarus puslapių skaičius - 6'),
    ('Preliminarus puslapių skaičius - 7'),
]

class ArticleCategory(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Article categories'

    def __str__(self):
        return self.category


class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=20, unique=True)
    cover = models.ImageField(upload_to='article_covers')
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=60)
    content = models.TextField()

    def __str__(self):
        return '{0} {1}'.format(self.title, self.date)


class ClientRequest(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=12)
    text = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Contacts request'

    def __str__(self):
        return '{0} {1} {2}'.format(self.first_name, self.last_name, self.date)


class WebRequest(models.Model):
    WEB_PAGES = [
        ('0', 'Preliminarus puslapių skaičius'),
        ('50', 'Preliminarus puslapių skaičius - 5'),
        ('100', 'Preliminarus puslapių skaičius - 6'),
        ('150', 'Preliminarus puslapių skaičius - 7'),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=12)
    text = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    web_locked_uisd = models.BooleanField(default=True)
    web_locked_tvs = models.BooleanField(default=True)
    web_locked_sti = models.BooleanField(default=True)
    web_locked_iz = models.BooleanField(default=True)
    web_locked_uz = models.BooleanField(default=True)
    web_locked_seo = models.BooleanField(default=True)
    web_locked_gai = models.BooleanField(default=True)
    web_pages_select = models.CharField(max_length=20, choices=WEB_PAGES,
                                        default=WEB_PAGES[1])
    web_optional_fpi = models.BooleanField(default=False)
    web_optional_pk = models.BooleanField(default=False)
    web_optional_pf = models.BooleanField(default=False)
    web_optional_d = models.BooleanField(default=False)
    web_optional_lc = models.BooleanField(default=False)
    web_optional_st = models.BooleanField(default=False)
    web_firm = models.CharField(max_length=50, blank=True)
    web_website = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.first_name, self.last_name, self.date)


class EshopRequest(models.Model):

    TVS_CHOICES = [
        ('0', 'Pasirinkite turinio valdymo sistemą'),
        ('100', 'A'),
        ('150', 'B'),
        ('200', 'C'),
    ]
    eshop_first_name = models.CharField(max_length=20)
    eshop_last_name = models.CharField(max_length=20)
    eshop_email = models.EmailField(max_length=30)
    eshop_phone_number = models.CharField(max_length=12)
    eshop_text = models.TextField(max_length=500)
    eshop_date = models.DateField(auto_now_add=True, null=True, blank=True)
    eshop_firm = models.CharField(max_length=50, blank=True)
    eshop_website = models.CharField(max_length=50, blank=True)

    eshop_locked_uisd = models.BooleanField(default=True)
    eshop_tvs_choices = models.CharField(max_length=20, choices=TVS_CHOICES,
                                         default=TVS_CHOICES[1])
    eshop_locked_tvs = models.BooleanField(default=True)
    eshop_locked_sti = models.BooleanField(default=True)
    eshop_locked_iz = models.BooleanField(default=True)
    eshop_locked_uz = models.BooleanField(default=True)
    eshop_locked_seo = models.BooleanField(default=True)
    eshop_locked_gai = models.BooleanField(default=True)
    eshop_locked_fpi = models.BooleanField(default=True)
    eshop_locked_pk = models.BooleanField(default=True)
    eshop_locked_pf = models.BooleanField(default=True)
    eshop_optional_d = models.BooleanField(default=False)
    eshop_optional_lc = models.BooleanField(default=False)
    eshop_optional_st = models.BooleanField(default=False)

    def __str__(self):
        return '{0} {1} {2}'.format(self.eshop_first_name, self.eshop_last_name, self.eshop_date)


class DesignRequest(models.Model):
    WEBSITE_TYPE = [
        ('0', 'Pasirinkite svetainės tipą'),
        ('100', 'Portfolio'),
        ('300', 'Commerce'),
        ('800', 'Custom'),
    ]
    DESIGN_PAGES = [
        ('0', 'Preliminarus puslapių skaičius'),
        ('50', 'Preliminarus puslapių skaičius - 5'),
        ('100', 'Preliminarus puslapių skaičius - 6'),
        ('150', 'Preliminarus puslapių skaičius - 7'),
    ]
    TEST_CYCLES = [
        ('0', 'Testavimo ciklai'),
        ('100', 'A Ciklas'),
        ('200', 'B Ciklas'),
        ('300', 'C Ciklas'),
    ]
    design_first_name = models.CharField(max_length=20)
    design_last_name = models.CharField(max_length=20)
    design_email = models.EmailField(max_length=30)
    design_phone_number = models.CharField(max_length=12)
    design_text = models.TextField(max_length=500)
    design_date = models.DateField(auto_now_add=True, null=True, blank=True)
    design_firm = models.CharField(max_length=50, blank=True)
    design_website = models.CharField(max_length=50, blank=True)

    design_website_type = models.CharField(max_length=20, choices=WEBSITE_TYPE,
                                           default=WEBSITE_TYPE[1])
    design_website_pages = models.CharField(max_length=20, choices=DESIGN_PAGES,
                                            default=DESIGN_PAGES[1])

    design_locked_paitn = models.BooleanField(default=True)
    design_locked_kait = models.BooleanField(default=True)
    design_locked_sia = models.BooleanField(default=True)
    design_locked_ssk = models.BooleanField(default=True)
    design_locked_dke = models.BooleanField(default=True)
    design_locked_dmie = models.BooleanField(default=True)
    design_locked_dpe = models.BooleanField(default=True)
    design_locked_pk = models.BooleanField(default=True)

    design_testing_cycle = models.CharField(max_length=20, choices=TEST_CYCLES,
                                            default=TEST_CYCLES[1])

    design_optional_tidt = models.BooleanField(default=False)

    def __str__(self):
        return '{0} {1} {2}'.format(self.design_first_name, self.design_last_name, self.design_date)


class Projects(models.Model):

    client = models.CharField(max_length=40)
    project_url = models.CharField(max_length=40)
    type = models.CharField(max_length=25)
    intro_title = models.CharField(max_length=30)
    intro_text = models.CharField(max_length=50)
    intro_image = models.ImageField(upload_to='projects_covers')
    date = models.DateField(auto_now_add=True)

    inside_title = models.CharField(max_length=80)
    inside_text = models.CharField(max_length=200)
    inside_intro_image = models.ImageField(upload_to='project_images', blank=True, null=True)

    a_1 = models.CharField(max_length=100)
    a_2 = models.CharField(max_length=100)
    a_3 = models.CharField(max_length=100)
    a_4 = models.CharField(max_length=100)

    tech_stack_1 = models.ImageField(blank=True, null=True)
    tech_stack_2 = models.ImageField(blank=True, null=True)
    tech_stack_3 = models.ImageField(blank=True, null=True)
    tech_stack_4 = models.ImageField(blank=True, null=True)
    tech_stack_5 = models.ImageField(blank=True, null=True)

    project_image_1 = models.ImageField(blank=True, null=True)
    project_image_2 = models.ImageField(blank=True, null=True)
    project_image_3 = models.ImageField(blank=True, null=True)

    write_up = models.TextField(max_length=300)
    owner_name = models.CharField(max_length=40)
    company = models.CharField(max_length=50)
    company_logo = models.ImageField(upload_to='Projects_logos')

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return '{0}'.format(self.client)

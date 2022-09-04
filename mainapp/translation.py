from modeltranslation.translator import register, TranslationOptions
from .models import WorkExperience, Lang, Ken


@register(WorkExperience)
class WorkExperienceTranslationOptions(TranslationOptions):
    fields = ('title','profession','country','skills1','skills2','skills3','lang','ken','ken2','lang2','lang3','ken3','work1','work2','work3','Education1','Education2',)


@register(Lang)
class LangTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Ken)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)



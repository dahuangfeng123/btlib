from django.forms import ModelForm
from btlib.models import *


class FormAuthor(ModelForm):
    class Meta:
        model = Author


class FormIllustrator(ModelForm):
    class Meta:
        model = Illustrator


class FormGenre(ModelForm):
    class Meta:
        model = Genre


class FormPublisher(ModelForm):
    class Meta:
        model = Publisher


class FormProjectStatus(ModelForm):
    class Meta:
        model = ProjectStatus


class FormProjectType(ModelForm):
    class Meta:
        model = ProjectType


class FormLanguage(ModelForm):
    class Meta:
        model = Language


class FormNovel(ModelForm):
    class Meta:
        model = Novel
        exclude = ('modified', 'created')


class FormVolume(ModelForm):
    class Meta:
        model = Volume
        exclude = ('modified', 'created')


class FormChapter(ModelForm):
    class Meta:
        model = Chapter
        exclude = ('modified', 'created')


class FormProject(ModelForm):
    class Meta:
        model = Project
        exclude = ('modified', 'created')


class FormProjectTrans(ModelForm):
    class Meta:
        model = ProjectTrans
        exclude = ('modified', 'created')


class FormNovelTrans(ModelForm):
    class Meta:
        model = NovelTrans
        exclude = ('modified', 'created')


class FormVolumeTrans(ModelForm):
    class Meta:
        model = VolumeTrans
        exclude = ('modified', 'created')


class FormChapterTrans(ModelForm):
    class Meta:
        model = ChapterTrans
        exclude = ('modified', 'created')


class FormRevision(ModelForm):
    class Meta:
        model = Revision
        exclude = ('modified', 'created')


class FormNote(ModelForm):
    class Meta:
        model = Note
        exclude = ('modified', 'created')


class FormImage(ModelForm):
    class Meta:
        model = Image
        exclude = ('modified', 'created')
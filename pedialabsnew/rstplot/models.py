from django import forms
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import smart_str
from django.db import models
from pagetree.models import PageBlock


class RstPlotBlock(models.Model):
    display_name = "Rapid Strep Test Plot"
    pageblocks = GenericRelation(PageBlock)
    template_file = "rstplot/rstplot.html"
    js_template_file = "rstplot/block_js.html"
    css_template_file = "rstplot/block_css.html"

    def pageblock(self):
        return self.pageblocks.all()[0]

    def __str__(self):
        return smart_str(self.pageblock())

    def needs_submit(self):
        return False

    @classmethod
    def add_form(self):
        return RstPlotBlockForm()

    def edit_form(self):
        return RstPlotBlockForm(instance=self)

    @classmethod
    def create(self, request):
        form = RstPlotBlockForm(request.POST)
        return form.save()

    def edit(self, vals, files):
        form = RstPlotBlockForm(data=vals,
                                files=files,
                                instance=self)
        if form.is_valid():
            form.save()

    def unlocked(self, user):
        return True


class RstPlotBlockForm(forms.ModelForm):
    class Meta:
        model = RstPlotBlock
        exclude = []

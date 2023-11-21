from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
class IndexView(LoginRequiredMixin, View):
    template_name = "tuto.html"
    def get(self, request):
        return render(request, self.template_name)
# class MarkAsDoneView_HTML(View):
#     def get(self, request, course_id):
#         session = request.session
#         course_chapter_count = {
#             'html_courses': 7
#         }
#         progress_by_course = session.get('progress',{})
#         progress = progress_by_course.get(course_id, 0)
#         progress += 1
#         chapter_count = course_chapter_count.get(course_id)
#         progress_percentage = (progress / chapter_count) * 100
#         progress_by_course[course_id] = progress
#         session['progress'] = progress_by_course
#         next_chapter = progress
#         next_section = 

class HtmlIntroductionView(LoginRequiredMixin, View):
    template_name = "htmlIntroduction.html"
    def get(self, request):
        return render(request, self.template_name)
class HtmlStructureView(LoginRequiredMixin, View):
    template_name = "htmlDescription.html"
    def get(self, request):
        return render(request, self.template_name)
class HtmlTextFormatingView(LoginRequiredMixin, View):
    template_name = "htmlTextFormating.html"
    def get(self, request):
        return render(request, self.template_name)
class VSCodeIntroductionView(LoginRequiredMixin, View):
    template_name = "vscodeIntroduction.html"
    def get(self, request):
        return render(request, self.template_name)
class VSCodeExtensionView(LoginRequiredMixin, View):
    template_name = "vscodeExtension.html"
    def get(self, request):
        return render(request, self.template_name)
# Create your views here.

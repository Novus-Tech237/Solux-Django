from django.contrib import admin
from django.urls import path
from .views import *

app_name = "tutos"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('vscode/', VSCodeTutoView.as_view(), name="vscode"),
    path('html/', HtmlTutoView.as_view(), name="html"),
    path('html/introduction', HtmlIntroductionView.as_view(), name="html_introduction"),
    # path('html/description', HtmlDescriptionView.as_view(), name="html_description"),
    # path('html/tags', HtmlTagsView.as_view(), name="html_tags"),
    # path('html/structure/head', HtmlHeadView.as_view(), name="html_head"),
    # path('html/structure/title', HtmlTitleView.as_view(), name="html_title"),
    # path('html/structure/charset', HtmlCharsetView.as_view(), name="html_charset"),
    # path('html/structure/body', HtmlBodyView.as_view(), name="html_body"),
    # path('html/structure/semantics', HtmlSemanticsView.as_view(), name="html_semantics"),
    # path('html/text-formatting/headings', HtmlHeadingsView.as_view(), name="html_headings"),
    # path('html/text-formatting/paragraphs', HtmlParagraphsView.as_view(), name="html_paragraphs"),
    # path('html/text-formatting/bold', HtmlBoldView.as_view(), name="html_bold"),
    # path('html/text-formatting/strong', HtmlStrongView.as_view(), name="html_strong"),
    # path('html/text-formatting/attributes', HtmlAttributesView.as_view(), name="html_attributes"),
    # path('html/text-formatting/spans', HtmlSpansView.as_view(), name="html_spans"),
    # path('html/media/images', HtmlImagesView.as_view(), name="html_images"),
    # path('html/media/media', HtmlMediaView.as_view(), name="html_media"),
    # path('html/media/audio', HtmlAudioView.as_view(), name="html_audio"),
    # path('html/media/iframes', HtmlIframesView.as_view(), name="html_iframes"),
    # path('html/media/youtube', HtmlYoutubeView.as_view(), name="html_youtube"),
    # path('html/media/plugins', HtmlPluginsView.as_view(), name="html_plugins"),
    # path('html/list-tables/list', HtmlListView.as_view(), name="html_list"),
    # path('html/list-tables/tables', HtmlTablesView.as_view(), name="html_tables"),
    # path('html/forms-divs/forms', HtmlFormsView.as_view(), name="html_forms"),
    # path('html/forms-divs/form-attributes', FormAttributesView.as_view(), name="form_attributes"),
    # path('html/forms-divs/form-elements', FormElementsView.as_view(), name="form_elements"),
    # path('html/forms-divs/input-types', HtmlInputTypesView.as_view(), name="html_input_types"),
    # path('html/forms-divs/input-attributes', HtmlInputAttributesView.as_view(), name="html_input_attributes"),
    # path('html/forms-divs/input-form-attributes', HtmlInputFormAttributesView.as_view(), name="html_input_form_attributes"),
    # path('html/forms-divs/divs', HtmlDivsView.as_view(), name="html_divs"),
    # path('html/forms-divs/classes', HtmlClassesView.as_view(), name="html_classes"),
    # path('html/forms-divs/id', HtmlIdView.as_view(), name="html_id"),
    # path('html/advance-tags-emmets/other-html-tags', OtherHtmlTagsView.as_view(), name="other_html_tags"),
    # Add more paths for other tutorials or sections as needed
]
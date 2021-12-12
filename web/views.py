from django.views.generic import TemplateView


class Demo(TemplateView):
    template_name = "hello.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["world"] = "cool"
        ctx["hello"] = "world"
        return ctx

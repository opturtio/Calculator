from ui.about_view import about_view as default_about_view


class AboutService:
    def __init__(self, about_view=default_about_view):
        self._about_view = about_view

    def initialize_about_view(self):
        self._about_view.show_about_view()
        self._about_view.print_info()


about_service = AboutService() # pylint: disable=invalid-name

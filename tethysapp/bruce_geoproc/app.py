from tethys_sdk.base import TethysAppBase, url_map_maker


class BruceGeoproc(TethysAppBase):
    """
    Tethys app class for Bruce Geoproc.
    """

    name = 'Bruce Geoproc'
    index = 'bruce_geoproc:home'
    icon = 'bruce_geoproc/images/BYU.jpg'
    package = 'bruce_geoproc'
    root_url = 'bruce-geoproc'
    color = '#F1650F'
    description = 'This app includes the buffer point geoservers tool.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='bruce-geoproc',
                controller='bruce_geoproc.controllers.home'
            ),
            UrlMap(
                name='group',
                url='bruce-geoproc/group',
                controller='bruce_geoproc.controllers.group'
            ),
        )

        return url_maps

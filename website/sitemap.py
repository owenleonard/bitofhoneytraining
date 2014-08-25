from django.contrib.sitemaps import Sitemap


class MainSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/"
    changefreq = "monthly"
    priority = "1"

class DirectionsSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/directions"
    changefreq = "monthly"
    priority = "1"

class FacilitiesSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/facilities"
    changefreq = "monthly"
    priority = "1"

class LessonHorsesSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/lesson_horses"
    changefreq = "monthly"
    priority = "1"

class PicturesSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/pictures"
    changefreq = "monthly"
    priority = "1"

class ReadingSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/reading"
    changefreq = "monthly"
    priority = "1"

class ServicesSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/services"
    changefreq = "monthly"
    priority = "1"

class TrainerSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/trainer"
    changefreq = "monthly"
    priority = "1"

class TestimonialsSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/testimonials"
    changefreq = "monthly"
    priority = "1"

class PtSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/pt"
    changefreq = "monthly"
    priority = "1"

class HolisticSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/holistic"
    changefreq = "monthly"
    priority = "1"

class FittingSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/fitting"
    changefreq = "monthly"
    priority = "1"

class ConsultingSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/consulting"
    changefreq = "monthly"
    priority = "1"

class InstructionSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/instruction"
    changefreq = "monthly"
    priority = "1"

class CalendarSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/calendar"
    changefreq = "monthly"
    priority = "1"

class EstimatorSitemap( Sitemap ):

    def items(self):
        return [self]

    location = "/estimator"
    changefreq = "monthly"
    priority = "1"

sitemaps = {
    '/': MainSitemap,
    '/directions': DirectionsSitemap,
    '/facilities': FacilitiesSitemap,
    '/lesson_horses': LessonHorsesSitemap,
    '/pictures': PicturesSitemap,
    '/reading': ReadingSitemap,
    '/services': ServicesSitemap,
    '/trainer': TrainerSitemap,
    '/testimonials': TestimonialsSitemap,
    '/pt': PtSitemap,
    '/holistic': HolisticSitemap,
    '/fitting': FittingSitemap,
    '/consulting': ConsultingSitemap,
    '/instruction': InstructionSitemap,
    '/calendar': CalendarSitemap,
    '/estimator': EstimatorSitemap,
}

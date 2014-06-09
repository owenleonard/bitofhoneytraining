from django.shortcuts import render_to_response
from website.models import Testimonial

# Create your views here.

def index(request):
    return render_to_response('bitofhoney/index.html', {'page': 'index', 'header': 'Bit of Honey Training'})

def directions(request):
    return render_to_response('bitofhoney/directions.html', {'page': 'directions', 'header': 'Directions'})

def facilities(request):
    return render_to_response('bitofhoney/facilities.html', {'page': 'facilities', 'header': 'Facilities'})

def lesson_horses(request):
    return render_to_response('bitofhoney/lesson_horses.html', {'page': 'lesson_horses', 'header': 'Lesson Horses'})

def pictures(request):
    return render_to_response('bitofhoney/pictures.html', {'page': 'pictures', 'header': 'Pictures'})

def reading(request):
    return render_to_response('bitofhoney/reading.html', {'page': 'reading', 'header': 'Recommended Reading'})

def services(request):
    return render_to_response('bitofhoney/services.html', {'page': 'services', 'header': 'Other Services'})

def trainer(request):
    return render_to_response('bitofhoney/trainer.html', {'page': 'trainer', 'header': 'Trainer'})

def testimonials(request):
    testimonials = Testimonial.objects.filter(display=True)
    return render_to_response('bitofhoney/testimonials.html', {'page': 'testimonials', 'header': 'Testimonials', 'testimonials': testimonials})

def pt(request):
    return render_to_response('bitofhoney/pt.html', {'page': 'pt', 'header': 'PT & Rehab'})

def holistic(request):
    return render_to_response('bitofhoney/holistic.html', {'page': 'holistic', 'header': 'Holistic Training'})

def fitting(request):
    return render_to_response('bitofhoney/fitting.html', {'page': 'fitting', 'header': 'Saddle & Tack Fitting'})

def consulting(request):
    return render_to_response('bitofhoney/consulting.html', {'page': 'consulting', 'header': 'Consulting'})

def instruction(request):
    return render_to_response('bitofhoney/instruction.html', {'page': 'instruction', 'header': 'Riding Instruction'})

def calendar(request):
    return render_to_response('bitofhoney/calendar.html', {'page': 'calendar', 'header': 'Calendar'})

from itertools import groupby
from re import match, search
from binascii import unhexlify

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from editor.models import Card
from editor.forms import UploadFileForm


def index(request):

    cards = Card.objects.all()

    template = loader.get_template('editor/index.html')
    context = {'cards': cards}

    return HttpResponse(template.render(context, request))


def load_cards(request):

    vcf_file = request.FILES.get('vcf_file', list())

    cards = list()

    tmp_details = dict()
    for line in vcf_file:
        line = line.decode('utf-8')
        if line.startswith('BEGIN:VCARD'):
            tmp_details = dict()
            continue
        if line.startswith('END:VCARD'):
            cards.append(tmp_details)
            Card.objects.create(**tmp_details)
            continue
        key = match(r'\w*', line).group(0)

        if 'ENCODING=QUOTED-PRINTABLE' in line:
            raw = search(r'(=[0-9a-zA-z]{2}){2,10000}', line).group(0)
            value = unhexlify(raw.replace('=', '')).decode('utf-8')
        else:
            value = line
        cleaners = [
            '\r\n', 'CELL;PREF', ';;;', ';',
            '{}:'.format(key),
            '{};'.format(key)]
        for c in cleaners:
            value = value.replace(c, '')

        if key:
            tmp_details[key.lower()] = value

    # form = UploadFileForm(request.POST, request.FILES)


def modify_card(request):
    pass


def delete_card(request):
    pass

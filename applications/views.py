from django.shortcuts import render, redirect
from datetime import date
import requests
from requests import Session
from requests_ntlm import HttpNtlmAuth
import json
from django.conf import settings as config
import datetime

# Create your views here.


def submittedOpenTenders(request):
    session = requests.Session()
    session.auth = config.AUTHS

    Access_Point = config.O_DATA.format("/ProcurementMethods")
    try:
        response = session.get(Access_Point, timeout=10).json()
        open = []
        for tender in response['value']:
            if tender['Process_Type'] == 'Tender' and tender['TenderType'] == 'Open Tender' and tender['Status'] == 'Archived':
                output_json = json.dumps(tender)
                open.append(json.loads(output_json))

    except requests.exceptions.ConnectionError as e:
        print(e)
    # Get Timezone
    # creating date object
    todays_date = datetime.datetime.now().strftime("%b. %d, %Y %A")
    ctx = {"today": todays_date, "res": open}

    return render(request, 'Open/SubOpenTender.html', ctx)


def submittedResTenders(request):
    session = requests.Session()
    session.auth = config.AUTHS

    Access_Point = config.O_DATA.format("/ProcurementMethods")
    try:
        response = session.get(Access_Point, timeout=10).json()
        Restrict = []
        for tender in response['value']:
            if tender['Process_Type'] == 'Tender' and tender['TenderType'] == "Restricted Tender" and tender['Status'] == 'Archived':
                output_json = json.dumps(tender)
                Restrict.append(json.loads(output_json))
    except requests.exceptions.ConnectionError as e:
        print(e)
    # Get Timezone
    # creating date object
    todays_date = datetime.datetime.now().strftime("%b. %d, %Y %A")
    ctx = {"today": todays_date, "res": Restrict}

    return render(request, 'SubResTender.html', ctx)


def submittedRFQ(request):

    return render(request, 'Sub-RFQ.html')


def submittedInterest(request):

    return render(request, 'SubInterest.html')

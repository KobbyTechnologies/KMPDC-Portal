from django.shortcuts import render, redirect
from datetime import date
import requests
from requests import Session
from requests_ntlm import HttpNtlmAuth
import json
from django.conf import settings as config
import datetime
from django.contrib import messages


# Create your views here.


def requestQuote(request):
    session = requests.Session()
    session.auth = config.AUTHS

    year = request.session['years']
    Access_Point = config.O_DATA.format("/ProcurementMethods")
    Access = config.O_DATA.format("/QyProspectiveSupplierTender")
    try:
        response = session.get(Access_Point, timeout=10).json()
        responses = session.get(Access, timeout=10).json()
        OpenRFQ = []
        Submitted = []
        for tender in response['value']:
            if tender['Process_Type'] == 'RFQ' and tender['SubmittedToPortal'] == True and tender['Status'] == 'New':
                output_json = json.dumps(tender)
                OpenRFQ.append(json.loads(output_json))
        for tender in responses['value']:
            if tender['Type'] == 'RFQ' and tender['Vendor_No'] == request.session['vendorNo']:
                output_json = json.dumps(tender)
                Submitted.append(json.loads(output_json))
    except requests.exceptions.ConnectionError as e:
        print(e)

    count = len(OpenRFQ)
    counter = len(Submitted)
    # Get Timezone
    # creating date object
    todays_date = datetime.datetime.now().strftime("%b. %d, %Y %A")
    ctx = {"today": todays_date, "res": OpenRFQ,
           "count": count, "counter": counter,
           "year": year, "sub": Submitted}
    return render(request, 'requestQuote.html', ctx)

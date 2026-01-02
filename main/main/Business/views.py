import json
import hmac
import hashlib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .router import route_payment

@csrf_exempt
def paystack_webhook(request):
    signature = request.headers.get("X-Paystack-Signature", "")
    body = request.body

    computed_signature = hmac.new(
        settings.PAYSTACK_SECRET_KEY.encode(),
        body,
        hashlib.sha512
    ).hexdigest()

    if signature != computed_signature:
        return JsonResponse({"error": "Invalid signature"}, status=400)

    event = json.loads(body)

    if event.get("event") != "charge.success":
        return JsonResponse({"status": "ignored"}, status=200)

    try:
        route_payment(event)
    except Exception as e:
        print("Webhook error:", e)


    return JsonResponse({"status": "success"}, status=200)
